import asyncio
import time
import threading

def thread_func(id):
    time.sleep(id)
    print("thread : {}, has successfully completed after {} seconds".format(id,id))

def normal_func(id):
    time.sleep(id)
    print("Coroutine: {}, has successfully completed after {} seconds".format(id,id))

async def asynchronous_func(id):
    await asyncio.sleep(id)
    print("Coroutine: {}, has successfully completed after {} seconds".format(id,id))

@asyncio.coroutine
def asynchronous_coroutine_func(id):
    yield from asyncio.sleep(id)
    print("Coroutine: {}, has successfully completed after {} seconds".format(id,id))
   
start_time= time.time()


#----------threading----------

thread_list=[]
for i in range(6):
    new_thread= threading.Thread(target=thread_func, args=(i,))
    thread_list.append(new_thread)
    new_thread.start()
 
for old_thread in thread_list:
    old_thread.join()
    

#-----------------Calling async with await()-------------------
#loop = asyncio.get_event_loop()
#tasks = []
#for i in range(6):
#    tasks.append(asyncio.ensure_future(asynchronous_func(i)))
#loop.run_until_complete(asyncio.wait(tasks))
#loop.close()    

#-----------------Calling async with yield-------------------
#tasks=[]
#for i in range(6):
#    tasks.append(asynchronous_coroutine_func(i))
#asyncio.run(asyncio.wait(tasks))

#-----------------Calling normal function-------------------
#for i in range(6):
#    normal_func(i)


end_time= time.time()

print ("Time taken py program : {}".format(end_time-start_time))
    