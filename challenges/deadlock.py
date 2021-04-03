import random
import time
import threading
from typing import List

threads: List[threading.Thread] = [None]
lock_map = {}

def go_wait():
    # Wait for other threads to initialize
    time.sleep(0.25)

    # Pick a thread at random
    thread = random.choice(
        list(filter(lambda k: k != threading.current_thread(), threads)))

    # Fill in the `lock map`
    lock_map[threading.current_thread()] = thread

    if thread is not None:
        # Wait for the thread to finish
        print(f"[{threading.current_thread().getName()}] Waiting for {thread.getName()}...")
        thread.join()
    else:
        # We picked no thread
        print(f"[{threading.current_thread().getName()}] Not waiting on any thread!")

    # Announce we're done!
    print(f"[{threading.current_thread().getName()}] Done!")


for i in range(5):
    thread = threading.Thread(target=go_wait)
    threads.append(thread)
    thread.start()

# Wait for everything to get started
time.sleep(0.5)

# Two steps to this challenge:
# 1) Use the `lock_map` to detect a deadlock (think about _cycles_)
# 2) Depending on the deadlock(s) you find, kill as few threads as possible to end the deadlock.
#    You can kill threads with `thread._stop()`