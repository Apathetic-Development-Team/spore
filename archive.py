from random import choice
from os import mkdir
from upload import is_gui, push
from shutil import copy, rmtree
import py7zr

PASSWORD = "raidforums"
words = ["milk", "eggs", "sausage", "bacon", "hotdog", "muffin", "banana", "apple", "noodles"]

included_file = "\n\n".join([
    "# AUTHORS",
    "https://github.com/Apathetic-Development-Team/spore",
    "CYBERLUST: https://github.com/CYBERLUST",
    "Forsol: https://github.com/Forsol",
    "whtrbbt: https://github.com/wwhtrbbtt",
    "# SHOUTOUT" ,
    "Huge shoutout to https://raidforums.com, especially the owner, OmniPotent."
])

def create_folder(user_input):
    print("Copying all files in a temp folder...")

    # make an empty folder called temp_folder
    rmtree('temp_folder', ignore_errors=True)
    mkdir("temp_folder")

    with open("temp_folder/info.md", "w") as f:
        f.write(included_file)

    # if the user wants multiple files, iterate over them
    if type(user_input) is tuple:
        is_gui(True)
        for file in user_input:
            copy(file, "temp_folder/" + file.split("/")[-1])

    # if they want only 1 file
    else:
        is_gui(False)
        copy(user_input, "temp_folder/" + user_input.split("/")[-1])

    print("Done!")
    
def process(user_input):
    create_folder(user_input)

    # generate the archive name
    archive_name  = "".join([choice(words) for _ in range(2)]) + ".7z"

    # create a 7z archive with the specified password
    with py7zr.SevenZipFile(archive_name, 'w', password=PASSWORD) as archive:
        archive.writeall('temp_folder', '/')
    
    print(archive_name + " generated sucessfully. Uploading now... ")
    # upload and delete it.
    push(archive_name)
    rmtree('temp_folder', ignore_errors=True)
