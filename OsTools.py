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
            for file in files:
                if back:
                    self.backup(file, f"backup-of-{file}.txt")
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
        try:
            file = open(name, 'x')
        except FileExistsError as error:
            print('A file with this name already exists!\nError:', error)
        if content != '':
            file.writelines(content)

    def deleteFile(self, file):
        try:
            os.remove(file)
        except FileNotFoundError as error:
            print('The file:', file, 'does not exist.\nError:', error)

    def deleteFiles(self, files):
        for file in files:
            try:
                os.remove(file)
            except FileNotFoundError as error:
                print('The file:', file, 'does not exist.\nError:', error)


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

    def repeatParam(self, func, param, loops):
        for i in range(loops):
            print(param)
            param = func(param)
        return param

