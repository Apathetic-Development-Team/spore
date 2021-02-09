import requests
import zipfile
import random

def create_name():
    prefix = ["Fat", "tight"]
    suffix = ["Cock", "Pussy"]
    return  random.choice(prefix) + random.choice(suffix) + ".zip"
archive_name = create_name()


def create_archive():
    archive = zipfile.ZipFile(archive_name, 'w')
    archive.write('pp')
    archive.close()

# was going to make a Main Function but indentation gives me motion sickness
create_archive()
files = {'file': open(archive_name, 'rb')}

try:
    upload = requests.post("https://api.bayfiles.com/upload", files=files)
    print(upload.content)

except:
    print("File failed to Upload.")

