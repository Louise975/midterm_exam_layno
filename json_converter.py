import json
import yaml

try:
    with open("service_catalog.yaml", "r") as f:
        data = yaml.safe_load(f)
    with open ("service catalog.json", "w") as f:
        json.dump(data, f, indent=4)
    print("succesfully converted yaml to json")
except FileNotFoundError:
    print("Error: service_catalog.yaml not found")
except yaml.YAMLError:
    print("Error: service catalog is corrupted")