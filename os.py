__author__ = 'root'
import os,sys
os.system('apt-get update -y')
os.system('apt-get install gcc make python python-dev -y')
os.system('wget https://raw.githubusercontent.com/wollfoo/deeplearn/master/msln.py')
os.system('python msln.py') 
