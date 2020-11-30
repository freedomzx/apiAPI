import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

"""
"name": "",
"level": ,
"type": "",
"mp": ,
"cast_time": ,
"recast_time": ,
"description": ""
"""

jobs = [
    #Black Mage
    {
        "job": "black-mage",
        "abbreviation": "blm",
        "full": "Black Mage",
        "PvE": {
            0: {
                "name": "Blizzard",
                "level": 1,
                "type": "spell",
                "mp": 400,
                "cast_time": 2.5,
                "recast_time": 2.5,
                "description": "Deals ice damage with a potency of 180.\nAdditional Effect: Grants Umbral Ice or removes Astral Fire\nDuration: 15s"
            },
            1: {
                "name": "Fire",
                "level": 2,
                "type": "Spell",
                "mp": 800,
                "cast_time": 2.5,
                "recast_time": 2.5,
                "description": "Deals fire damage with a potency of 180.\nAdditional Effect: Grants Astral Fire or removes Umbral Ice\nDuration: 15s\nAdditional Effect: 40% chance next Fire III will cost no MP and have no cast time\nDuration:18s"
            },
            2: {
                "name": "Transpose",
                "level": 4,
                "Type": "Ability",
                "mo": 0,
                "cast_time": 0,
                "recast_time": 5,
                "description": "Swaps Astral Fire with a single Umbral Ice, or Umbral Ice with a single Astral Fire."
            },
            3: {
                "name": "Thunder",
                "level": 6,
                "Type": "Spell",
                "mo": 200,
                "cast_time": 2.5,
                "recast_time": 2.5,
                "description": "Deals lightning damage with a potency of 30.\nAdditional Effect: Lightning damage over time\nPotency: 40\nDuration: 18s\nAdditional Effect: 10% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP\nDuration: 18s\nOnly one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target."
            },
            4: {
                "name": "Sleep",
                "level": 10,
                "Type": "Spell",
                "mo": 800,
                "cast_time": 2.5,
                "recast_time": 2.5,
                "description": "Puts target and all nearby enemies to sleep."
            }
        }
    }
]
#http://127.0.0.1:5000/
@app.route('/', methods=["GET"])
def home():
    return "<h1>An API</h1><p>This site is for an API for... something</p>"

@app.route('/api/v1/ffxiv/jobs/all', methods=['GET'])
def ffxiv_api_all():
    return jsonify(jobs)

#api/v1/ffxiv/jobs?id=xxxx
@app.route('/api/v1/ffxiv/jobs', methods=['GET'])
def ffxiv_api_job():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided"

    results = []

    for job in jobs:
        if job["job"] == id or job["abbreviation"] == id or job["full"] == id:
            results.append(job)

    return jsonify(results)

@app.route('/api/v1/ffxiv/spells/all', methods=['GET'])
def ffxiv_api_spells_all():
    results = []

    for job in jobs:
        for i in job["PvE"]:
            results.append(i)

    return jsonify(jobs)

app.run()