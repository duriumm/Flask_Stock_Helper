import os
import json
root_path = os.path.dirname(__file__)

def get_config():
  print("getting config from utils")
  config_file_path = os.path.join(root_path, "config.json")
  print(f"Using config: {config_file_path}") ##### 
  if os.path.isfile(config_file_path):
      config_json_file = config_file_path
      with open(config_json_file, "r") as f:
          config = json.load(f)
  return config