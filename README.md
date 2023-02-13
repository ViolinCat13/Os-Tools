# OsTools by Neocryptix
##  Created by ViolinCat

To use this module, first add the OsTools.py file into your project. Then import it into the file you want to use it in like this:
```python
from OsTools import *
```
Or:
```python
from OsTools import FileHandler
```
To import a specific class
## File Handling

To create a file handler, use this code:
```python
handler = FileHandler(<permission level>)
```
The file handler has two permission modes, Admin and User. Admin permission is required to wipe files.

### Backups

Creates a backup (copy) of any file containing text. Does not work with images, videos, or GIFs.

```python
handler.backup(<file name>, <backup file>)

```

### Wiping Files

To wipe a file, use the wipe function like this:
```python
handler.wipe(<file to wipe>, <backup>)
```
The parameter \<backup> is an optional boolean value which indicates whether to create a backup of the file. By default it is set to false

To wipe multiple files use the wipeFiles function:
```python
files = ['file1.txt', 'file2.txt', 'file3.txt']

handler.wipefiles(files)
```
The syntax is:
```python
handler.wipefiles(<list of filenames>, <backup>)
```
The files you want to wipe should be in a list.

### Creating Files

This function creates a file, which is empty by default.
```python
handler.createFile(<file name>, <content>)
```
The \<content> parameter is optional, use it if you want to create a file with content in it already.

### Deleting Files

To delete a file, use the deleteFile function
```python
handler.deleteFile(<file>)
```
To delete multiple files use the deleteFiles function, which has the same syntax as the wipeFiles function, without the backup parameter.

### Append File

The appendFile function appends one file to the end of another file.
```python
handler.appendFile(<file>, <destination>)
```

## Variable Handling

To create a variable handler, use this code:
```python
handler = VarHandler(<permission level>)
```

### Wipe Variables
The wipe function sets the value of a variable to None
```python
handler.wipe(<variable>)
```

## Easy Looping

### Repeating Functions

To repeat a function, use the repeat function:
```python
handler.repeat(<function>, <repeats>)
```
To repeat a function with a parameter, use the repeatParam function:
```python
handler.repeatParam(<function>, <parameter>, <repeats>)
```
Note: This only works with one parameter