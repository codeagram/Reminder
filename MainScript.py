from Reminder import main
from time import time, sleep
from datetime import datetime
from CustomModule import Telegram


def execute():

    sleep(60 - time() % 60)
    while True:
        if (datetime.now().minute % 5) != 0:
            sleep(60 - time() % 60)
        else:
            main()


def send_notification(notifier, message):

    telegram = Telegram()
    telegram.send_message(notifier, message)


if __name__ == "__main__":

    try:
        execute()

    except:
        notifier = 792670289
        message = "Some Problem in Telegrambot. Execution Stops!"
        send_notification(notifier, message)
