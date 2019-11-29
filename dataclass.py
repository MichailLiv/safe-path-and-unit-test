import numpy as np
class DataClass:

    def __init__(self):
        self.name = '.txt'



    def Read(self, name):
        self.name = name + self.name #import text file name
        f = open(self.name, "r")
        inputs = f.read()
        input_values = inputs.split('\n')

        x = np.array(list(map(float, input_values[0].split()))) #the first number is Zearth
        self.n = int(input_values[1])#number of additional destinations
        self.input_information = {}
        self.input_information['0'] = np.zeros(3)  # This is Earth
        self.names = ['0']

        for i in range(self.n):
            coordinates = input_values[i + 2].split()#
            node_data = np.array(list(map(float, coordinates)))
            self.names.append(str(i + 1))
            self.input_information[str(i + 1)] = node_data

        self.names.append(str(self.n + 1))
        self.input_information[str(self.n + 1)] = x  # This is Zearth

        self.names = tuple(self.names)