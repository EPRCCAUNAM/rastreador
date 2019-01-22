from grafica import graph
from grafica import getData
import matplotlib.pyplot as plt

class newgraph(graph):
    def graphData(self):
        data = getData(self.filename, self.colY, self.colX)
        plt.plot(data.dataX, data.dataY,
                #line
                #'r--',
                )
        plt.axis([0,640,480,0])
        plt.show()

g=newgraph('solar2.cca', 1,2)
