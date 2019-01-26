#!python
print("content-type: text/html; charset=euc-kr\n")
print()
import cgi,os,view

form=cgi.FieldStorage()
if 'id' in form:
    pageid=form["id"].value
    description=open('data/'+pageid,'r').read()
else:
    pageid='Welcome'
    description='Hello'

print('''
<!doctype html>
<html>
    <head>
        <title>KGW HTML&PYTHON Practice</title>
        <meta charset="euc-kr">
    </head>
    <body>
        <h1><a href="index.py">Entertainment</a></h1>
        <ol>{list}</ol>
        <a href="update.py">update</a>
        <form action="process_update.py" method="post" accept-charset="utf-8">
            <input type="hidden" name="pageid" value={title}>
            <p><input type="text" name="title" placeholder="title" value={title}></p>
            <p><textarea rows="4" name="description" placeholder="description">{desc}</textarea></p>
            <p><input type="submit"></p>
        </form>
    </body>
</html>
'''.format(list=view.getlist(),title=pageid,desc=description))
