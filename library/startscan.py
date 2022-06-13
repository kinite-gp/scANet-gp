from xml import dom
from library import getwhois,portscanner,register,tinput,log,sound

def scanrun():
    domin = tinput.tinput('Start scANet','whats is domin : ')
    reg = register.registred(domin)
    if reg == True:
        sound.start()
        log.log('start scanet procces')
        getwhois.getwhois(domin)
        portscanner.scaner(domin)

    else:
        sound.error()
        log.log('scanet error')

    sound.finish()
    log.log('finish scanet')