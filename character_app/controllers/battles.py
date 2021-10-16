from character_app import app
from flask import render_template, redirect, request, session
import random
from flask import flash
# currently is rendered and utilizes session but can not be used by the db.
MAP= {
    "entrance": (5,10),
    "hallway": (7, 14),
    "smallroom": (10,25),
    "thieve's room": (10, 50)
}
@app.route('/battle')
def battle():
    if "battle" and "rounds" not in session:
        session["battle"]= 0
        session["results"]=[]
        session["rounds"]= 0
    return render_template("battle.html")

@app.route('/process_battle',methods=['POST'])
def process_battle():
    building_name= request.form['building']
    building = MAP[building_name]
    building_name_upper = building_name[0].upper() + building_name[1:]
    current_battle = random.randint(building[0], building[1])
    result= 'win'
    message= f'Found {current_battle} gold on the ground near the {building_name}'
    if building_name == "thieve's room":
        if random.randint(0,1) > 0:
            message = f"You're attacked by a thief and lost {current_battle} gold..."
            current_battle = current_battle * -1
            result = 'lose'
    session["battle"] += current_battle
    session["rounds"] += 1
    session["results"].append({"message": message, "result":result})
    if session['battle'] >= 150:
        gold_obtained = random.randint(10,20)
        session['gold'] += gold_obtained
        flash(f'You received {gold_obtained} gold from quest giver.')
    return redirect ('/battle')

@app.route('/reset')
def reset():
    session.pop('battle',None)
    session.pop('results', None)
    session.pop('rounds', None)
    return redirect('/battle')
