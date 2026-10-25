# FlavorLab

## Overview

FlavorLab is a Django web application for exploring ingredients, flavour notes, flavour pairings, and cooking experiments. It helps users organise flavour information, discover ingredient combinations, and record the results of cooking experiments.

## Features

- Browse, search, filter, and sort ingredients.
- View ingredient details, including flavour notes and intensity.
- Create, edit, and delete ingredients.
- Create and manage flavour notes.
- Create flavour pairings and explain why ingredients complement each other.
- Record cooking experiments, including ingredients, observations, and results.
- Manage ingredients, pairings, and experiments through web forms.
- View readable ingredient intensity labels and a custom 404 page.

## Technologies

- Python
- Django
- HTML and CSS
- Database configured in Django settings (PostgreSQL)

### Database configuration

FlavorLab uses PostgreSQL. Before running the project, ensure PostgreSQL is installed and running, and configure the database connection using the environment variables expected by `config/settings.py`.

Do not commit database passwords or other secrets to GitHub.

After configuring the database, apply migrations:

`python manage.py migrate`

## Main Django apps

- **ingredients** — ingredients, flavour notes, and ingredient filtering.
- **pairings** — ingredient combinations and explanations.
- **experiments** — cooking experiments, observations, and results.

## Setup

1. Clone the repository:

   `git clone https://github.com/mihaelabozeva/FlavourLab.git`

2. Navigate into the project directory:

   `cd FlavourLab`

3. Create and activate a Python virtual environment.

4. Install the dependencies:

   `pip install -r requirements.txt`

5. Configure the environment variables required by your local settings. Do not commit secret values to version control.

6. Apply database migrations:

   `python manage.py migrate`

7. Start the development server:

   `python manage.py runserver`

8. Open `http://127.0.0.1:8000/` in your browser.

## Project status

FlavorLab was developed as a Django learning project, with a focus on managing related data, implementing CRUD operations, validating forms, and using reusable templates.
