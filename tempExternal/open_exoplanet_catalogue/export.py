from html.parser import HTMLParser


def indent(elem, level=0):
    i = "\n" + level * "\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

class MyHTMLParser(HTMLParser):#HTML parser to get the information from the webpage
    def handle_starttag(self, tag, attrs): #get start tag and may store its attributes
        global boolean, dictio_mags, data2, dictio_ident, inname
        if tag =="a" and section=="identifiers":
            inname = 1

    def handle_data(self, data):
        global data2, boolean, section, inname, dictio_distance, dictio_coord, dictio_spectral