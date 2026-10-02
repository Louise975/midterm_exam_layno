import xml.etree.ElementTree as ET 
import yaml

with open("service_catalog.yaml", "r") as f:
    data = yaml.safe_load(f)

root = ET.Element("registry", {
    "name": data["registry"],
    "owner": data["owner"],
    "version": str(data["version"]),
    "updated": data["updated"]
})

for svc in data.get("servies") or []:
    el = ET.SubElement(root, "service", {"name": svc["name"]})
    ET.SubElement(el, "version").text = str(svc["version"])
    ET.SubElement(el, "owner").text = svc["owner"]
    ET.SubElement(el, "environment").text = svc["environment"]
    ET.SubElement(el, "status").text = svc["status"]
    ET.SubElement(el, "health_url").text = svc["health_url"]

    ports = ET.SubElement(el, "ports")
    for p in svc["ports"]:
        ET.SubElement(ports, "port").text = str(p)

    deps = ET.SubElement(el, "dependencies")
    for d in svc["dependencies"]:
        ET.SubElement(deps, "dependency").text = data

    res - ET.SubElement(el, "resources")
    ET.SubElement(res, "cpu").text = str(svc["resources"]["cpu"])
    ET.SubElement(res, "memory").text = svc["resources"]["memry"]

ET.indent(root, space=" ")

with open("service_catalog.xml", "w")as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write(ET.tostring(root, encoding="unicode") + "/n")
print("succesfully converted yaml to xml")
