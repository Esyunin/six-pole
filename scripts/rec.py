from pylab import *
from matplotlib import rc
from functions import parsing
import os.path as path
import sys
from scipy import interpolate
from pandas import read_excel as read
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])


rc('font', family='serif')

rec = path.abspath('..'+'\\rec\\rec.xlsx')
# # ion()
# df=read(rec, sheet_name='Uрез=90В')

# figure('Uрез=90В,1')
# x=3*array(df['Uотр, В/3'])
# y=array(df['I, mA'])
# g = interpolate.interp1d(x,y, 'cubic')
# x=linspace(0,x[-1],1000)
# y=g(x)
# # plot(x,y)
# plot(3*df['Uотр, В/3'],df['I, mA'],'*')
# xlabel(r'$U_{\text{отр}}$, \text{В}',fontsize=16)
# ylabel(r'$I$, деления',fontsize=16)
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')
# minorticks_on()
# savefig(path.abspath('..'+'\\fig\\res90V_1.pdf'))

# figure('Uрез=90В,2')
# plot(3*df['Uотр, В/3'],df['lambda, cm'],'*')
# xlabel(r'$U_{\text{отр}}$, \text{В}',fontsize=16)
# ylabel(r'$\lambda$, см',fontsize=16 )
# ylim((10,11))
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')    
# minorticks_on()
# savefig(path.abspath('..'+'\\fig\\res90V_2.pdf'))

# df=read(rec, sheet_name='Uрез=96В')

# figure('Uрез=96В,1')
# x=3*array(df['Uотр, В/3'])
# y=array(df['I, mA'])
# g = interpolate.interp1d(x,y, 'cubic')
# x=linspace(0,x[-1],1000)
# y=g(x)
# # plot(x,y)
# plot(3*df['Uотр, В/3'],df['I, mA'],'*')
# xlabel(r'$U_{\text{отр}}$, \text{В}',fontsize=16)
# ylabel(r'$I$, деления',fontsize=16)
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')
# minorticks_on()
# savefig(path.abspath('..'+'\\fig\\res96V_1.pdf'))

# figure('Uрез=96В,2')
# plot(3*df['Uотр, В/3'],df['lambda, cm'],'*')
# xlabel(r'$U_{\text{отр}}$, \text{В}',fontsize=16)
# ylabel(r'$\lambda$, см',fontsize=16 )
# ylim((10,11))
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')
# minorticks_on()
# savefig(path.abspath('..'+'\\fig\\res96V_2.pdf'))

# df=read(rec, sheet_name='Uрез=120В')

# figure('Uрез=120В,1')
# x=3*array(df['Uотр, В/3'])
# y=array(df['I, mA'])
# g = interpolate.interp1d(x,y, 'cubic')
# x=linspace(0,x[-1],1000)
# y=g(x)
# # plot(x,y)
# plot(3*df['Uотр, В/3'],df['I, mA'],'*')
# xlabel(r'$U_{\text{отр}}$, \text{В}',fontsize=16)
# ylabel(r'$I$, деления',fontsize=16)
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')
# minorticks_on()
# savefig(path.abspath('..'+'\\fig\\res120V_1.pdf'))

# figure('Uрез=120В,2')
# plot(3*df['Uотр, В/3'],df['lambda, cm'],'*')
# xlabel(r'$U_{\text{отр}}$, \text{В}',fontsize=16)
# ylabel(r'$I$, деления',fontsize=16)
# ylim((10,11))
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')
# minorticks_on()
# savefig(path.abspath('..'+'\\fig\\res120V_2.pdf'))


df=read(rec, sheet_name='Uотр=3В')

