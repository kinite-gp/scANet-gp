import json

def get_date_json():
    file = open('library\\setup.json','r')
    date = file.read()
    dict = json.loads(date)

    return dict
