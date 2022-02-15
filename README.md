# Capstone Know-Your-Neighborhood:
 ## Back-end layer

## `Introduction`
This back-end layer is producing API to be used by the know-your-neiborhood web app. There are two type of API: public and protected API.

## `Built With`

This projet is built with:
1. Flask python library
2. Postgres SQL DataBase
3. Auth0
4. GitHub version control
5. Heroku host server
   
## `Structure of the project`

### `app/__init__.py`

This file configures the app.
- import all the libraries
- Set the DataBase connection string
- Import the model (Business) 
- Register the blueprint (business_bp)

### `app/models`

This project has one mode: `Business`
- Under the directory : `app/models/business.py`

#### `app/routes.py`

Here all the enpoins are defined.
- import the model `Business`
- import all the libraries
- import `Blueprint`, `request` and `db`
- import `helperfunctions.py` and `functions from auth,py`
  
### `.env`

This file containes the environmental virables:
- `URL for the postgress SQL DataBase`
- `AUTH0_DOMAIN`
- `API_AUD` 


### `requirements.txt`

This file containe all dependencies which are needed to run the project.

### `Procfile`

This file  has the contents needed for a Heroku deployment.


## `Installations`

To run the code on your local matchin:
1. Clone or Fork the repo 
   git clone https://github.com/tirhas20/back-end-know-your-neighborhood
2. Change directory to `back-end-know-your-neighborhood`
   - cd back-end-know-your-neighborhood
3. Create a virtual environment
    - python3 -m venv venv
4. Activate the virtual environment by running the following code: 
    - source venv/bin/activate
5. Under the activated environment install the dependecies by running the code:
   - pip install -r requirements.txt
6. To save the installed dependency in to the requirement run the code:
    - pip3 freeze > requirement.txt
7. When you finish working deactivate the virtual environment by ruuning:
    - deactivate
8. When you need to test the endpoints on Postman run the code:
   - flask run



