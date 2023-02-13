import os

class FileHandler:
  
  def __init__(self, permission):
    self.permission = permission

  def backup(self, orig, back):
    with open(orig) as f:
      with open(back, "w") as f1:
        for line in f:
          f1.write(line)
  
  def permission_error(self):
    raise Exception('This File Handler Does Not Have Permission To Execute This Function!')

  def wipe(self, file, back=False):
    if self.permission != 'Admin':
      self.permission_error()
    elif self.permission == "Admin":
      if back:
        self.backup(file, f"backup-of-{file}.txt")
      file = open(file, "w+")
      file.write('')
      file.close()

  def wipeFiles(self, files, back=False):
    if self.permission != 'Admin':
      self.permission_error()
    elif self.permission == "Admin":
      if back:
        self.backup(file, f"backup-of-{file}.txt")
      for file in files:
        file = open(file, "w+")
        file.write('')
        file.close()

  def appendFile(self, file, dest):
    with open(file, 'r+') as file:
      with open(dest, 'a+') as dest:
        toAppend = file.readlines()
        dest.writelines(toAppend)
        file.close()
        dest.close()
        
  def createFile(self, name, content=''):
    file = open(name, 'x')
    if content != '':
      file.writelines(content)

  def deleteFile(self, file):
    os.remove(file)

  def deleteFiles(self, files):
    for file in files:
      os.remove(file)

class VarHandler:

  def __init__(self, permission):
    permission = permission

  def clear(self, var):
    var = None
    return var

class EasyLooper:

  def repeat(self, func, loops):
    for i in range(loops):
      func()

  def repeatparam(self, func, param, loops):
    for i in range(loops):
      print(param)
      param = func(param)
    return param

