# FlavorLab

FlavorLab is a Django web application for exploring ingredients, flavour notes, flavour pairings and cooking experiments. It works like a personal flavour notebook: you describe ingredients, link them to flavour notes, record which ingredients go well together, and log the results of your own cooking experiments.

Built as the individual project for the **Django Basics** course at SoftUni.

---

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Pages and URLs](#pages-and-urls)
- [Validation](#validation)
- [Getting Started](#getting-started)
- [Database Setup](#database-setup)
- [Configuration](#configuration)
- [Using the Application](#using-the-application)
- [Custom 404 Page](#custom-404-page)

---

## Features

- **Ingredients** – full CRUD (create, read, update, delete) with a category, a 1–5 flavour intensity and any number of flavour notes.
- **Search, filter and sort** – search ingredients by name, filter by category or flavour note, and sort by name or intensity.
- **Flavour notes** – create and delete notes (for example *citrus*, *smoky*, *sweet*) and see how many ingredients use each one.
- **Pairings** – full CRUD for ingredient combinations, each with an explanation of why the two ingredients work together.
- **Experiments** – full CRUD for cooking experiments, linking the ingredients used with observations and a result.
- **Delete confirmation** – every delete asks for confirmation first. Deleting an ingredient warns you how many pairings will be removed with it.
- **Feedback messages** – success messages after creating, editing and deleting ingredients, pairings and experiments.
- **Custom template filter** – `intensity_label` turns the numeric intensity (1–5) into a readable label such as "Very mild" or "Strong".
- **Reusable templates** – a base template, partials for the navbar, footer, messages, form fields, ingredient cards and the filter bar.
- **Custom 404 page.**

## Technologies

- Python 3
- Django 6.1
- PostgreSQL (configured through environment variables), with an automatic SQLite fallback when no database is configured
- `psycopg2-binary` – PostgreSQL driver
- `python-dotenv` – loads settings from a `.env` file
- HTML and CSS (custom stylesheet)

## Project Structure

```
FlavourLab/
├── config/                 # Project settings, root URLs, WSGI/ASGI
├── ingredients/            # Ingredients and flavour notes
│   ├── templates/ingredients/
│   │   └── partials/       # card.html, filter_bar.html
│   └── templatetags/       # flavour_extras.py (custom filter)
├── pairings/               # Ingredient pairings
├── experiments/            # Cooking experiments
├── templates/              # base.html, 404.html
│   └── partials/           # navbar, footer, messages, form_fields
├── static/css/style.css
├── manage.py
├── requirements.txt
└── .env.example
```

**Main Django apps**

| App | Responsibility |
|---|---|
| `ingredients` | Ingredients, flavour notes, searching, filtering and sorting |
| `pairings` | Combinations of two ingredients and why they work together |
| `experiments` | Cooking experiments, observations and results |

## Data Model

| Model | App | Fields |
|---|---|---|
| `FlavourNote` | ingredients | `name` (unique) |
| `Ingredient` | ingredients | `name` (unique), `description`, `category`, `intensity` (1–5), `flavour_notes` (many-to-many with `FlavourNote`) |
| `Pairing` | pairings | `first_ingredient` and `second_ingredient` (foreign keys to `Ingredient`), `explanation` |
| `Experiment` | experiments | `title`, `ingredients` (many-to-many with `Ingredient`), `observations`, `result`, `created_at` |

**Relationships**

- Many-to-many: `Ingredient` ↔ `FlavourNote`, and `Experiment` ↔ `Ingredient`.
- Many-to-one: each `Pairing` points to two `Ingredient` records.

## Pages and URLs

Every page is reachable through the navigation bar or links on the pages themselves.

| URL | Page |
|---|---|
| `/` | Redirects to the ingredient list |
| `/ingredients/` | All ingredients, with search, filtering and sorting |
| `/ingredients/add/` | Add an ingredient |
| `/ingredients/<id>/` | Ingredient details |
| `/ingredients/<id>/edit/` | Edit an ingredient |
| `/ingredients/<id>/delete/` | Delete confirmation |
| `/ingredients/notes/` | All flavour notes |
| `/ingredients/notes/add/` | Add a flavour note |
| `/ingredients/notes/<id>/delete/` | Delete a flavour note (confirmation) |
| `/pairings/` | All pairings |
| `/pairings/add/` | Add a pairing |
| `/pairings/<id>/` | Pairing details |
| `/pairings/<id>/edit/` | Edit a pairing |
| `/pairings/<id>/delete/` | Delete confirmation |
| `/experiments/` | All experiments |
| `/experiments/add/` | Add an experiment |
| `/experiments/<id>/` | Experiment details |
| `/experiments/<id>/edit/` | Edit an experiment |
| `/experiments/<id>/delete/` | Delete confirmation |

## Validation

- **Ingredients:** the name must be unique and at most 80 characters; intensity must be a whole number from 1 to 5; the description is required.
- **Pairings:** an ingredient cannot be paired with itself, and the same two ingredients cannot be paired twice (in either order).
- **Experiments:** at least one ingredient, plus observations and a result, are required.
- **Flavour notes:** names must be unique.
- All forms show custom, user-friendly error messages, labels, help texts and placeholders.
- When editing an experiment, the *Created at* field is shown as read-only (disabled).

## Getting Started

### Requirements

- Python 3.12 or newer (check the Django release notes for the exact minimum for your Django version)
- `pip`
- PostgreSQL *(optional – without it, the project uses SQLite automatically)*

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mihaelabozeva/FlavourLab.git
   cd FlavourLab
   ```

2. Create and activate a virtual environment:

   ```bash
   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows (PowerShell)
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Choose a database (see [Database Setup](#database-setup)):
   - **Quickest:** do nothing. Without a `.env` file, the project uses SQLite.
   - **PostgreSQL:** create a database, copy `.env.example` to `.env` and fill in the `DB_*` values.

5. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open <http://127.0.0.1:8000/> in your browser.

No fixtures or prepopulated data are needed. The application works with an empty database, and everything can be created through the website.

## Database Setup

FlavorLab picks its database from the environment variables:

- **`DB_NAME` is set** → PostgreSQL, using the `DB_*` variables.
- **`DB_NAME` is empty or missing** → SQLite (`db.sqlite3` is created in the project folder).

### Using PostgreSQL

1. Make sure PostgreSQL is installed and running.
2. Create an empty database, for example:

   ```sql
   CREATE DATABASE flavorlab;
   ```

3. Copy `.env.example` to `.env` and fill in your connection details:

   ```
   DB_NAME=flavorlab
   DB_USER=your_postgres_user
   DB_PASS=your_postgres_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. Run `python manage.py migrate`.

### Using SQLite

Leave the `DB_*` variables out (or empty). Nothing else is required.

## Configuration

Settings are read from environment variables, which can be placed in a `.env` file in the project root (next to `manage.py`). Every variable has a default, so the project also runs without a `.env` file.

| Variable | Default | Purpose |
|---|---|---|
| `SECRET_KEY` | built-in development key | Django secret key. Set your own for anything beyond local testing. |
| `DEBUG` | `True` | Set to `False` to disable debug mode (see [Custom 404 Page](#custom-404-page)). |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated list of allowed hosts. |
| `DB_NAME` | *(empty)* | PostgreSQL database name. If empty, SQLite is used instead. |
| `DB_USER` | *(empty)* | PostgreSQL user. |
| `DB_PASS` | *(empty)* | PostgreSQL password. |
| `DB_HOST` | `localhost` | PostgreSQL host. |
| `DB_PORT` | `5432` | PostgreSQL port. |

Never commit your `.env` file or real credentials to version control.

## Using the Application

A good order for trying everything out on an empty database:

1. **Add flavour notes** – open *Flavour notes* in the navigation bar and add a few (for example *citrus*, *earthy*, *sweet*).
2. **Add ingredients** – open *Ingredients*, click **+ Add ingredient**, and choose a category, an intensity and some flavour notes.
3. **Search and filter** – on the ingredients page, search by name, filter by category or flavour note, and change the sort order.
4. **Add a pairing** – open *Pairings* and combine two different ingredients with an explanation.
5. **Record an experiment** – open *Experiments*, pick the ingredients you used and write your observations and result.
6. **Edit and delete** – every item can be edited, and deleting asks for confirmation first.

## Custom 404 Page

With `DEBUG=True` (the default), Django shows its own detailed error page for missing URLs. To see the custom 404 page:

1. Set `DEBUG=False` in your `.env` file.
2. Start the server with static files enabled:

   ```bash
   python manage.py runserver --insecure
   ```

3. Visit any address that does not exist, for example <http://127.0.0.1:8000/nothing-here/>.