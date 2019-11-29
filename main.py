import numpy as np
from Find_Max_Path import Graph
from dataclass import DataClass

#Read data
inputs=DataClass()
inputs.Read('data')

#Initialize graph
g=Graph()
#Initialize nodes on the graph
g.set_node_names(inputs.names)

#This can be used to reduce computation to reduce the number of connected nodes that are defined, however it is preferred not to,
#because the weight in the graph might be chosen to be defined differently
#visited=[]

for i in range(0,inputs.n+2):
  for j in range(0,inputs.n+2):

    #visited.append(i)
    if j !=i :
      calculate_risk= np.linalg.norm (inputs.input_information[str(i)]-inputs.input_information[str(j)] )
      #insert edge betweem two nodes along with the corresponding weight
      g.insert_edge(calculate_risk, int(i), int(j))
    else:
      continue


import pprint
pp = pprint.PrettyPrinter(indent=2)

print ("Edge List")
pp.pprint(g.get_edge_list_names())

print ("\nAdjacency List")
pp.pprint(g.get_adjacency_list_names())

print ("\nAdjacency Matrix")
pp.pprint(g.get_adjacency_matrix())


print ("\nBest Path and maximum distance in safest path")
pp.pprint(g.dijkstar_output(0))
