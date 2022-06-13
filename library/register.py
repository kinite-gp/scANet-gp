import requests
from library import log


def registred(domain):
    response = requests.get(domain)
    response = response.status_code
    try:
        if response == 200:
            log.log('domin is found')
            return True
        elif response == 404:
            log.log('domin is not found')
            return False
        else:
            print(response)
    except requests.exceptions.ConnectionError:
        log.log('not Connect')
        return False
    except requests.exceptions.MissingSchema:
        log.log('"http://" not found')
        return False
