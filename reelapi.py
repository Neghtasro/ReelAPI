import RetrieveMovieList
import XMLGen
import sys

xml = True
month = ""
for item in sys.argv[1:]:
	if item == "json":
		xml = False
	elif (RetrieveMovieList.monthCheck(item) == True):
		month = item

if month == "":
	month = RetrieveMovieList.findDate()
	

#month = "april" #For debugging purposes
if xml == True:
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