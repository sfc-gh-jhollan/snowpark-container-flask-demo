# Snow Services Flask API example

## Pre-reqs
- Python (builds to Python 3.10 docker)

## Setup

1. `https://github.com/snowflakecorp/snowservice-udf-flask`
2. `cd snowservice-udf-flask`
3. Create a virtual environment: `python3 -m venv .venv`
4. Activate the virtual environment: `source .venv/bin/activate`
5. Install packages: `pip install -r requirements.txt`
6. Test running the app: `python -m flask --app app run`
7. You can call the endpoint by crafting a request like is in the `test.http` folder. I use the VS Code extension "REST Client" which just lets me click the "Send Request" button in the file.
8. Build a docker container: `docker build -t {your_snowservice_registry_path}/{database}/{schema}/{repository}/flask .`
9. Push the docker container to your registry: `docker push {your_snowservice_registry_path}/{database}/{schema}/{repository}/flask`
10. Update the contents of `flask.yaml` with the path to your container image
11. Upload flask.yaml to a stage
12. Run the commands in `deploy.sql`
13. Call the UDF: `select echo('{ "hello": "world"});`