import time
import random
import threading
import logging
from instagrapi import Client
from flask import Flask

app = Flask(__name__)
spam_status = {"total_sent": 0, "running": True}

@app.route('/')
def home():
    return f"<h1>HAWK SUJAL ALIVE</h1><h2>Sent: {spam_status['total_sent']}</h2><p>KING KUNAL 24x7 RUNNING</p>"

USERNAME   = "sujalgotban"
PASSWORD   = "sujal@007"
THREAD_ID  = 1810955266238485

# PURA LAMBA MESSAGE — EK HI LINE MEIN — KOI \n NAHI — 100% SAFE
MESSAGES = [
    "KING-KUNAL-EBUU-DEVIL-NOOR-SHER} RAMU KAKA LADKE TMKC ˚✦ . . ˚ . . ✦ ˚ . ★⋆. . ˚ * ✦ . . ✦ ˚ ˚ KING-KUNAL-EBUU-DEVIL-NOOR-SHER} Ŗ̜̯͟͡A͢͏̜̖̙̲M͏̬̗͍͓̘Ų̵̼̳̱͙͎̲̘̩ K͏͈̯̭̭̥̠̗̙A͢͏̜̖̙̲K͏͈̯̭̭̥̠̗̙A͢͏̜̖̙̲ K͏͈̯̭̭̥̠̗̙ L̶̥̤̤̪̜̩͇͟A͢͏̜̖̙̲D̷̰̘̹͈̜̺͓͇̀K͏͈̯̭̭̥̠̗̙E̱̭̘̫̮ T̩̙̰̬͙͖ͅM͏̬̗͍͓̘K͏͈̯̭̭̥̠̗̙C ˚✦ . . ˚ . . ✦ ˚ . ★⋆. . ˚ * ✦ . . ✦ ˚ ˚ KING-KUNAL-EBUU-DEVIL-NOOR-SHER} RAMU KAKA LADKE TMKC"
]

DELAY       = 8.0
CYCLE_BREAK = 35
NUM_THREADS = 1

logging.basicConfig(filename='spam_log.log', level=logging.INFO)

class HawkSujalSpammer:
    def __init__(self):
        self.client = Client()
        self.client.delay_range = [1, 4]
        self.running = True
        self.total_sent = 0

    def login(self):
        for i in range(5):
            try:
                self.client.login(USERNAME, PASSWORD)
                print("KING KUNAL LOGIN SUCCESSFUL!")
                return True
            except:
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
                print(f"Sent #{self.total_sent} → KING KUNAL BOMB")
                time.sleep(DELAY * random.uniform(0.9, 1.3))
                if self.total_sent % 50 == 0:
                    time.sleep(CYCLE_BREAK)
            except:
                time.sleep(30)

    def start(self):
        if self.login():
            print("KING KUNAL 24x7 SPAMMER STARTED 🔥")
            threading.Thread(target=self.send_message, daemon=True).start()
        while True:
            time.sleep(10)

spammer = HawkSujalSpammer()
threading.Thread(target=spammer.start, daemon=True).start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
