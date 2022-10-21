import yaml
import sys
from detect_key import detect_secret_manual_simple

inputfile  = sys.argv[1]
outputfile = sys.argv[2]

try:
  options = sys.argv[3]
except: options = None

file = open(inputfile, "r")
lines = file.readlines()
json_envs = {
  "apiVersion": "v1",
  "kind": "ConfigMap",
  "metadata": {
    "annotations": {
      "reloader.stakater.com/match": "true"
    },
    "name": outputfile.split(".")[0]
  }
}

json_secret = {
  "apiVersion": "v1",
  "kind": "Secret",
  "metadata": {
    "name": outputfile.split(".")[0]
  },
  "type": "Opaque"
}

env = {}
secret = {}
for line in lines:
  if "${" in line and "}" in line:
    raw = line.split("${")[1].split("}")[0]
    index = raw.index(":")
    key = raw[0:index]
    if options == '-s':
      if detect_secret_manual_simple(key=key):
        value = raw.split(f"{key}:")[1]
        secret.update({key:value})
    value = raw.split(f"{key}:")[1]
    env.update({key:value})

# Close read file
file.close()

# Update json env
json_envs.update({"data":env})
yaml_data = yaml.dump(json_envs,indent=2, default_flow_style=False)
file = open(outputfile, "a")
file.write(yaml_data)
file.close()

print(f"Done at {outputfile} type: configmap!")

# Update json secret
if options == '-s':
  json_secret.update({"data":secret})
  yaml_data = yaml.dump(json_secret,indent=2, default_flow_style=False)
  file = open(f"secret-{outputfile}", "a")
  file.write(yaml_data)
  file.close()
  print(f"Done at {outputfile} type: secrets~")
