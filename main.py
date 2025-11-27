import time
import random
import threading
import logging
from instagrapi import Client
from flask import Flask

# ====================== FLASK SETUP ======================
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
    <p>Status: {'RUNNING' if spam_status['running'] else 'STOPPED'}</p>
    """

# ====================== CONFIGURATION ======================
USERNAME   = "sujalgotban"
PASSWORD   = "sujal@007"
THREAD_ID  = 1810955266238485

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# TERA NAYA LAMBA MESSAGE YAHAN HAI (bilkul perfect copy-paste)
MESSAGES = [
    "KING-KUNAL-EBUU-DEVIL-NOOR-SHER} ̰͖̯͕̥̱̲̰̳͟Ŗ̜̯͟͡A͢͏̛̜̖̙̲͍̥M͏̬̗͍͓̘̗͈̳̙̕ͅŲ̵̼̳̱͙͎̲̘̩  ̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙A͢͏̜̖̙̲̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙A͢͏̜̖̙̲  ̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙  ̷̠̤͓͉̱̹͖̻͓͝L̶̥̤̤̪̜̩͇͟A͢͏̵̸̜̖̙̲͈̝͚̻̣̲̩͔̝́D̷̰̘̹͈̜̺͓͇̖̻̰̟̟̀͝K͏͈̯̭̭̥̠̗̙҉̶̡͕͓̪͚͕̩͈͔̩E̱̭̘̫̮  ̙̥̻̰̻̀͡T̛̩̙̰̬͙͖͍̥ͅM͏̬̗͍͓̘̖̻̰̟̟͝K͏̵̶͈̯̭̭̥̠̗̙̱͉̳̠͢C̢̩͍̳̱͠ \n"
    "˚　　　　✦　　　.　　. 　 ˚　.　　　　　 . ✦　　　 　˚　　　　 . ★⋆.\n"
    "　　　.   　˚　　 　　*　　 　　✦　　　.　　.　　　✦　˚ 　　　\n"
    "KING-KUNAL-EBUU-DEVIL-NOOR-SHER} ̰͖̯͕̥̱̲̰̳͟Ŗ̜̯͟͡A͢͏̛̜̖̙̲͍̥M͏̬̗͍͓̘̗͈̳̙̕ͅŲ̵̼̳̱͙͎̲̘̩  ̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙A͢͏̜̖̙̲̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙A͢͏̜̖̙̲  ̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙  ̷̠̤͓͉̱̹͖̻͓͝L̶̥̤̤̪̜̩͇͟A͢͏̵̸̜̖̙̲͈̝͚̻̣̲̩͔̝́D̷̰̘̹͈̜̺͓͇̖̻̰̟̟̀͝K͏͈̯̭̭̥̠̗̙҉̶̡͕͓̪͚͕̩͈͔̩E̱̭̘̫̮  ̙̥̻̰̻̀͡T̛̩̙̰̬͙͖͍̥ͅM͏̬̗͍͓̘̖̻̰̟̟͝K͏̵̶͈̯̭̭̥̠̗̙̱͉̳̠͢C̢̩͍̳̱͠"
]
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

DELAY       = 8.0          # 8 seconds delay → bilkul safe
CYCLE_BREAK = 3import time
import random
import threading
import logging
from instagrapi import Client
from flask import Flask

# ====================== FLASK SETUP ======================
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
    <p>Status: {'RUNNING' if spam_status['running'] else 'STOPPED'}</p>
    """

# ====================== CONFIGURATION ======================
USERNAME   = "sujalgotban"
PASSWORD   = "sujal@007"
THREAD_ID  = 1810955266238485

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# TERA NAYA LAMBA MESSAGE YAHAN HAI (bilkul perfect copy-paste)
MESSAGES = [
    "KING-KUNAL-EBUU-DEVIL-NOOR-SHER} ̰͖̯͕̥̱̲̰̳͟Ŗ̜̯͟͡A͢͏̛̜̖̙̲͍̥M͏̬̗͍͓̘̗͈̳̙̕ͅŲ̵̼̳̱͙͎̲̘̩  ̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙A͢͏̜̖̙̲̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙A͢͏̜̖̙̲  ̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙  ̷̠̤͓͉̱̹͖̻͓͝L̶̥̤̤̪̜̩͇͟A͢͏̵̸̜̖̙̲͈̝͚̻̣̲̩͔̝́D̷̰̘̹͈̜̺͓͇̖̻̰̟̟̀͝K͏͈̯̭̭̥̠̗̙҉̶̡͕͓̪͚͕̩͈͔̩E̱̭̘̫̮  ̙̥̻̰̻̀͡T̛̩̙̰̬͙͖͍̥ͅM͏̬̗͍͓̘̖̻̰̟̟͝K͏̵̶͈̯̭̭̥̠̗̙̱͉̳̠͢C̢̩͍̳̱͠ \n"
    "˚　　　　✦　　　.　　. 　 ˚　.　　　　　 . ✦　　　 　˚　　　　 . ★⋆.\n"
    "　　　.   　˚　　 　　*　　 　　✦　　　.　　.　　　✦　˚ 　　　\n"
    "KING-KUNAL-EBUU-DEVIL-NOOR-SHER} ̰͖̯͕̥̱̲̰̳͟Ŗ̜̯͟͡A͢͏̛̜̖̙̲͍̥M͏̬̗͍͓̘̗͈̳̙̕ͅŲ̵̼̳̱͙͎̲̘̩  ̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙A͢͏̜̖̙̲̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙A͢͏̜̖̙̲  ̖̻̰̟̟͝K͏͈̯̭̭̥̠̗̙  ̷̠̤͓͉̱̹͖̻͓͝L̶̥̤̤̪̜̩͇͟A͢͏̵̸̜̖̙̲͈̝͚̻̣̲̩͔̝́D̷̰̘̹͈̜̺͓͇̖̻̰̟̟̀͝K͏͈̯̭̭̥̠̗̙҉̶̡͕͓̪͚͕̩͈͔̩E̱̭̘̫̮  ̙̥̻̰̻̀͡T̛̩̙̰̬͙͖͍̥ͅM͏̬̗͍͓̘̖̻̰̟̟͝K͏̵̶͈̯̭̭̥̠̗̙̱͉̳̠͢C̢̩͍̳̱͠"
]
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

