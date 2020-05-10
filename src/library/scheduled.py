# -*- coding: utf-8 -*-
import threading
import datetime
import time
from .gmail import CustomGmail
from .outlook import CustomOutlook


class CustomScheduled():
    def __init__(self):
        self.thread_a = CustomThread(1, "Thread-1")
        self.msg = ''

    def start(self):
        try:
            self.thread_a.start()
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is started"

    def stop(self):
        try:
            self.thread_a.stop()
            self.thread_a = CustomThread(1, "Thread-1")
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is stopped"

    def restart(self):
        try:
            self.thread_a.restart()
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is restarted"


class CustomThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = 20

        self.stoprequest = threading.Event()

    def run_mailbox_process(self):
        print("thread running ... ")
        gmail = CustomGmail()
        gmail.read_email_from_gmail()
        outlook = CustomOutlook()
        outlook.read_email_from_outlook()

    def start(self):
        threading.Thread.start(self)

    def stop(self):
        self.stoprequest.set()

    def restart(self):
        threading.Thread.__init__(self)
        threading.Thread.start(self)

    def run(self):
        while not self.stoprequest.isSet():
            self.run_mailbox_process()
            time.sleep(self.delay)
