import random
import zipfile
import upload
import os

words = ["milk", "eggs", "sausage", "bacon", "hotdog"]

def process(user_input):
    archive_name = random.choice(words) + random.choice(words) + ".zip"
    if os.path.isdir(user_input) == True:
        pass
    else:
        archive = zipfile.ZipFile(archive_name, 'w')
        archive.write(user_input)
        archive.close()

    print(archive_name + " generated sucessfully. Uploading now... ")
    upload.push(archive_name)



