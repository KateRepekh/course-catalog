# course-catalog

course-catalog is a basic Django project.

## Prerequisites

This project is guaranteed to run on [Python](https://realpython.com/installing-python/) 3.7.1 or later.

It is assumed that you have [git](https://github.com/git-guides/install-git) and [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) installed on your machine.

## Installation
1. Clone the repository
```bash
git clone https://github.com/KateRepekh/course-catalog.git
cd course-catalog
```
2. Create a virtual environment and install required Python libraries
```bash
virtualenv env
# If the following command doesn't work on your OS, 
# see https://virtualenv.pypa.io/en/latest/user_guide.html#activators 
source env/bin/activate
pip install -r requirements.txt
```
3. Create a database with all needed tables and start a server
```bash
python3 manage.py migrate
python3 manage.py runserver
```

