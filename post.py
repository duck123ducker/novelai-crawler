import base64
import threading
import time
import requests
import random
import json
import os
import argparse
from threading import Thread
from utils import r_f,get_beijin_time

stat = {}
count = 0
mutex1=threading.Lock()
mutex2=threading.Lock()

def task(target,prompt,uc,h,w,scl,stp):
    while 1:
        try:
            mutex1.acquire()
            stat[target]=1
            mutex1.release()
            url='http://{}/generate-stream'.format(target)
            data={"prompt":prompt,"width":w,"height":h,"scale":scl,"sampler":"k_euler_ancestral","steps":stp,"seed":random.randint(0,999999999),"n_samples":1,"ucPreset":0,"uc":uc,}
            req = requests.post(url,data=json.dumps(data),timeout=(3,43200))
            data=req.text.split(':')[3]
            image_data = base64.b64decode(data)
            mutex2.acquire()
            global count
            count += 1
            with open('images/'+tsktm+('0000'+str(count))[-5:]+'.jpg', 'wb') as f:
                f.write(image_data)
            mutex2.release()
            print(get_beijin_time(time.time())+' TASK '+ str(count) + ' : ' +('0000'+str(count))[-5:]+'.jpg Done!')
        except Exception as e:
            mutex1.acquire()
            stat[target] = 0
            mutex1.release()
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pmpt', type=str, default=None)
    parser.add_argument('--uc', type=str, default=None)
    parser.add_argument('--h', type=int, default=768)
    parser.add_argument('--w', type=int, default=512)
    parser.add_argument('--scl', type=int, default=10)
    parser.add_argument('--stp', type=int, default=28)
    args = parser.parse_args()
    if args.pmpt==None:
        print('need prompt\nexit')
        exit()
    tsktm = time.strftime('%Y-%m-%d_%H_%M_%S/', time.gmtime(time.time() + 28800))
    os.mkdir('images/' + tsktm)
    with open('images/' + tsktm + 'prompt_uc.txt', "a") as f:
        f.write(prompt + '\n' + uc)
    while 1:
        a = r_f('open_port.txt')
        for address in a:
            if address not in list(stat.keys()):
                stat[address]=0
            if stat[address]==0:
                t = Thread(target=task, args=(address,args.prompt,args.uc,args.h,args.w,args.scl,args.stp))
                t.start()
        time.sleep(random.randint(30,60))