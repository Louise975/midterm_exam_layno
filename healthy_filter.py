import json 
import yaml

with open("service_catalog.yaml", "r") as f:
    data = yaml.safe_load(f)


services = data.get("services") or []

healthy_count = sum(1 for s in services if s.get("status") == "healthy")
unhealthy_count = sum(1 for s in services if s.get("status") == "unhealthy")
maintenance_count = sum(1 for s in services if s.get("status") == "maintenance")

healthy_names = sorted([s["name"] for s in services if s.get("status") == "healthy"])

filetered_services = [s for s in services if s.get("status") == "healthy"]

output_data = data.copy()
output_data["services"] = filetered_services

with open("healthy_services.json", "w") as f:
    json.dump(output_data, f, indent=4)

print(f"Healthy: {healthy_count} | Unhealthy: {unhealthy_count} | Maintenance: {maintenance_count}")
print(f"healthy services: {', '.join(healthy_names)}")