DELAY       = 8.0          # 8 seconds delay → bilkul safe
CYCLE_BREAK = 35           # har 50 messages ke baad 35 sec break
NUM_THREADS = 1            # sirf ek thread

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
                print("LOGIN SUCCESSFUL - KING KUNAL IS READY!")
                logging.info("Login successful")
                return True
            except Exception as e:
                print(f"Login failed: {e}")
                time.sleep(30)
        return False

    def send_message(self):
        global spam_status
        while self.running:
            try:
                msg = random.choice(MESSAGES)
                self.client.direct_send(msg, thread_ids=[THREAD_ID])
                self.total_sent += 1
                spam_status["total_sent"] = self.total_sent

                print(f"Sent #{self.total_sent} → KING-KUNAL-EBUU-DEVIL-NOOR-SHER")
                logging.info(f"Sent #{self.total_sent}")

                self.consecutive_errors = 0
                time.sleep(DELAY * random.uniform(0.9, 1.3))

                if self.total_sent % 50 == 0:
                    print(f"50 messages sent! Taking {CYCLE_BREAK}s break...")
                    time.sleep(CYCLE_BREAK)

            except Exception as e:
                self.consecutive_errors += 1
                print(f"Error: {e}")
                if "too many requests" in str(e).lower():
                    print("Rate limit! Sleeping 5 min...")
                    time.sleep(300)
                time.sleep(30)

    def start(self):
        if not self.login():
            spam_status["running"] = False
            return
        print("SPAMMER STARTED - 24×7 MODE | KING KUNAL ON FIRE")
        threading.Thread(target=self.send_message, daemon=True).start()
        while True:
            time.sleep(10)

# ====================== START ======================
spammer = HawkSujalSpammer()
threading.Thread(target=spammer.start, daemon=True).start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)           # har 50 messages ke baad 35 sec break
NUM_THREADS = 1            # sirf ek thread

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
                print("LOGIN SUCCESSFUL - KING KUNAL IS READY!")
                logging.info("Login successful")
                return True
            except Exception as e:
                print(f"Login failed: {e}")
                time.sleep(30)
        return False

    def send_message(self):
        global spam_status
        while self.running:
            try:
                msg = random.choice(MESSAGES)
                self.client.direct_send(msg, thread_ids=[THREAD_ID])
                self.total_sent += 1
                spam_status["total_sent"] = self.total_sent

                print(f"Sent #{self.total_sent} → KING-KUNAL-EBUU-DEVIL-NOOR-SHER")
                logging.info(f"Sent #{self.total_sent}")

                self.consecutive_errors = 0
                time.sleep(DELAY * random.uniform(0.9, 1.3))

                if self.total_sent % 50 == 0:
                    print(f"50 messages sent! Taking {CYCLE_BREAK}s break...")
                    time.sleep(CYCLE_BREAK)

            except Exception as e:
                self.consecutive_errors += 1
                print(f"Error: {e}")
                if "too many requests" in str(e).lower():
                    print("Rate limit! Sleeping 5 min...")
                    time.sleep(300)
                time.sleep(30)

    def start(self):
        if not self.login():
            spam_status["running"] = False
            return
        print("SPAMMER STARTED - 24×7 MODE | KING KUNAL ON FIRE")
        threading.Thread(target=self.send_message, daemon=True).start()
        while True:
            time.sleep(10)

# ====================== START ======================
spammer = HawkSujalSpammer()
threading.Thread(target=spammer.start, daemon=True).start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
