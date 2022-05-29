import pyshorteners
s = pyshorteners.Shortener()
link = input("Enter the link to shorten: ")
print(s.chilpit.short(link)) 