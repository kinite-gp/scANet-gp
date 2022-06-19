from library import getwhois,register,module
import socket
from datetime import datetime
from library import module

def whoisrun():
    domin = module.tinput('Start scANet whois','whats is domin : ')
    reg = register.registred(domin)
    if reg == True:
        module.start()
        module.log('start scanet procces')
        getwhois.whoisdomin(domin)
    else:
        module.error()
        module.log('scanet error')
    module.finish()
    module.log('finish scanet')

def portscanner(target):
    remotserverip = socket.gethostbyname(target)

    print(f'Server IP {remotserverip}')
    module.autosave(target,f'server IP is {remotserverip}')
    module.writeout(target,f'server IP is {remotserverip}')
    time = datetime.naw()
    try:
        for port in range(1,1025):
            sock = socket.socket(socket.socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remotserverip, port))
            if result == 0:
                module.autosave(target,f'Port {port}: Open')
                module.writeout(f'Port {port}: Open')
            sock.close()
    except KeyboardInterrupt:
        print('Press Ctrl+C')
    except socket.gaierror:
        print('Domin not be resolved')
    except socket.error:
        print('Not connect to server')

    time = datetime.now() - time

    module.log(f'Scan completed in: {time}')

