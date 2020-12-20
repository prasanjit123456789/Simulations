import xlrd
import matplotlib.pylab as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2
def excel_file(loc,sheet_no, row_start= 2,col_start= 1,row_end=None,col_end=None):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(sheet_no-1)
    first_time=True
    data=[]
    row_end=row_end if row_end!=None else sheet.nrows
    col_end = col_end if col_end != None else sheet.ncols
    for i in range(row_start-1,row_end):
        p=0
        for j in range(col_start-1,col_end):
            if first_time: data.append([])
            data[p].append(sheet.cell_value(i,j))
            p+=1
        first_time=False
    print("Reading complete........\n")
    del wb
    return np.array(data)

par_names=[]
def set_par_names(list):
    global par_names
    par_names=list

def other_params(f,x,y,parms,params_covar,sigma=None):
    global par_names
    if sigma==None:
        sigma=np.ones_like(y)
    r=f(x,*parms)-y
    ch2= np.sum((r/sigma)**2)
    DOF =len(y)-len(parms)
    print("%20s = %0.6f"%("chi2",ch2))
    print("%20s = %d"%("DOF",DOF))
    par_err=np.sqrt(np.diag(params_covar))
    par_no=0
    for i,j in zip(parms,par_err):
        if par_names==[]:
            print("%20s%d = %0.6e +/- %0.6e"%("par",par_no,i,j))
        else:
            print("%20s = %0.6e +/- %0.6e"%(par_names[par_no],i,j))
        par_no += 1
    print()
    return ch2, DOF, par_err



