import networkx as nx 

g = nx.read_edgelist('dolphins.edges')
print(g.number_of_nodes())
print(g.number_of_edges())
nx.write_gml(g, 'dolphins.gml')