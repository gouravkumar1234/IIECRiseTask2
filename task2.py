#! /usr/bin/python3
import cgi
import subprocess
print("context-type: text/html")
print()

input = cgi.FieldStorage()
commandText = input.getvalue("commandText")
sudoCommand = "sudo " + commandText
output = subprocess.getoutput(sudoCommand)
print("""<html><style>body{background-color:rgb(200,200,200);color:black;}</style><h2>Result: <h2></html>""")
print(output)