import sys
import os
from github import Github

path = "/home/ishan/Projects/" #Change path to your path /home/[user_name]/

username = "" #Enter your username here
password = "" #Enter your password here

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path+str(sys.argv[1]))
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Successfully created repository", folderName)

if __name__ == "__main__":
    create()