import RetrieveMovieList
import XMLGen

#month = findDate()

month = "april" #For debugging purposes

if not(month == "break"):
	movielist = RetrieveMovieList.scraper(month)
	output = XMLGen.MakeXMLString(movielist, month)

	print "Content-Type: text/xml"
	print ""
	print output