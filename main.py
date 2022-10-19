import socket
import argparse
import threading
import time
from threading import Thread
from utils import get_beijin_time,duplicate_remove

def ip2int(ip):
    lis = ip.split('.')
    return int("%02x%02x%02x%02x" % (int(lis[0]), int(lis[1]), int(lis[2]), int(lis[3])), 16)

def int2ip(num):
    hexIP = str('%08x' % num)
    return str("%i.%i.%i.%i" % (int(hexIP[0:2], 16), int(hexIP[2:4], 16), int(hexIP[4:6], 16), int(hexIP[6:8], 16)))

def main(f,to,tm):
    print(f, to)
    while 1:
        port=6969
        start_time = time.time()
        for target in [int2ip(x) for x in range(ip2int(f), ip2int(to) + 1)]:
            print(target)
            t = Thread(target=portscan, args=(target, port))
            t.start()
        end_time = time.time()
        print("All done in %.2f s" % (end_time - start_time))
        print('Done at ' + get_beijin_time(time.time()) + ',next scan start at ' + get_beijin_time(time.time() + tm))
        time.sleep(tm)


def portscan(target, port):
    try:
        socket.setdefaulttimeout(1)
        client = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target, int(port)))
        client.close()
        mutex.acquire()
        with open("open_port.txt", "a") as f:
            f.write("%s:%d\n" % (target, int(port)))
        mutex.release()
        mutex.acquire()
        duplicate_remove()
        mutex.release()
    except Exception as e:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str, default='10.0.0.0')
    parser.add_argument('--t', type=str, default='10.255.255.255')
    parser.add_argument('--i', type=int, default=3600)
    args = parser.parse_args()
    mutex=threading.Lock()
    main(args.f,args.t,args.i)
