import time
import concurrent

def thread_function(name):
    print(f'Thread {name} starting at {time.time}')
    time.sleep(2)
    print(f'Thread {name} ending at {time.time}')

if __name__ == "__main__":

    import threading
    from concurrent.futures import ThreadPoolExecutor

"""    x = threading.Thread(target=thread_function, args=(1,))
    print("Main    : before running thread")
    x.start()
    print("Main    : after running thread")
    x.join()
    print("Main    : all done") """
    
""" threads = list()
for index in range(3):
    print(f'Main    : before running thread')
    x = threading.Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    print('Main    : waiting for the thread to finish')
    thread.join()
    print('Main    : all done') """

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_function, range(3))