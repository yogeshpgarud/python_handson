import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../config/')))
config_path = "../config/"

print os.getcwd()
print sys.path
print os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# data = json.load(open(config_path+'config.json'))

# pprint(data)
