#QUEUE:
#Bài 1:
     
import queue
q=queue.Queue()
queue_new=queue.Queue()

no_max=int(input())
for i in range (no_max+1):
    q.put(i)

no_max=q.qsize()
for i in range(no_max-1,-1,-1):
    if q.queue[i] %2==0:
        queue_new.put(q.queue[i])

queue_new.put(' ')
        
for i in range(no_max-1,-1,-1):        
    if q.queue[i] %2==1:
        queue_new.put(q.queue[i])

for i in range(no_max):
    print(queue_new.queue[i],end=' ')

#Bài 2:
import queue
def _queue_(list1):
    for elem in list1:
        blk_list=[ ]
        if elem %2==0:
            blk_list.append(elem)
        return blk_list
list1=list(input())
print(_queue_(list1))
#Bài 3:
from queue import Queue, PriorityQueue, LifoQueue
queue1=Queue()
queue1.put(1)
queue1.put(3)
queue1.put(1)
queue1.put(3)
queue1.put(1)
queue1.put(3)
tmp=queue1.qsize()
length=int(input("Nhập số giá trị"))
k=int(input("Nhập số k"))
if tmp!=length:
    pass
while tmp>0:
    value1=queue1.get()
    value2=queue1.queue[0]
    for i in range (0, length):
        if value1-value2==k or value2-value1==k:
            i+=1
        
        else:
            continue
        print(i)
    
#Josephus_Problem
def Jusephus(N,M):
    list1=[]
    for elem in range (1, N+1):
        list1.append(elem)
    while len(list1)>1:
        pos=M-1
        out=list1[(pos)%len(list1)]
        list1.pop(out)
        pos+=M-1
        pos=pos%len(list1)
    return list1[0]
print("Last man standing is:", Jusephus(9,7))
        
