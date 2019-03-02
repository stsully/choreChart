#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

from flask import Flask, request, render_template
import sqlite3
import datetime
import pprint

app = Flask(__name__)

def getDB():
    try:
        conn = sqlite3.connect('chores.sqlite')
    except IOError:
        print "Error: can\'t find db file"
        exit(1)
    return conn

def getDayOfWeek():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    d = datetime.date.today()
    return week[d.weekday()]

def validUser(user):
    users = {"JP": "John", "JM":"Josephine", "CW":"Charlie", "ME": "Mary", "SA":"Stella"}
    if user in users:
        return True
    else:
        return False

###MAIN App ###
@app.route("/")
def showChores():
    # print request
    ###Note that the HTMl has the full data set in it, no need to query sqlite
    ##TODO: convert it to DB
    return render_template("chores.html")

@app.route("/daily")
def showDaily():
    print request
    db = getDB()
    c = db.cursor()
    print "SELECT chore, " + getDayOfWeek() + " FROM chores ORDER BY " + getDayOfWeek()
    c.execute("SELECT chore, " + getDayOfWeek() + " FROM chores ORDER BY " + getDayOfWeek())
    entries = c.fetchall()
    day = getDayOfWeek()
    print entries
    return render_template("daily.html", dayOfWeek=day, entries=entries)

@app.route("/user", methods=['GET'])
def user():
    #Flask passes in the request values as a hash of lists: access with getlist("key")
    user = request.args.getlist('user')[0].upper()
    if validUser(user) == False:
        userTuple = ('*',)
    else:
        userTuple = (user,)
    db = getDB()
    c = db.cursor()
    c.execute('SELECT chore, ' + getDayOfWeek() + ' FROM chores WHERE ' + getDayOfWeek() + ' like ?', userTuple)
    entries = c.fetchall()
    print "Entries: ", entries
    return render_template("daily.html", entries=entries)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
