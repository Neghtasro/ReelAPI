import RetrieveMovieList
import XMLGen

#month = findDate()

month = "april" #For debugging purposes

movielist = RetrieveMovieList.scraper(month)

output = XMLGen.MakeXMLString(movielist)

print "Content-Type: text/xml"
print ""
print output

