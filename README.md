TaskManager -  built with Django, Postgres, jQuery.

    TaskManager is a Django web application for managing tasks. It allows you to create, read, update, and delete tasks, change their status, filter tasks by status, and search by task title. Additionally, it includes user registration, login, and authentication functionalities.

Features
    1. Create, Read, Update, and Delete tasks.
    2. Task status management
    3. Task filtering by status
    4. Task search by title
    5. User registration, login, and authentication

NOTE: Try to use python version >= 9

Setup:
    1. Clone the repository:
        git clone https://github.com/jeevangupta/Task-Manager.git
        cd Task-Manager

    2. Create a virtual environment:

        python3 -m venv env
        source ./env/bin/activate

    3. Install dependencies:

        pip install -r requirements.txt

    4. Install Postgres and create the database
        1. Install Postgres and pgAdmin4 .
        2. Create a database named "TaskManager".

    5. Run database migrations:
        cd TaskProject
        python manage.py migrate

    6. Start the development server:

        python manage.py runserver

    The Django server will start running at http://localhost:8000.

Usage:
    1. Navigate to http://localhost:8000 in your web browser.
    2. You will see a page with links to Login, Register, and My Tasks (the main dashboard).
    3. If you are a new user, register first to access the "My Tasks" page.
    4. Once registered and logged in, you will see the "My Tasks" page.
    5. Use the "Create Task" button to create a new task.
    6. Use the "Delete" button to delete a task.
    7. Use the "Change Status" dropdown and "Update" button to update a task's status.
    8. Use the "Filter By" option to filter tasks by status.
    9. Use the "Search by Title" option to search for specific tasks.







