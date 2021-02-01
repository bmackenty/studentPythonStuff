"""
This program creates a three dimension array which
represents a non-directional weighted graph of N nodes.

This program was written to help test Dykstra's best path algorithm
and other path finding algorithms. 

This code is not yet ready for release. 
"""
import random

def copy(lToo, lFrom):
    while len(lToo) < len(lFrom):
        lToo.append([0,0])
    for x in range(0, len(lFrom)):
        for y in range(0, len(lFrom[x])):
            lToo[x][y]=lFrom[x][y]
            lToo[x][y] = lFrom[x][y]

nodes = input("How many nodes do you want? ")
connections = input("What are the maximum number of connected nodes? ")
weightC = int(input("Whats the maximum weight between the nodes? "))
numberOfConnectedNodes = 1

counter = 0
new_graph = []

# we start by just creating a simple list of N .
while counter < int(nodes):
    new_graph.append([])
    counter += 1

# now we will add connections to each node:
for counter in range(0, int(nodes)):
    buildRandomConnections = []
    copy(buildRandomConnections, new_graph[counter])
    numberOfRandomConnections = random.randint(1, int(connections)-1)
    while len(buildRandomConnections)<=numberOfRandomConnections:
        aRandomNode = random.randint(1, int(nodes))
        weight = random.randint(1, weightC)
        # this prevents nodes looping to themselves
        # this horribly ugly code prevents duplicate values in the same node.
        repeat = True
        while repeat:
            repeat = False
            for x in range(0, len(buildRandomConnections)):
                if aRandomNode == buildRandomConnections[x][0]:
                    repeat=True
                    aRandomNode = random.randint(1, int(nodes))
            while counter+1 == aRandomNode:
                aRandomNode = random.randint(1, int(nodes))
                repeat = True

        if len(new_graph[aRandomNode-1])<int(connections):
            buildRandomConnections.append([aRandomNode, weight])
            new_graph[aRandomNode-1].append([counter+1, weight])

    copy(new_graph[counter], buildRandomConnections)


counter=1
for x in range(0, len(new_graph)):
    print("Node",x+1,":",new_graph[x])

for x in range(0, len(new_graph)):
    if len(new_graph[x])>int(connections):
        print("To big:",counter," Length:",len(new_graph[x]))
    counter += 1

print(new_graph)   
