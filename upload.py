import json
import requests
from requests_toolbelt.multipart import encoder
import gui

gui_state = True


def is_gui(status):
    global  gui_state

    if status:
        gui_state = True
    elif not status:
        gui_state = False




def bayfiles_upload(files):
    try:
        session = requests.Session()
        with open(files, 'rb') as f:
            form = encoder.MultipartEncoder({
                "file": (files, f, "application/octet-stream"),
            })
            headers = {"Prefer": "respond-async", "Content-Type": form.content_type}
            r = session.post("https://api.bayfiles.com/upload", headers=headers, data=form)
        session.close()
        resp = json.loads(r.content)
        if r.status_code == 200:
            print('BayFiles Uploaded: ' + resp['data']['file']['url']['short'])
            if gui_state:
                gui.update_links('BayFiles: ' + resp['data']['file']['url']['short'])

        else:
            print('Something else happened')
    except Exception as e:
        print(e)


def anonfiles_upload(files):
    try:
        session = requests.Session()
        with open(files, 'rb') as f:
            form = encoder.MultipartEncoder({
                "file": (files, f, "application/octet-stream"),
            })
            headers = {"Prefer": "respond-async", "Content-Type": form.content_type}
            r = session.post("https://api.anonfiles.com/upload", headers=headers, data=form)
        session.close()
        resp = json.loads(r.content)
        if r.status_code == 200:
            print('AnonFiles Uploaded: ' + resp['data']['file']['url']['short'])
            if gui_state:
                gui.update_links('AnonFiles: ' + resp['data']['file']['url']['short'])
        else:
            print('Something else happened')
    except Exception as e:
        print('AnonFiles did not upload')


def gofile_upload(files):
    try:
        session = requests.Session()
        with open(files, 'rb') as f:
            form = encoder.MultipartEncoder({
                "file": (files, f, "application/octet-stream"),
            })
            headers = {"Prefer": "respond-async", "Content-Type": form.content_type}
            r = session.post("https://srv-store1.gofile.io/uploadfile", headers=headers, data=form)
        session.close()
        resp = json.loads(r.content)
        if r.status_code == 200:
            print('GoFile Uploaded: ' + 'https://gofile.io/d/' + resp['data']['code'])
            if gui_state:
                gui.update_links('GoFile: ' + 'https://gofile.io/d/' + resp['data']['code'])
        else:
            print('Something else happened')
    except Exception as e:
        print(e)


def push(archive_name):
    try:
        with open(archive_name, 'rb') as archive:
            files = archive.name
            if gui_state:
                gui.clear()
            bayfiles_upload(files)
            anonfiles_upload(files)
            gofile_upload(files)
            if gui_state:
                gui.InfoBox("All Files Uploaded.")

    except Exception as e:
        print("Failed to Upload (all?) files")
        print(e)

    return 0
