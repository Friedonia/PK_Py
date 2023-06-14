# made by Frieder Schmidt last chnage 9.06.2023

from flask import Flask
import random
import time
app = Flask(__name__)

def randNum():
    return random.randrange(360)

def randNum14():
    a = random.randrange(14)
    if 0 != a % 2:
        return randNum14()
    return a


@app.route('/')
def index():
    return 'Hello'

@app.route('/deg')
def get_deg():
    return {"deg": randNum()}, 200, {"Access-Control-Allow-Origin": "*"}

@app.route('/table')
def get_table():
    return {"tab":open('ultraschallsensor.txt','r').read()}, 200,  {"Access-Control-Allow-Origin": "*"}

@app.route('/table2')
def get_table2():
    return {"tab":open('ultraschallsensor.txt','r').read()}, 200,  {"Access-Control-Allow-Origin": "*"}
    
@app.route('/blende')
def get_blende():
    return {"see": randNum14()}, 200,  {"Access-Control-Allow-Origin": "*"}
    

#Zum jedesmal zum starten:
#      source /Users/Schule/Desktop/PK_Py/.venv/bin/activate (.venv aktiviern)
#      export FLASK_APP=application.py
#      export FLASK_ENV=development
#      flask run


# cd /Direcktory/zu/gehen
# pwd (sicher stellen das man in diesem ist)
# python3 -m venv .venv (Erstellt den verstckten .venv[sichtbar mit shift + cmd + .])
# source .venv/bin/activate (.venv aktiviern)
# pip3 install flask (in .venv ordner flask instalierne)
# pip3 install flask-sqlalchemy (in .venv ordner flask-sqlalchemy instalierne)
# pip3 freeze > requirments.txt (erstellt durch instalieren datei)
# touch appication.py (erstellt Python datei für api zum programieren)
# control + c (um das Program zu beenden)
