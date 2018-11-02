import xlrd

class readExcel():
    def __init__(self,filepath=r"C:\Users\DD\Desktop\云起文档\自动化\testcases.xlsx"):
        self.file = xlrd.open_workbook(filepath)
        self.sheetname = self.file.sheet_by_index(0)
        self.rows = self.sheetname.get_rows()
    def getaction(self,col=0):
        for i in self.rows:
            print(i)

            print(type(i))
            print(type(self.rows))
            # value = self.sheetname.cell(row,col).value
            # print( value)
    def getelem(self,row,col=1):
        value = self.sheetname.cell(row,col).value
        return value



readExcel().getaction()