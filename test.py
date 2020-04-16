# from test1 import module as ml
import unittest
from test1 import app
from werkzeug.serving import run_simple

if __name__ == "__main__":
    # ml.unittest.main()
    run_simple('localhost', 5000, app, use_reloader= True, use_debugger = True, use_evalex=True)