import json

import requests


def bayfiles_upload(files):
    try:
        r = requests.post("https://api.bayfiles.com/upload", files=files)
        resp = json.loads(r.content)
        print(resp['data']['file']['url']['short'])
        if r.status_code == 200:
            print('BayFiles Uploaded.')
        else:
            print('Something else happened')
    except Exception as e:
        print('Bayfiles did not upload')


def anonfiles_upload(files):
    try:
        r = requests.post("https://api.anonfiles.com/upload", files=files)
        resp = json.loads(r.content)
        print(resp['data']['file']['url']['short'])
        if r.status_code == 200:
            print('AnonFiles Uploaded.')
        else:
            print('Something else happened')
    except Exception as e:
        print('AnonFiles did not upload')


def gofile_upload(files):
    try:
        r = requests.post("https://srv-store1.gofile.io/uploadfile", files=files)
        resp = json.loads(r.content)
        print('https://gofile.io/d/' + resp['data']['code'])
        if r.status_code == 200:
            print('GoFile Uploaded.')
        else:
            print('Something else happened')
    except Exception as e:
        print('GoFile did not upload')


def push(archive_name):

    try:
        with open(archive_name, 'rb') as archive:
            files = {'file': (archive.name, archive.read())}
            bayfiles_upload(files)
            anonfiles_upload(files)
            gofile_upload(files)
    except:
        print("Failed to Upload (all?) files")

    return 0
