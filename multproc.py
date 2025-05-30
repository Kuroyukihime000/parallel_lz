import multiprocessing
import time

def producer(queue, data):
    for item in data:
        queue.put(item)
        time.sleep(0.5)
    queue.put(None) 

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(0.1) 

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    queue = multiprocessing.Queue()

    produc = multiprocessing.Process(target=producer, args=(queue, data))
    produc.start()

    consum = multiprocessing.Process(target=consumer, args=(queue,))
    consum.start()

    produc.join()
    queue.put(None) 
    consum.join()

    print("Finished")
