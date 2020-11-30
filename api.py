import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    dicti = {}
    for idx, col in enumerate(cursor.description):
        dicti[col[0]] = row[idx]
    return dicti

#http://127.0.0.1:5000/
@app.route('/', methods=["GET"])
def home():
    return "<h1>An API</h1><p>This site is for an API for... something</p>"

#404 resource not found
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The requested resource could not be found.</p>"

#/api/v1/ffxiv/jobs/all - all ffxiv jobs
@app.route('/api/v1/ffxiv/jobs/all', methods=['GET'])
def ffxiv_jobs_all():
    #connect to sqlite and set cursor
    connection = sqlite3.connect('api.db')
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    #execute query for all jobs
    query = "select * from ffxiv_jobs"
    all_jobs = cursor.execute(query).fetchall()

    return jsonify(all_jobs)

#/api/v1/ffxiv/spells/all - all ffxiv spells
@app.route('/api/v1/ffxiv/actions/all', methods=['GET'])
def ffxiv_spells_all():
    #connect to sqlite and set cursor
    connection = sqlite3.connect('api.db')
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    #execute query for all spells
    query = "select * from ffxiv_actions"
    all_spells = cursor.execute(query).fetchall()

    return jsonify(all_spells)

#/api/v1/ffxiv/jobs/spells?job=??? - all spells for a certain job - use 3 letter abbreviation
@app.route('/api/v1/ffxiv/jobs/actions', methods=['GET'])
def ffxiv_job_spells():
    #get args
    params = request.args
    job = params.get('job')

    #prep query
    query = "select * from ffxiv_actions where"
    to_filter = []
    if job:
        query += ' job=?'
        to_filter.append(job)
    else:
        return page_not_found(404)
    query += ";"

    #connect to sqlite and set cursor
    connection = sqlite3.connect('api.db')
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    #execute query for all spells listed under a job
    results = cursor.execute(query, to_filter).fetchall()

    return jsonify(results)

#/api/v1/ffxiv/actions
@app.route('/api/v1/ffxiv/actions', methods=['GET'])
def ffxiv_spell():
    #get args
    params = request.args
    action = params.get('action_name')

    #prep query
    query = "select * from ffxiv_actions where"
    to_filter = []
    if action:
        query += ' action_name=?'
        to_filter.append(action)
    else:
        return page_not_found(404)
    query += ";"

    #connect to sqlite and set cursor
    connection = sqlite3.connect('api.db')
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    #execute query for all spells listed under a job
    results = cursor.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()