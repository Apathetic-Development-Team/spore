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

#fetches animal list from GitHub, puts two animals together
def get_wordlist():
    fetch_words = requests.get("https://gist.githubusercontent.com/mbauer14/eaaa001b7fb8073dd576/raw/84501d87e7ac3a134700862a6b22916c9cb16773/animals.txt")
    return fetch_words.text.splitlines()

# takes the animals, puts them in an array and chooses one at random.
def create_name():
    word = ([c.strip() for c in get_wordlist()])
    return  random.choice(word) + random.choice(word) + ".zip"
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

