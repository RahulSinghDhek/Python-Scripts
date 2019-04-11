import time
import threading
start_time= time.time()
def passtime(rang):
    for i in range(rang):
        pass
passtime(1000000000)
#thread_list=[]
#for i in range(100):
#    thr=threading.Thread(target=passtime,args=(10000000,))
#    thread_list.append(thr)
#    thr.start()
#for old_thread in thread_list:
#    old_thread.join()
        
end_time= time.time()
print ("Time taken py program : {}".format(end_time-start_time))