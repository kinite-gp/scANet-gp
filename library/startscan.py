from library import getwhois,register,module

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