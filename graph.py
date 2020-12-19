import xlrd
import matplotlib.pylab as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2
def file_excel(loc,sheet_index, row_start= 1,col_start= 1, init_str= True,row_end=None,col_end=None):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(sheet_index)
    first_time=True
    data=[]
    row_start=row_start-1 if not init_str else row_start
    row_end=row_end if row_end!=None else sheet.nrows
    col_end = col_end if col_end != None else sheet.ncols
    for i in range(row_start,row_end):
        p=0
        for j in range(col_start-1,col_end):
            if first_time: data.append([])
            data[p].append(sheet.cell_value(i,j))
            p+=1
        first_time=False
    print("Reading complete........")
    del wb
    return np.array(data)

def CHI2(f,x,y,parms,sigma=None):
    if sigma==None:
        sigma=np.ones_like(y)
    r=f(x,*parms)-y
    ch2= np.sum((r/sigma)**2)
    DOF =len(y)-len(parms)
    print("chi2 = %0.6f"%ch2)
    print("DOF = %d"%DOF)
    return ch2, DOF



