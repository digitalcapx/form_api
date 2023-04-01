# API to persist a simple form to Landing Page

## Technologies used
 - Python 3.x
 - FastAPI
 - Peewee ORM
 
 ## Endpoints
 
 Endpoint   | Method | Request Body | Description
:---------: | :------: | :-----: | :-----
/form | POST | *name_surname*: str, *email*: str, *phone*: str | Create form
/docs | GET | - | Swagger Documentation

## Steps to use
1. Create a virtual environment using `python -m venv env` in the project root directory.
2. Activate the environment:
   2.1. Non-Linux: `source env/bin/activate`
   2.2. Without Windows: `env/Scripts/Activate`
3. Install dependencies: `pip install -r requirements.txt`.
4. Run: `uvicorn --app-dir src/ main:app --reload`
