import os
#specify the directory you wanat to list
directory_path = '/second sem'
# list all file and diectrectory in specified path
content = os.listdir(directory_path)
# print each file and directory name
for item in content:
    print(item)
