# Instawork Coding Challenge F'22

Simple [Django](https://github.com/django/django) project to simulate a team-member management application that allows the user to view, edit, add, and delete team members.

## Live demo


## Setting Up Locally
(tested on Python 3.8.10 and Django 4.0.6)
1. Fork/Clone this repo  

2. Go to the root project directory

3. Create/Activate virtual env
```bash
$ python3 -m venv env                 # create new virtual environment

# or to activate created environment
$ source env/bin/activate             # Linux/MacOs             
# or
$ .\env\Scripts\activate              # Windows
```

4. Install dependencies
```bash
(env)$ pip install -r requirements.txt
```

5. Start local server
```bash
(env)$ python team_management/manage.py runserver 
```
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.


## Testing
Unit tests using Python standard library module: [unittest](https://docs.python.org/3/library/unittest.html#module-unittest)

## Functionality
* List page shows a list of all team members, number of team members, add member button, whether member is admin and link to the edit page
* Add page for team members
* Edit page for team members including delete function
