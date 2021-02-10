import requests

def push(archive_name):
    files = {'file': open(archive_name, 'rb')}

    try:
        upload = requests.post("https://api.bayfiles.com/upload", files=files)
        print(upload.content)
    except:
        print("File failed to Upload.")

    return 0
