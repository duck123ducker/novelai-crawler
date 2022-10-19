import socket
import threading
import time
from threading import Thread
from utils import r_f

a=r_f('open_port.txt')
i=0
#print(a)
def main():
    for ai in a:
        if ai !='':
            target=ai.split(':')[0]
            port = ai.split(':')[1]
            t = Thread(target=portscan, args=(target, port))
            t.start()  # 开始线程


def portscan(target, port):
    try:
        socket.setdefaulttimeout(1)
        client = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target, int(port)))
        mutex.acquire()
        print("[*] %s:%d 在线" % (target, int(port)))
        global i
        i+=1
        mutex.release()
        client.close()
    except Exception as e:
        pass

if __name__ == "__main__":
    mutex = threading.Lock()
    main()
    time.sleep(2)
    print('当前在线服务:' + str(i))