import networkx as nx

num_forests, num_years = int(input()), int(input())
delta = [ int(input()) for _ in range(num_years) ]
tau = [ int(input()) for _ in range(num_forests) ]
w = [ [ int(input()) for _ in range (num_years) ] for _ in range(num_forests) ]
u = [ int(input()) for _ in range(num_years) ]

g = nx.DiGraph()

for forest in range(num_forests):
	g.add_edge('s', 'num_forests%d' % (forest), capacity=tau[forest])
	for year in range(num_years):
		g.add_edge('num_years%d' % (year), 't', capacity=u[year])
		g.add_edge('num_forests%d' % (forest), 'w%d_%d' % (forest,year), capacity=w[forest][year])
		for z in range(delta[year]):
			g.add_edge('w%d_%d' % (forest,year), 'num_years%d' % (year+z),  capacity=w[forest][year])

flow = nx.algorithms.flow.maxflow.maximum_flow(g, 's', 't')
print(flow[0])