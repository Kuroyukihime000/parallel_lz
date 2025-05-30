import subprocess
def ping(ip):
    result = subprocess.run(["ping", "-c", "1", ip], capture_output = True)
    print(f"{ip} is {'up' if result.returncode == 1 else 'down'}")

adds = ['112.212.124.111', '81.51.12.230', '49.92.151.176', '146.76.200.248',
         '74.22.206.38','150.154.127.130','155.189.243.215','126.202.18.5',
         '219.107.21.234','147.199.104.13']
for ip in adds: 
    ping(ip)