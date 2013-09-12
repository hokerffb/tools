import string, threading, time
import os
 

def thread_main(index):
    global count, mutex
    threadname = ""
    threadname += str(threading.currentThread().__hash__())
    cmd = "sh debug_httpd.sh " + str(index) + " > logs/" + threadname
    print cmd
    os.system(cmd)
    return
 
    for x in xrange(0, int(index)):
        mutex.acquire()
        count = count + 1
        mutex.release()
        print threadname, x, count
        time.sleep(1)


def main(num):
    global count, mutex
    threads = []
 
    count = 1
    mutex = threading.Lock()

    for x in xrange(1, num + 1):
        threads.append(threading.Thread(target=thread_main, args=(x,)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()  
 
 
if __name__ == '__main__':
    num = 20
    main(num)

