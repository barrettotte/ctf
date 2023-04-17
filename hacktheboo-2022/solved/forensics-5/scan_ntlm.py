import xml.etree.ElementTree as ET

event_schema = '{http://schemas.microsoft.com/win/2004/08/events/event}'
tree = ET.parse('security_dump.xml')
events = tree.getroot()

for event in events:
    for event_child in event:
        if event_child.tag == event_schema + 'EventData':
            for event_data in event_child:
                data_name = event_data.attrib.get('Name')
                data_text = event_data.text
                if data_name == 'AuthenticationPackageName' and data_text == 'NTLM':
                    ET.indent(event)
                    print(ET.tostring(event, encoding='utf-8').decode())
