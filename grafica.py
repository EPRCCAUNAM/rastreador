import matplotlib.pyplot as plt

class graph():
    def __init__(self, filename, colX, colY):
        self.filename = filename
        self.colX = colX
        self.colY = colY
        self.graphData()

    def graphData(self):
        data= getData(self.filename, self.colY,self.colX)
        plt.plot(data.dataX, data.dataY, 'ro')
        plt.show()

class getData():
    '''get data from a file, end of line is \n'''
    def __init__(self, filename, colY, colX=None, sep=','):
        self.filename = filename
        #colX and colY (int)
        self.colY = colY
        self.colX = colX
        self.end = '\n'
        self.sep = sep
        self.get()

    def get(self):
        myfile = open(self.filename, 'r')
        data = myfile.readlines()
        data_row=[]
        #data list
        data_X=[]
        data_Y=[]
        for row in data:
            dataE=False
            #remove end of line
            row.replace(self.end,'')
            #column separate
            data_row.append(row.split(self.sep))
            #delete not numeric rows
            try:
                data_X.append( float(data_row[-1][self.colX]))
            except:
                dataE=True
            if dataE == False:
                try:
                    data_Y.append(float(data_row[-1][self.colY]))
                except:
                    data_X.pop()
        self.dataX= data_X
        self.dataY= data_Y
        



