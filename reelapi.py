import RetrieveMovieList
import XMLGen

month = RetrieveMovieList.findDate()

#month = "april" #For debugging purposes

if not(month == "break"):
	movielist = RetrieveMovieList.scraper(month)
	output = XMLGen.MakeXMLString(movielist, month)
elif month=="break":
	output = XMLGen.MakeXMLError("The Reel is currently not open. Try again during the school year.")
else:
	output = XMLGen.MakeXMLError("An unknown error occurred.")

print "Content-Type: text/xml"
print ""
print output