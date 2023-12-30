import snap
import os
Rnd = snap.TRnd(42)
Rnd.Randomize()
# create a folder called 'subgraph'
os.makedirs('subgraph',exist_ok=True)
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
# create a random Graph with 1000 node and 50000 edges
G=snap.TUNGraph.New()
# add 1000 nodes in it
for i in range(1000):
    G.AddNode(i)
# add 50000 edges
while(G.GetEdges() < 50000):
    # v1 and v2 are two random node to add edge between them
    v1=Rnd.GetUniDevInt(0,1000)
    v2=Rnd.GetUniDevInt(0,1000)
    if(not G.IsEdge(v1,v2) and v1!=v2):
        G.AddEdge(v1,v2)
# store the  Graph 
snap.SaveEdgeList(subgraph, "random.elist")
# create a Small world graph with 1000 nodes , node degree and rewire probability =0.6
#create a complete graph with 1000 nodes
G=snap.GenFull(snap.PUNGraph,1000)
# add rewiring probality as 0.6
snap.Rewiring(G,0.6)
#ensure that each node have the required node degree
for i in G.Nodes():
    while(i.GetOutDeg() <50):
        # find a random node and add edge between the present node and random node
        # untill its degree is 50
        v2=Rnd.GetUniDevInt(0,1000)
        if(not G.IsEdge(i.GetId(),v2) and i.GetId()!=v2):
            G.AddEdge(i.GetId(),v2)
# store the  Graph 
snap.SaveEdgeList(subgraph, "smallworld.elist")
