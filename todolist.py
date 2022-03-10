'''
todolist.py is a Object Relational Mapping to the todolist database

The ORM will work map SQL rows with the schema
    (rowid,title,desc,completed)
to Python Dictionaries as follows:

(5,'commute','drive to work',false) <-->
{rowid:5,title:'commute',desc:'drive to work',completed:false)

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/todo.db

'''
import sqlite3
import os

def toDict(t):
    ''' t is a tuple (rowid,title, desc,completed)'''
    return {rowid:t[0], title:t[1], desc:t[2], completed:t[3]}

class TodoList():
    def __init__(self):
        con= sqlite3.connect(os.getenv('HOME')+'/todo.db')
        cur = con.cursor() 
        cur.execute('''CREATE TABLE IF NOT EXISTS todo
                    (title text, desc text, completed int)''')
        con.commit()
        con.close()
    def selectActive(self):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/todo.db')
        cur = con.cursor() 
        cur.execute("SELECT rowid,* from todo where completed=0")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    def selectAll(self):
        pass
    def selectCompleted(self):
        pass
    def add(self,title,desc,completed):
        pass
    def delete(self,rowid):
        pass
    def complete(self,rowid):
        pass


    
        
