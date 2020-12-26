from graph import*

f=lambda x,a,b: a*x +b

loc="DATA.xls"

bbox=dict(facecolor='white', edgecolor='black', boxstyle='round',alpha=0.5)

print(loc)
data= excel_file(loc, 1)

pov,povc=curve_fit(f,data[0],data[1])

par_names=["Slope","Intercept"]

chi2,DOF,par_err = other_params(f,*data,pov,povc,names=par_names)

text= "Slope = %0.3e +/- %0.3e\n"%(pov[0],par_err[0])+"Intercept = %0.3e +/- %0.3e"%(pov[1],par_err[1])

plt.plot(*data,"ro",ls=':',label="Data")

plt.plot(data[0],f(data[0],*pov),color="green",label="Fit")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Whatever")
plt.text(7.5,4,text,bbox=bbox)
#plt.text(7.5,2.8,,bbox=bbox)

plt.legend().set_draggable(True)

plt.show()
#plt.savefig("data.png")

