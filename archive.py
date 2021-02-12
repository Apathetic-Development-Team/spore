import random
import zipfile
import upload

words = ["milk", "eggs", "sausage", "bacon", "hotdog"]


def process(user_input):
    archive_name = random.choice(words) + random.choice(words) + ".zip"
    archive = zipfile.ZipFile(archive_name, 'w')
    if type(user_input) is tuple:
        upload.is_gui(True)
        for i in user_input:
            print(i)
            archive.write(i, i.rsplit('/', 1)[-1])
    else:
        upload.is_gui(False)
        archive.write(user_input, user_input.rsplit('/', 1)[-1])
    archive.close()

    print(archive_name + " generated sucessfully. Uploading now... ")
    upload.push(archive_name)
