import xmltodict
import json
import os

output_filename = 'data.json'
output_path = r'C:\Users\wwwki\Desktop\json'
with open('code xml.xml') as f:
    xml_data = f.read()

json_data = xmltodict.parse(xml_data)

json_string = json.dumps(json_data, indent=4)

print(json_string)

with open(os.path.join(output_path, output_filename), 'w') as f:
    f.write(json_string)

print(f'JSON data saved to: {os.path.join(output_path, output_filename)}')


