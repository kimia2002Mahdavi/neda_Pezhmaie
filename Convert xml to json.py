import xmltodict
import json

with open('code xml.xml') as f:
    xml_data = f.read()

json_data = xmltodict.parse(xml_data)

json_string = json.dumps(json_data, indent=4)

print(json_string)


