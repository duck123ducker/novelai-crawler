import time
import re

def w_f_list( file_save , raws ):
    with open(file_save, "w", encoding='utf-8') as file:#存入新信息
        for raw in raws:
            file.write(str(raw) + '\n')

def r_f( file_read ):
    with open(file_read, "r", encoding='utf-8') as file:#读取信息
        contents = [line.rstrip() for line in file]
    return contents

def get_beijin_time(t):
    return time.strftime('%H:%M:%S',time.gmtime(t + 28800))

def duplicate_remove():
    a=r_f('open_port.txt')
    if len(a)<=1:
        return
    b=[]
    c = []
    for ai in a:
        if (ai not in b)&(ai!=''):
            b.append(ai)
    for bi in b:
        c.append(re.split('\.|:',bi))
    for index in range(len(c)):
        for i in range(4):
            c[index][i]=int(c[index][i])
    a=sorted(c, key=lambda x: (x[1],x[2],x[3]))
    c=[]
    for ai in a:
        c.append(str(ai[0])+'.'+str(ai[1])+'.'+str(ai[2])+'.'+str(ai[3])+':'+str(ai[4]))
    w_f_list('open_port.txt',c)