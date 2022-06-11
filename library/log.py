from datetime import datetime

def timelog():
    var = datetime.now()

    timedate = var.strftime("%d/%m/%Y %H:%M:%S")
    return timedate

def log(log):
    var = datetime.now()
    timedate = var.strftime("%d/%m/%Y %H:%M:%S")
    logs = timedate +' >> '+log
    
    return logs