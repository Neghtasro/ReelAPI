#XML Generation Module
def toXML(f, movie, i):
    f.write("\t<movie" + str(i) + ">\n")
    f.write("\t<title>\n\t\t" + movie[0] + "\n\t</title>\n\t<dates>\n\t\t" + movie[1] + "\n\t</dates>")
    f.write("\t</movie" + str(i) + ">\n")

def MakeXMLFile(movies):
    """Generates the basic XML file, and calls the routine to generate XML for each listing."""
    
    f = open("movielist.xml", 'w')
    f.write("<?xml version=\"1.0\"?>\n<movielist>\n")
    i = 0
    
    for item in movies:
        i += 1
        toXML(f, item, i)
    
    f.write("</movielist>")
    f.close()