🚀

# Backend

The PocketRocket backend is written in Python using Flask.

## Starting a local server

1. `cd` into the `api` folder.
2. Set up the python environment:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
3. Start the server:
```
export FLASK_APP=app.py
flask run
```
4. Visit http://127.0.0.1:5000/ (or whatever link is printed in the CLI) in your web browser.

# Frontend

The PocketRocket frontend is written in JavaScript using React.

## Starting a local server

1. `cd` into the `client` folder.
2. Install node packages:
```
npm install
```
3. Start the server:
```
npm start
```
4. Visit http://localhost:8000/ (or whatever link is printed in the CLI) in your web browser.
