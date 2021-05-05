# course-catalog

course-catalog is a basic Django project.

## Table of contents

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)

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
3. Create a database with all the needed tables and start a server
```bash
python3 manage.py migrate
python3 manage.py runserver
```

## Usage

1. Create a course

`POST /courses/`

A course has 4 attributes: 
- name (256 characters or less)
- start_date (YYYY-MM-DD format)
- end_date (YYYY-MM-DD format)
- num_lections (non-negative integer)


2. Get a list of all courses

`GET /courses/`

3. Filter courses by start_date or end_date or search by name (constraints can be used together as well as separately)

`GET /courses/?start_date=2020-12-25&end_date=2021-12-27&search=Math/`

4. Get a course by its id (integer)

`GET /courses/1/`

5. Filter a specific course by start_date or end_date or search by name (constraints can be used together as well as separately)

`GET /courses/1/?search=Gym&start_date=2020-12-25&end_date=2021-12-27/`

6. Update a course

`PUT /courses/1/`

7. Update a course partially

`PATCH /courses/1/`

8. Delete a course

`DELETE /courses/1/`
