
from OsTools import *
import time

handle = FileHandler('Admin')

files = ['1.txt', '2.txt', '3.txt', '4.txt']

handle.deleteFiles(files)

time.sleep(1)

for file in files:
  handle.createFile(file)