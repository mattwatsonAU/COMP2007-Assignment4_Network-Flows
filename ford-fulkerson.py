# this is a simple script to print a graph's maximum flow
# you can pipe the output of your pre-processing script to this
# script if you don't want to run ford-fulkerson in your script
# flow is computed between vertex 0 and vertex n-1

# expected input format:
# n
# m
# vertexId vertexId capacity
# vertexId vertexId capacity
# ...
# vertexId vertexId capacity

import networkx as nx

g = nx.DiGraph()

n, m = int(input()), int(input())

for i in range(n):
	g.add_node(i)

for _ in range(m):
	a, b, c = [ int(i) for i in input().split(' ') ]
	g.add_edge(a, b, capacity=c)
	
max_flow = nx.algorithms.flow.maxflow.maximum_flow(g, 0, n-1)[0]
print(max_flow)
