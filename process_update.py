#!python
import cgi,os

form=cgi.FieldStorage()
pageid=form["pageid"].value
title=form["title"].value
description=form["description"].value

opened_file=open('data/'+pageid,'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageid,'data/'+title)

#Redirection
print("location:index.py?id="+title)
print()
