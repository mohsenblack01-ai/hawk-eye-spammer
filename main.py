import time
import random
import threading
import logging
import signal
import sys
from instagrapi import Client
from flask import Flask

# ====================== FLASK SETUP (Uptime Robot ke liye) ======================
app = Flask(__name__)
spam_status = {
    "total_sent": 0,
    "running": True,
    "last_message": "Bot started..."
}

@app.route('/')
def home():
    return f"""
    <h1>HAWK SUJAL SPAMMER IS ALIVE</h1>
    <h2>Total Messages Sent: {spam_status['total_sent']}</h2>
    <p>Last: {spam_status['last_message']}</p>
    <p>Status: {'RUNNING' if spam_status['running'] else 'STOPPED'}</p>
    """

# ====================== CONFIGURATION (YAHAN APNA DATA DAAL) ======================
USERNAME   = "sujalgotban"           # ←← CHANGE KAR
PASSWORD   = "sujal@007"           # ←← CHANGE KAR
THREAD_ID  = 1810955266238485       # ←← Group ka number only daal

MESSAGES = [                           # ←← Yahan jitne message chahe daal de
    "Bhai aa gaya re",
    "Hawk Sujal is here",
    "Spam time baby",
    "Check karo bhai log",
    "Kaisa hai sab?",
]

DELAY = 1.5
CYCLE_BREAK = 15
NUM_THREADS = 2
# =====================================================================

logging.basicConfig(filename='spam_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class HawkSujalSpammer:
    def __init__(self):
        self.client = Client()
        self.client.delay_range = [1, 4]
        self.running = True
        self.total_sent = 0
        self.consecutive_errors = 0

    def login(self):
        for i in range(5):
            try:
                print(f"Login attempt {i+1}/5...")
                self.client.login(USERNAME, PASSWORD)
                print("LOGIN SUCCESSFUL - HAWK SUJAL IS READY!")
                logging.info("Login successful")
                return True
            except Exception as e:
                print(f"Login failed: {e}")
                logging.error(f"Login failed: {e}")
                time.sleep(30)
        print("Permanent login failed!")
        return False

    def send_message(self):
        global spam_status
        while self.running:
            try:
                msg = random.choice(MESSAGES)
                self.client.direct_send(msg, thread_ids=[THREAD_ID])
                self.total_sent += 1
                spam_status["total_sent"] = self.total_sent
                spam_status["last_message"] = msg

                print(f"Sent #{self.total_sent} → {msg}")
                logging.info(f"Sent #{self.total_sent}: {msg}")

                self.consecutive_errors = 0
                time.sleep(DELAY * random.uniform(0.8, 1.4))

                # Har 50 message ke baad chhota break
                if self.total_sent % 50 == 0:
                    print(f"50 messages sent! Taking {CYCLE_BREAK}s break...")
                    time.sleep(CYCLE_BREAK)

            except Exception as e:
                self.consecutive_errors += 1
                error_msg = str(e)
                print(f"Error #{self.consecutive_errors}: {error_msg}")
                logging.error(f"Error: {error_msg}")

                if "too many requests" in error_msg.lower() or "500" in error_msg:
                    print("Too many requests! Sleeping 5 minutes...")
                    time.sleep(300)

                time.sleep(30)

    def start(self):
        if not self.login():
            spam_status["running"] = False
            return

        print("SPAMMER STARTED - 24×7 MODE")
        print(f"Target: {THREAD_ID} | Messages: {len(MESSAGES)} | Threads: {NUM_THREADS}")

        for i in range(NUM_THREADS):
            t = threading.Thread(target=self.send_message, daemon=True)
            t.start()
            time.sleep(3)

        # Keep Flask alive
        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            print("Shutting down...")
            self.running = False

# ====================== START EVERYTHING ======================
spammer = HawkSujalSpammer()
threading.Thread(target=spammer.start, daemon=True).start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
