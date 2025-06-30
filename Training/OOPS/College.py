class College:
    def __init__(self,cname,caddrr,cdept):
        self.cname=cname
        self.caddrr=caddrr
        self.cdept=cdept
    def show(self):
        print(f'Colllege Name: {self.cname} \nCollege Address: {self.caddrr} \nDepartment Name: {self.cdept}')
