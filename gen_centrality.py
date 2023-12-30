import os
import snap
import sys
Rnd = snap.TRnd(42)
Rnd.Randomize()
# create “centralities” folder to store all output
os.makedirs('centralities',exist_ok=True)
# create Graph from given edgelist passed through the termial
G = snap.LoadEdgeList(snap.PUNGraph,sys.argv[1], 0, 1)


# funtion to compute the closeness centrality
def closeness_centrality(G):
    # formulato compute closeness centrality for each node = ci=(n-1)/summation(dij) -> dij is shortest length from i to j
    closeness={}
    for i in G.Nodes():
        vertex_id=i.GetId()
        # using bfs ro find the shortest path from node i to all other node
        path={vertex_id:0} 
        queue=[vertex_id]
        while(queue):
            node=queue.pop(0)
            for adjacent in G.GetNI(node).GetOutEdges():
                if(adjacent not in path):
                    path[adjacent]=path[node]+1
                    queue.append(adjacent)
        # compute the sum paths from source node to all other nodes
        path_length=sum(path.values())
        # if it is more then 0 then compute the closeness centrality using the  formula for each node
        if(path_length>0):
            closeness[vertex_id]=(G.GetNodes()-1)/path_length
        else:
            closeness[vertex_id]=0
    return closeness
# compute the Betweenness centrality
def betweenness_centrality(G):
    # formulato compute closeness centrality for each node = ci=(n-1)/summation(dij) -> dij is shortest length from i to j
    betweenness={}
    # initalise every vertex betweenness as 0
    for i in G.Nodes():
        betweenness[i.GetId()]=0.0
    for i in G.Nodes():
        for j in G.Nodes():
            for k in G.Nodes():
               if(i.GetId()!=j.GetId() and j.GetId()!=k.GetId() and k.GetId()!=i.GetId() and G.IsEdge(i.GetId(),j.GetId()) and G.IsEdge(i.GetId(),k.GetId())):
                   betweenness[i.GetId()]+=1
                   betweenness[i.GetId()]+=betweenness[j.GetId()]*betweenness[k.GetId()]
    for i in G.Nodes():
        betweenness[i.GetId()] = betweenness[i.GetId()]/2
    return betweenness
# compute page rank 


def biased_page_rank(G):
    pass



# compute the number of influencers



# compute and save the closeness centrality
closeness=closeness_centrality(G)
with open('centralities/closeness.txt','w') as f:
    for i in sorted(closeness.items(),key=lambda x:x[1],reverse=True):
        f.write(f"{i[0]} {i[1]:.6f}\n")
# compute and save the betweenness centrality
between_ness=betweenness_centrality(G)
with open('centralities/betweenness.txt','w') as f:
    for i in sorted(between_ness.items(),key=lambda x:x[1],reverse=True):
        f.write(f"{i[0]} {i[1]:.6f}\n")
# compute and save the biased pagerank 
"""
page_rank=closeness_centrality(G)
with open('centralities/pagerank.txt','w') as f:
    for i,j in page_rank.items():
        f.write(f"{i} {j:.6f}\n")
"""
#

