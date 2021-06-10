#!/usr/bin/env python3

loginfail = 0 

keystonefile = open("/home/student/pythoMyCode/loops/WorkingWith/keystone.common.wsgi","r")

keystone_file_lines = keystonefile.readlines()

for line in keystone_file_lines:

    if "- - - - -] Authorization failed" in line:
        loginfail += 1

print("The number of failed log in attempts is", loginfail)

keystonefile.close()


