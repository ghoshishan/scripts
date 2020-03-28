# Automate Repository Creation using GitHub API

### Requirements
1. PyGithub
```bash
sudo pip install PyGithub #enter password when prompted
```
2. Visual Studio Code

### Installation
```bash
git clone "https://github.com/Ishan1742/project_initializer.git"
cd project_initializer
```
Open create.py and set your username and password for GitHub account and also set your correct path in the same file.
Open commands.sh and set your correct remote for GitHub

Then
```bash
cp commands.sh ~/.commands.sh
```

### Running

If a new terminal is opened then type
```bash
source ~/.commands.sh
```
Then to create your project run
```bash
create [project name]
```