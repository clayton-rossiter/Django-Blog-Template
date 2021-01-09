# Django Blog Template    
This template has been created as an extremely stripped down version of starting a blog Django template.  No bells, no whistles, just the stripped down version of a new Django project with a Blog app (containing the blog components), and an Index app (containing common components, such as navbar, footer and index.html)

## Table of Contents

## General


## How to Use
## Just to Get It Working
If you just want to get this thing working, follow the steps below:   
- Setup your virtual environment
    - depending on your operating system, make a virtual environment (virtualenv, pipenv, pyenv)
    - activate this virtual environment:
        - Mac OS: source /path/to/virtualenv/bin/activate
        - Windows: /path/to/virtualenv/Scripts/activate
    - install requirements by running `pip install -r requirements.txt` in the terminal
- Add a .env file in the 'project' directory and, in this file, insert:
    - SECRET_KEY = <random 50 character secret key>
    - DEBUG = True
- run `python manage.py migrate`    
- run `python manage.py runserver`

The views in this project use Class-based views for ease of deploying multiple pages and making use of the awesome get_context_data and get_queryset functions inherited from the ListView and DetailView classes.


## How to Adapt
### Django Components
#### Adding New Blog Models

#### Customise Existing Models

### Styling
This project has been built in CSS; no libraries like bootstrap or anything (though I wish I had)

## Deployment
I hate deploying this stuff... so please bear with me as I fudge my way through a step-by-step method of hosting on the services below.
### Heroku

