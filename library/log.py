from datetime import datetime

def timelog():
    var = datetime.now()

    timedate = var.strftime("%d/%m/%Y %H:%M:%S")
    return timedate

def log(log):
    var = datetime.now()
    timedate = var.strftime("%Y/%m/%d %H:%M:%S")
    logs = timedate +' >> '+log
    file = open('logs\\logs.txt','a')
    file.write(f'{logs}\n')
    file.close()
    
