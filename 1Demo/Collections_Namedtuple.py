# -*- coding: utf-8 -*-
#Factory Function for Tuples with Named Fields
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'], verbose=True)
p = Point(11, y=22) 
print p[0] + p[1]
x, y = p 
print x
print y
print p.x + p.y 
print p


#import sqlite3
#EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
#conn = sqlite3.connect('/companydata')
#cursor = conn.cursor()
#cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
#for emp in map(EmployeeRecord._make, cursor.fetchall()):
#    print emp.name, emp.title


t = [11, 22]
print Point._make(t)
p._replace(x=33)
print p._asdict()
print p._fields
print getattr(p, 'x')

Status = namedtuple('Status', 'open pending closed')._make(range(3))
print Status.open, Status.pending, Status.closed