# figure('Uотр=3В,1')
plot(3*df['Uрез, В/3'],df['I, mA'],'*')
xlabel(r'$U_{\text{рез}}$, \text{В}',fontsize=16)
ylabel(r'$I$, деления',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# savefig(path.abspath('..'+'\\fig\\ref3V_1.pdf'))

# # figure('Uотр=3В,2')
# plot(3*df['Uрез, В/3'], df['lambda, cm'],'*')
# xlabel(r'$U_{\text{рез}}$, \text{В}',fontsize=16)
# ylabel(r'$\lambda$, см',fontsize=16 )
# ylim((10.5,10.6))
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')
# minorticks_on()
# savefig(path.abspath('..'+'\\fig\\ref3V_2.pdf'))


df=read(rec, sheet_name='Uотр=19.5В')

# figure('Uотр=19.5В,1')
plot(3*df['Uрез, В/3'],df['I, mA'],'*')
xlabel(r'$U_{\text{рез}}$, \text{В}',fontsize=16)
ylabel(r'$I$, деления',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# savefig(path.abspath('..'+'\\fig\\ref19V_1.pdf'))

# figure('Uотр=19.5В,2')
# plot(3*df['Uрез, В/3'], df['lambda, cm'],'*')
# xlabel(r'$U_{\text{рез}}$, \text{В}',fontsize=16)
# ylabel(r'$\lambda$, см',fontsize=16 )
# ylim((10.5,10.6))
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')
# minorticks_on()
# savefig(path.abspath('..'+'\\fig\\ref19V_2.pdf'))

df=read(rec, sheet_name='Uотр=48В')

# figure('Uотр=48В,1')
plot(3*df['Uрез, В/3'],df['I, mA'],'*')
xlabel(r'$U_{\text{рез}}$, \text{В}',fontsize=16)
ylabel(r'$I$, деления',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# savefig(path.abspath('..'+'\\fig\\ref48V_1.pdf'))

# figure('Uотр=48В,2')
# plot(3*df['Uрез, В/3'], df['lambda, cm'],'*')
# xlabel(r'$U_{\text{рез}}$, \text{В}',fontsize=16)
# ylabel(r'$\lambda$, см',fontsize=16 )
# ylim((10.5,10.6))
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')
# minorticks_on()
# savefig(path.abspath('..'+'\\fig\\ref48V_2.pdf'))

# df=read(rec, sheet_name='Uрез=120В, Uотр=48В')
# figure('Uрез=120В, Uотр=48В')
# x=array(df['I,ma'])
# y=array(df['I,дел'])
# # plot(x,y)
# g = interpolate.interp1d(x,y, 'quadratic')
# x=linspace(x[5],x[-1],1000)
# y=g(x)
# xlabel(r'$I$, мА',fontsize=16)
# ylabel(r'$I$, деления',fontsize=16)
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')    
# minorticks_on()
# plot(df['I,ma'],df['I,дел'],'o')
# savefig(path.abspath('..'+'\\fig\\res120Vref48V.pdf'))

# df=read(rec, sheet_name='Uрез=12В, Uотр=19.5В')
# figure('Uрез=120В, Uотр=19.5В')
# minorticks_on()
# g = interpolate.interp1d(x,y, 'cubic')
# x=linspace(x[6],x[-2],1000)
# y=g(x)
# # plot(x,y)
# xlabel(r'$I$, мА',fontsize=16)
# ylabel(r'$I$, деления',fontsize=16)
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')    
# plot(df['I,ma'],df['I,дел'],'o')
# savefig(path.abspath('..'+'\\fig\\res120Vref19V.pdf'))

# df=read(rec, sheet_name='Uрез=12В, Uотр=3В')
# figure('Uрез=120В, Uотр=3В')

# g = interpolate.interp1d(x,y, 'cubic')
# x=linspace(x[0],x[-1],1000)
# y=g(x)
# # plot(x,y)
# plot(df['I,ma'],df['I,дел'],'o')
# x=array(df['I,ma'])
# y=array(df['I,дел'])
# xlabel(r'$I$, мА',fontsize=16)
# ylabel(r'$I$, деления',fontsize=16)
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')    
# minorticks_on()
# savefig(path.abspath('..'+'\\fig\\res120Vref3V.pdf'))
show()