import time
import threading

def long_task(length: float, name="Task"):
    print(f"⏳ {name} is starting...")
    time.sleep(length)
    print(f"✅ {name} is complete!")

def new_thread(task):
    thread = threading.Thread(target=task)
    thread.start()
    return thread