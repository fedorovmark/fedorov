from matplotlib import pyplot
import matplotlib.ticker as ticker
import numpy
with open('settings.txt', 'r') as f:
    settings = [float(i) for i in f.read().split('\n')]
data = numpy.loadtxt('data.txt', dtype = int)
data = data*settings[1]
data_time = numpy.array([i/settings[0] for i in range(data.size)])

fig, ax = pyplot.subplots(figsize = (16, 10), dpi = 100)
ax.set_title('Process zaryadki i razryadki kondencatora')
ax.axis([data.min(), data_time.max()+1, data.min(), data.max()+0.2])

time_of_zaryadka = round(data_time[numpy.argmax(data)], 2)
time_of_razryadka = round(data_time[-1] - time_of_zaryadka, 2)
box_1 = {'facecolor':'black',    #  цвет области
       'edgecolor': 'red',     #  цвет крайней линии
       'boxstyle': 'round'} 

ax.text(300, 2.5, 'zar = ' + str(time_of_zaryadka) + '\n' + 'razr = ' + str(time_of_razryadka),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 20)




ax.grid(which = 'major', color = 'b')
ax.minorticks_on()
ax.grid(which = 'minor', color = 'g', linestyle = ':')
ax.set_xlabel('vremya, s')
ax.set_ylabel('napryazhenie, v')
ax.plot(data_time[0:data.size:20], data[0:data.size:20], c = 'black', linewidth = 1, label = 'V(t)')
ax.scatter(data_time[0:data.size:1000], data[0:data.size:1000], marker = '.', c = 'blue', s = 100)
ax.legend(shadow = False, loc = 'right', fontsize = 30)
fig.savefig('graph.png')
fig.savefig('graph.svg')