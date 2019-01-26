#!python
import cgi,os

form=cgi.FieldStorage()
pageid=form["pageid"].value

os.remove('data/'+pageid)

#Redirection
print("location:index.py")
print()
