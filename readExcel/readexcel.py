import xlrd
from config.readconfig import readConfig
class readExcel():
    def __init__(self,filepath=readConfig.getconfigvalue("xlrdpath","filepath")):
        self.file = xlrd.open_workbook(filepath)
        self.sheetname = self.file.sheet_by_index(0)
        self.rows = self.sheetname.get_rows()
    def getaction(self,col=0):
        for i in self.rows:
            row = i
            value = self.sheetname.cell(row,col).value
            return value
    def getelem(self,row,col=1):
        value = self.sheetname.cell(row,col).value
        return value



