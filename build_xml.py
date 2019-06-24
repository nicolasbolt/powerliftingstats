import xml.etree.cElementTree as ET

def lifter_search_xml(name, wc, fed):
	data = ET.Element('data')
	n = ET.SubElement(data, 'name')
	w = ET.SubElement(data, 'wc')
	f = ET.SubElement(data, 'fed')
	n.text = name
	w.text = wc
	f.text = fed

	tree = ET.ElementTree(data)
	tree.write("form_data.xml")

def pull_lifter_data(xml_file):
	tree = ET.parse(xml_file)
	root = tree.getroot()
	for i in root.findall('name'):
		name = i.text
	for i in root.findall('wc'):
		wc = i.text
	for i in root.findall('fed'):
		fed = i.text
	xml_list = [name, wc, fed]
	return xml_list