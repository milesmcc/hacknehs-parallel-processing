from utils import long_task, new_thread

new_thread(lambda: long_task(3, name="Task #1"))
new_thread(lambda: long_task(4, name="Task #2"))
new_thread(lambda: long_task(2, name="Task #3"))