# apiAPI
apiAPI (Attack Properties Interface API) is a RESTful API created in Python Flask, designed to provide video game attack information for several video games (Street Fighter V, Tekken 7, Final Fantasy XIV, etc).

All information is retrieved in a json format, using a GET request to the specified API endpoints.

# Final Fantasy XIV

## List of jobs

/api/v1/ffxiv/jobs/all

## List of all actions

/api/v1/ffxiv/spells/all

## All spells for a certain job

/api/v1/ffxiv/jobs/spells?job=<3 letter abbreviation of job>

## Information on specific job action

/api/v1/ffxiv/actions?action_name=<action name, all lowercase, use - instead of a space>