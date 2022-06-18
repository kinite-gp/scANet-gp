import socket
from datetime import datetime
from library import module

def scanner(target):
    remotserverip = socket.gethostbyname(target)

    print(f'Server IP {remotserverip}')
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

scanner('google.com')