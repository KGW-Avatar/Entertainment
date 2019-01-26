#!python
print("content-type: text/html; charset=euc-kr\n")
print()
import cgi,os,view

form=cgi.FieldStorage()
if 'id' in form:
    pageid=form["id"].value
    description=open('data/'+pageid,'r').read()
    update_link='<a href="update.py?id={}">update</a>'.format(pageid)
    delete_action='''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageid" value="{}">
            <input type="submit" value="delete">
        </form>
        '''.format(pageid)
else:
    pageid='Welcome'
    description='Hello'
    update_link=''
    delete_action=''

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
        <a href="create.py">create</a>
        {update}
        {delete}
        <h2>{title}</h2>
        <p>{desc}</p>
    </body>
</html>
'''.format(title=pageid,desc=description,list=view.getlist(),update=update_link,delete=delete_action))
