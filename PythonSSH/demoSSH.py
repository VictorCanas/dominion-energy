#! /usr/bin/python

import os
import paramiko
import xlsxwriter
import socket
import  re
import sys
import smtplib
import getpass

username = "admin"
password = "pass"

# Opens file in read mode
f1 = open("hostfile.txt","r")
f2 = open("commandfile.txt","r")

# Creates list based on f1 and f2
devices = f1.read().split(',')
commands = f2.read().split(',')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

data = []
for device in devices:
        column = device.split()
        data.append([column[0]])
        print column[0]
        for command in commands:
            try:
                    conn=ssh.connect(column[0], username=username, password=password, timeout=4)
                    if conn is None:
                        stdin, stdout, stderr = ssh.exec_command(command)
                        data[-1].append(stdout.read())
                        ssh.close()
            except  paramiko.AuthenticationException:
                    output = "Authentication Failed"
                    data[-1].append(output)
                    break
            except  paramiko.SSHException:
                    output = "Issues with SSH service"
                    data[-1].append(output)
                    break
            except  socket.error, e:
                    output = "Connection Error"
                    data[-1].append(output)
                    break
        data[-1] = tuple(data[-1])


f1.close()
f2.close()

#Create Workbook instance
book = xlsxwriter.Workbook('Workbook.xlsx')
sheet = book.add_worksheet('Sheet1')

header = ["hostname","show version","show inventory","show module","show diag","show environment all"]
#the header creates the columns for the commands that are run

#Define and format header
header_format = book.add_format({'bold':True , 'bg_color':'yellow'})

for col, text in enumerate(header):
    sheet.write(0, col, text, header_format)



# Now, let's write the contents
for row, data_in_row in enumerate(data):
    for col, text in enumerate(data_in_row):
        sheet.write(row + 1, col, text)


book.close()
