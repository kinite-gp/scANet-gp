import requests
from library import module


def registred(domain):
    response = requests.get(domain)
    response = response.status_code
    try:
        if response == 200:
            module.log('domin is found')
            return True
        elif response == 404:
            module.log('domin is not found')
            return False
        else:
            print(response)
    except requests.exceptions.ConnectionError:
        module.log('not Connect')
        return False
    except requests.exceptions.MissingSchema:
        module.log('"http://" not found')
        return False
