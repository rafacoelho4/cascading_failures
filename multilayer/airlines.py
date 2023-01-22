# author: Rafael Coelho Monte Alto
# advisor: Prof. Dr. Vander Luis 
# 2022/2023

# Appling cascading failures to real networks

def readAirports(filename):
    with open(filename, 'r') as f:
        airports = []
        while True:
            s = f.readline()
            if not s:
                break
            split = s.split()
            id = int(split[0])
            icao = split[1]
            longitude = split[2]
            latitude = split[3]
            a = Airport(id, icao, longitude, latitude)
            airports.append(a)
        # for i in airports:
        #     i.print()
    return airports

def readAirline(filename):
    airline = []
    with open(filename, 'r') as f:
        s = f.readline()
        active_nodes = int(s)
        # blank line
        _ = f.readline()
        for _ in range(active_nodes):
            s = f.readline()
            if not s:
                break
            split = s.split()
            it = int(split[1])
            for j in range(it):
                tupla = (split[0], split[j+2])
                airline.append(tupla)
    return airline

class Airport:
    def __init__(self, id, icao, longitude, latitude):
        self.id = id
        self.icao = icao
        self.longitude = longitude
        self.latitude = latitude

    def print(self):
        print("Airport:", self.id, self.icao, self.longitude, self.latitude)
    
    def print_array(array):
        for a in array: 
            a.print()

from create import createGraph
from plot import plotGraph

def main():
    filename = 'input/airports.txt'
    airports = readAirports(filename)
    filenames = ['input/air-france.txt', 'input/british.txt', 'input/lufthansa.txt']
    layers = []
    for i in filenames:
        a = readAirline(i)
        layers.append(a)
    
    mg, node_color = createGraph(len(layers), 450, 3)
    plotGraph(mg, node_color)
    return 

if __name__ == "__main__":
    main()
