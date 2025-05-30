import multiprocessing
import time

def producer(queue, data):
    for item in data:
        queue.put(item)
        time.sleep(1)  # Simulate some processing time
    queue.put(None)  # Signal the end of data

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break  # Stop when a signal is received
        print(f"Consumed: {item}")
        time.sleep(2)  # Simulate some processing time

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    queue = multiprocessing.Queue()

    # Start producer
    producer_process = multiprocessing.Process(target=producer, args=(queue, data))
    producer_process.start()

    # Start consumer
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))
    consumer_process.start()

    # Wait for processes to finish
    producer_process.join()
    consumer_process.join()

    print("Finished")