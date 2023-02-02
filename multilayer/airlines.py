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
                tupla = (int(split[0]), int(split[j+2]))
                airline.append(tupla)
    # print(active)
    return airline, active

class Airport:
    def __init__(self, id, icao, longitude, latitude):
        self.id = int(id)
        self.icao = icao
        self.longitude = float(longitude)
        self.latitude = float(latitude)

    def print(self):
        print("Airport:", self.id, self.icao, self.longitude, self.latitude)
    
    def print_array(array):
        for a in array: 
            a.print()

from create import createAir
from plot import plotGraph
from cascade import cascade 
from style import FIGURE

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
    
    total_layers = len(layers) 
    total_nodes = len(airports) 
    node_size = [] 
    for i in range(total_layers): 
        for j in range(total_nodes): 
            if (j in active_airports[i]): 
                node_size.append(FIGURE["node_size"]) 
            else: 
                node_size.append(0) 

    custom_pos = {} 
    for i in range(total_nodes): 
        custom_pos[i] = [airports[i].latitude, airports[i].longitude/30] 

    mg, node_color = createAir(total_layers, total_nodes, active_airports, layers) 
    plotGraph(mg, node_color, node_size=node_size, node_position=custom_pos) 
    mg = cascade(mg, node_color, phi=0.36)
    return 

if __name__ == "__main__":
    main()
