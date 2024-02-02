import threading
from time import sleep


def do_job(number):
    sleep(3)
    print(f"Job {number} finished")


def main():
    for i in range(5):
        thread = threading.Thread(target=do_job, args=(i,))
        # This does not start the thread immediately,
        # but instead allows the operating system to schedule the
        # function to execute as soon as possible.
        thread.start()


main()
