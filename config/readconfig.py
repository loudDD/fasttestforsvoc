import configparser

class readConfig():
    def __init__(self,filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)
    def getconfigvalue(self,section,name):
        value = self.cf.get(section,name)
        return value


