# author: Rafael Coelho Monte Alto
# advisor: Prof. Dr. Vander Freitas  
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
            # i.print()
    return airports

def readAirline(filename):
    airline = []
    active = []
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
            active.append(int(split[0]))
            for j in range(it):
                tupla = (split[0], split[j+2])
                airline.append(tupla)
    # print(active)
    return airline, active

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

from create import createGraph, createAir
from plot import plotGraph

def main():
    filename = 'input/airports.txt'
    airports = readAirports(filename)
    filenames = ['input/air-france.txt', 'input/british.txt', 'input/lufthansa.txt']
    layers = []
    active_airports = []
    for i in filenames:
        a, b = readAirline(i)
        layers.append(a)
        active_airports.append(b)

    # print(active_airports[0][0])
    # print(type(active_airports[0][0]))
    matrix = [[]]
    # mg, node_color = createGraph(len(layers), 450, 3)
    mg, node_color = createAir(len(layers), 450, active_airports, matrix)
    plotGraph(mg, node_color)
    return 

if __name__ == "__main__":
    main()
