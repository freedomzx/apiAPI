import flask
from flask import request, jsonify
#http://127.0.0.1:5000/
app = flask.Flask(__name__)
app.config["DEBUG"] = True

"""
    "Level": ,
    "Type": "",
    "MP": ,
    "Casting Time": ,
    "Recast Time": ,
    "Description": ""
"""

jobs = [
    #Black Mage
    {
        "Job": "Black Mage",
        "PvE": {
            "Blizzard": {
                "Level": 1,
                "Type": "Spell",
                "MP": 400,
                "Casting Time": 2.5,
                "Recast Time": 2.5,
                "Description": "Deals ice damage with a potency of 180.\nAdditional Effect: Grants Umbral Ice or removes Astral Fire\nDuration: 15s"
            },
            "Fire": {
                "Level": 2,
                "Type": "Spell",
                "MP": 800,
                "Casting Time": 2.5,
                "Recast Time": 2.5,
                "Description": "Deals fire damage with a potency of 180.\nAdditional Effect: Grants Astral Fire or removes Umbral Ice\nDuration: 15s\nAdditional Effect: 40% chance next Fire III will cost no MP and have no cast time\nDuration:18s"
            },
            "Transpose": {
                "Level": 4,
                "Type": "Ability",
                "MP": 0,
                "Casting Time": 0,
                "Recast Time": 5,
                "Description": "Swaps Astral Fire with a single Umbral Ice, or Umbral Ice with a single Astral Fire."
            },
            "Thunder": {
                "Level": 6,
                "Type": "Spell",
                "MP": 200,
                "Casting Time": 2.5,
                "Recast Time": 2.5,
                "Description": "Deals lightning damage with a potency of 30.\nAdditional Effect: Lightning damage over time\nPotency: 40\nDuration: 18s\nAdditional Effect: 10% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP\nDuration: 18s\nOnly one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target."
            }
        }
    }
]

@app.route('/', methods=["GET"])
def home():
    return "<h1>An API</h1><p>This site is for an API for... something</p>"

@app.route('/api/v1/jobs/all', methods=['GET'])
def api_all():
    return jsonify(jobs)

app.run()