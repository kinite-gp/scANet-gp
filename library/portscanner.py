import socket
import time
import threading
from queue import Queue
from library import log,files


def scaner(target):
    socket.setdefaulttimeout(0.25)
    lock = threading.Lock()
    iptarget = socket.gethostbyname(target)
    log.log(f'start scan an host {iptarget}')

    def portscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((iptarget))
            with lock:
                files.autosave(target,port + 'is poen')
                files.writeout(port + "is open")
                con.close()
        except:
            log.log('error portScanner.scaner.portscan')
    
    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()

    q = Queue()
    starttime = time.time()
    
    for a in range(100):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()
    
    for worker in range(1,500):
        q.put(worker)

    q.join()
    log.log(f'token time portScanner {time.time() - starttime}')
    files.autosave(target,'\n---------------------------------------')
    files.writeout('\n---------------------------------------')
    files.autosave(target,f'ip domin : {iptarget}\n---------------------------------------')
    files.writeout(f'ip domin : {iptarget}\n---------------------------------------')