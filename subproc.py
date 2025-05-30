import subprocess
import threading
import time


def ping(ip):
    result = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    print(f"{ip} is {'up' if result.returncode == 1 else 'down'}")

ips = ['20.122.7.178',
'239.230.29.179',
'231.218.110.223',
'37.59.92.2',
'230.59.47.120',
'222.203.39.124',
'121.111.91.242',
'234.227.65.184',
'215.208.150.127',
'217.247.62.43']


def lil (ips):
    start_time = time.time()
    for ip in ips:
        ping(ip)
    posled_time = time.time() - start_time
    print(f"The sequential check took: {posled_time:.2f} sec\n")
    return posled_time


def potoks(ips):
    threads = []
    start_time_potoki = time.time()
    for ip in ips:
        thread = threading.Thread(target=ping, args=(ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    potoki_time = time.time() - start_time_potoki
    print(f"Testing using threads took: {potoki_time:.2f} \n")
    return potoki_time


pos_time = lil(ips)
potok_time = potoks(ips)

print(f"Difference - {pos_time - potok_time:.2f} sec")