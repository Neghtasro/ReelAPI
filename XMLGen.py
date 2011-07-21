#XML Generation Module
def toXML(movie, i):
    return ("\t<movie" + str(i) + ">\n") + \
	("\t<title>\n\t\t" + movie[0] + "\n\t</title>\n\t<dates>\n\t\t" + movie[1] + "\n\t</dates>") + \
	("\t</movie" + str(i) + ">\n")

def MakeXMLFile(movies, month):
    """Generates the basic XML file, and calls the routine to generate XML for each listing."""
    
    f = open("/output/movielist.xml", 'w')
    f.write("<?xml version=\"1.0\"?>\n<movielist>\n") + \
	("\t<month>\n\t\t" + month + "\n\t</month>\n")
    i = 0
	
    for item in movies:
        i += 1
        f.write(toXML(item, i))
    
    f.write("</movielist>")
    f.close()
	
def MakeXMLString(movies, month):
    """Generates a string, which will form an XML file when parsed. Hopefully."""
    
    str = ("<?xml version=\"1.0\"?>\n<movielist>\n" + "\t<month>\n\t\t" + month + "\n\t</month>\n")
    i = 0
	
    for item in movies:
        i += 1
        str += toXML(item, i)
    
    str += ("</movielist>")
    return str