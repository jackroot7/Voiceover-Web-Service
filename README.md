# Voiceover Web Service

Get help to implement a video voiceover web service service 
User Interaction: The user selects a finalized script and inputs their voice preferences, such as the type of voice (gender, age, accent) and the speed of narration.


## Getting Started

These instructions will guide you through setting up the project locally for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- `Python 3.9` or higher
- `Django 4.2` or higher


### Installing

A step-by-step series of examples that tell you how to get a development environment running.

1. **Download the Project**

    Start by downloading the ZIP file of the project and extract it to your desired location.

2. **Set Up a Virtual Environment**

    Navigate to the project directory in your terminal and set up a Python virtual environment by running:

    ```
    python -m venv venv
    ```

    Activate the virtual environment:

    - On Windows:
      ```
      venv\Scripts\activate
      ```
    - On Unix or MacOS:
      ```
      source venv/bin/activate
      ```

3. **Install Required Packages**

    Install all dependencies listed in the `requirements.txt` file using pip:

    ```
    pip install -r requirements.txt
    ```

3. **Static files**

    Dont forget to collect static using:

    ```
    python manage.py collectstatic
    ```


### Running the Project

After installing, you can run the project on your local development server.

1. **Apply Migrations**

    First, apply the migrations to your database:

    ```
    python manage.py migrate
    ```

2. **Start the Development Server**

    Start the Django development server by running:

    ```
    python manage.py runserver
    ```

    You should now be able to access the project admin panel at `http://127.0.0.1:8000/admin/`. `username: admin` and `password: vover12345`.

    Also, you can test to sent request to API using different query paraments. You should now be able to access the `Ninja api doc` at `http://127.0.0.1:8000/api/v1/docs/`.

## Usage

Follow Ninja API documentations
