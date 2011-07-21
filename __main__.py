import RetrieveMovieList
import XMLGen

#month = findDate()

month = "april" #For debugging purposes

movielist = RetrieveMovieList.scraper(month)

XMLGen.MakeXMLFile(movielist)

