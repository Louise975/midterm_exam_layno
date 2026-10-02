import argparse
from requests.exceptions import HTTPError
from registry_client import RegistryClient

parser = argparse.ArgumentParser()
parser.add_argument("service_id", type=int)
args = parser.parse_args()
sid = args.service_id

client = RegistryClient()

try:
    before = client.get_service(sid)
    print(f"Status before: {before['status']}")

    after = client.update_service(sid, {"status": "maintenance"})
    print(f"Status after: {after['status']}")

    check = client.get_service(sid)
    print(f"Confirmed: {check['status']}")

    client.delete_service(sid)
    print(f"Deregistered {before['name']} (id {sid})")

except HTTPError:
    print(f"Service with id {sid} not found, nothing to do.")