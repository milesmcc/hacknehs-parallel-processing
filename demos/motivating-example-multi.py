from utils import long_task, new_thread

new_thread(lambda: long_task(3, name="Movie download"))
new_thread(lambda: long_task(4, name="Pie baking"))
new_thread(lambda: long_task(2, name="Dog walking"))