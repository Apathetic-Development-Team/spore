# Spore :microbe:

In biology, a spore is a unit of sexual or asexual reproduction that may be adapted for dispersal and for survival, often for extended periods of time, in unfavourable conditions. Although with less sex, Spore is python program that seeks to provide a similar solution for resilient file uploads. The program will take your desired file(s), compress them into a single 7zip archive, rename the archive to something boring, and upload them to multiple hosts. The goal of Spore is to make it more difficult for third parties to remove your uploaded files, or even detect them in the first place as anything but a silly archive. **The 7z password is raidforums**

At present three file hosts are supported: GoFile, Anonfiles, Bayfiles. 

# Getting Started

Install the requirements.txt file, and start uploading.

`pip install -r requirements.txt`

tkinter is a required library which should come bundled with your Python version. Some Ubuntu distro's do not have it, please run the command below:

`apt-get install python3-tk`

# Usage

> :warning: **Large files will take much longer to upload.**

Windows, OSX, Linux:

`python3 main.py`

You should be greeted with the below:

![spore](images/main.png)

Once you select your files and finish the upload, you can find the links in the text box:

![uploaded](images/main-downloaded.png)

