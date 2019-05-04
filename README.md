# Basic Flask api seed project.

Main Dependencies include:
1. Flask
2. Flask-RESTful -- https://flask-restful.readthedocs.io/en/latest/
3. Flask-RESTplus -- https://flask-restplus.readthedocs.io/en/stable/
4. pep8 -- https://www.python.org/dev/peps/pep-0008/


Steps to run the project:
1. Clone the repo.
2. Create virtual environment on python
    a. Option 1: You can use Anaconda's `conda create -n test_env python=3.5`
    b. Option 2: You can create a virtual env using steps: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
3. Activate the virtual environment -- Follow steps based on the option you chose for Step 2.
4. Change directory to the project `cd PATH_TO/flask-rest-template`.
5. Install dependencies using `pip install -r requirements.txt`. This is install the dependencies listed in `requirements.txt` file.
6. Optional: To turn the DEBUG_MODE on, set environment variable `export DEBUG_MODE=True` 
7. Run the app. Use `python src/app.py`. 
8. Swagger doc for current api is configured to show up on: `http://localhost:5000/v1`

Features: 
- Release version can be configure from `settings/version.py`
- Environment variables can be used to configure settings in `settings/main.py`
    To export an environment variable use `export VARIABLE_NAME` in the root directory of the project i.e `cd PATH_TO/flask-rest-template`
- Write end-points in `src/api/v1/endpoints.py`. Suggestion: For every new namespace, create a new file.
- To install more dependencies, just do `pip install DEPENDENCY_NAME`. Persists this change by `pip freeze > requirements.txt` -- This is add it to the list for future setups or setup on other machine.