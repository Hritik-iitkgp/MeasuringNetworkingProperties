import snap
import os
import sys
Rnd = snap.TRnd(42)
Rnd.Randomize()

os.makedirs('plot',exist_ok=True)
G = snap.LoadEdgeList(snap.PUNGraph,sys.argv[1], 0, 1)
#print size of network
print("Number of nodes:", G.GetNodes())
print("Number of edges:", G.GetEdges())
# degree of node in network
print("Number of nodes with degree=7:",sum([1 for i in G.Nodes() if i.GetDeg()==7]))
highest_node=[]
high_degree=float('-inf')
for i in G.Nodes():
    if i.GetDeg()>high_degree:
        high_degree=i.GetDeg()
        highest_node=[i]
    elif(i.GetDeg()==high_degree):
        highest_node.append(i)
print("Node id(s) with highest degree:",",".join([str(i.GetId()) for i in G.Nodes() if i.GetDeg()==high_degree]))
#plot
#plot=os.path.join('plot','deg_dist_')
#G.PlotInDegDistr('deg_dist_','Plot of the Degree distribution')

# path in network
# 3. Paths in the Network
approx_full_diameter = snap.GetBfsFullDiam(G, 1000)
print("Approximate full diameter:", approx_full_diameter)

approx_effective_diameter = snap.GetBfsEffDiam(G, 1000)
print("Approximate effective diameter:", round(approx_effective_diameter,4))
# 4. Components of the Network
MxWcc = snap.GetMxWcc(G)
fraction_largest_component = MxWcc.GetNodes() / float(G.GetNodes())
print("Fraction of nodes in largest connected component:", round(fraction_largest_component,4))

#num_edge_bridges = snap.CntNonTreeEdges(MxWcc)
#print("Number of edge bridges:", num_edge_bridges)

#num_articulation_points = snap.CntArtPoints(MxWcc)
#print("Number of articulation points:", num_articulation_points)

# 5. Connectivity and Clustering
average_clustering_coeff = snap.GetClustCf(G)
print("Average clustering coefficient:", round(average_clustering_coeff,4))

num_triads = snap.GetTriads(G)
print("Number of triads:", num_triads)

random_node_id = G.GetRndNId()
clustering_coeff_random_node = snap.GetNodeClustCf(G, random_node_id)
print("Clustering coefficient of random node (ID {}):".format(random_node_id), round(clustering_coeff_random_node,4))

num_triads_random_node = snap.GetNodeTriads(G, random_node_id)
print("Number of triads random node participates (ID {}):".format(random_node_id), num_triads_random_node)

# 6. Centrality Metrics
# Degree Centrality
deg_centrality = snap.TIntFltH()
snap.GetNodeInDegCentr(G, deg_centrality)
top_deg_centrality = deg_centrality.SortByDat(False)[:5]
print("Top 5 nodes by degree centrality:")
for item in top_deg_centrality:
    print("Node ID:", item, "Degree Centrality:", top_deg_centrality[item])

# Closeness Centrality
closeness_centrality = snap.TIntFltH()
snap.GetNodeClCf(G, closeness_centrality)
top_closeness_centrality = closeness_centrality.SortByDat(False)[:5]
print("Top 5 nodes by closeness centrality:")
for item in top_closeness_centrality:
    print("Node ID:", item, "Closeness Centrality:", top_closeness_centrality[item])

# Betweenness Centrality
betweenness_centrality = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(G, betweenness_centrality, Edges, 1.0)
top_betweenness_centrality = betweenness_centrality.SortByDat(False)[:5]
print("Top 5 nodes by betweenness centrality:")
for item in top_betweenness_centrality:
    print("Node ID:", item, "Betweenness Centrality:", top_betweenness_centrality[item])

#print(highest_node[len(highest_node)-1].GetId())
"""
# create a folder called 'plot'

#output file for facebooklist
facebook=os.path.join('subgraph', 'facebook.elist')
G = snap.LoadEdgeList(snap.PUNGraph, 'facebook_combined.txt', 0, 1)
# list of node IDs which is not divisible by 5
node_divisible_5=[i.GetId() for i in G.Nodes() if i.GetId()%5==0]
subgraph = snap.GetSubGraph(G,node_divisible_5)
snap.SaveEdgeList(subgraph, facebook)
#output file for twitterlist
twitter=os.path.join('subgraph', 'twitter.elist')
G = snap.LoadEdgeList(snap.PUNGraph, 'twitter_combined.txt', 0, 1)
not_divisible_3=[i.GetId() for i in G.Nodes() if i.GetId()%3!=0]
subgraph = snap.GetSubGraph(G, not_divisible_3)
snap.SaveEdgeList(subgraph, twitter)
"""

