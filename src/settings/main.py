import os

ROOT_DIR = '/'.join(os.path.abspath(__file__).split('/')[0:-2])

# App settings. Read setting from the environment variables. Variable value can also be hard coded.
DEBUG_MODE = True if os.environ.get('DEBUG_MODE') == 'True' else False
