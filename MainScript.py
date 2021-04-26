from Reminder import main
from time import time, sleep
from datetime import datetime



def execute():

    sleep(60 - time() % 60)
    while True:
        if (datetime.now().minute % 5) != 0:
            sleep(60 - time() % 60)
        else:
            main()


if __name__ == "__main__":

    execute()
