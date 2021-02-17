import json
from requests import Session
from requests_toolbelt.multipart import encoder
import gui
from threading import Thread

gui_state = True
progress_state = []


def is_gui(status):
    global gui_state
    gui_state = status


def bayfiles_upload(files):
    """
    Uploads to bayfiles.io
    """
    try:
        global progress_state
        session = Session()
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
            progress_state.append(1)
            if gui_state:
                gui.update_links('BayFiles: ' + resp['data']['file']['url']['short'])

        else:
            print('Something else happened')
    except Exception as e:
        print('BayFiles did not upload')


def anonfiles_upload(files):
    """
    Uploads to anonfiles.io
    """
    try:
        global progress_state
        session = Session()
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
            progress_state.append(1)
            if gui_state:
                gui.update_links('AnonFiles: ' + resp['data']['file']['url']['short'])
        else:
            print('Something else happened')
    except Exception as e:
        print('AnonFiles did not upload')


def gofile_upload(files):
    """
    Uploads to gofile.io
    """
    try:
        global progress_state
        session = Session()
        with open(files, 'rb') as f:
            form = encoder.MultipartEncoder({
                "file": (files, f, "application/octet-stream"),
            })
            headers = {"Prefer": "respond-async", "Content-Type": form.content_type}
            r = session.post("https://srv-store1.gofile.io/uploadfile", headers=headers, data=form)
        session.close()
        resp = json.loads(r.content)
        if r.status_code == 200:
            gofile_url = f'https://gofile.io/d/{resp["data"]["code"]}'
            print(f'GoFile Uploaded: {gofile_url}')
            progress_state.append(1)
            if gui_state:
                gui.update_links(f'GoFile: {gofile_url}')
        else:
            print('Something else happened')
    except Exception as e:
        print('GoFile did not upload')


def push(archive_name):
    """
    upload the file to every supported platform
    """
    try:
        with open(archive_name, 'rb') as archive:
            files = archive.name
            if gui_state:
                gui.clear()
            # start the threads
            Thread(target=bayfiles_upload, args=[files]).start()
            Thread(target=anonfiles_upload, args=[files]).start()
            Thread(target=gofile_upload, args=[files]).start()
            # if gui_state:
            #     gui.infobox("All Files Uploaded.")

    except Exception as e:
        print("Failed to Upload (all?) files")
        print(e)

    return 0
