import csv

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


def buildGraph(people, appearances, teams):
    d = {}
    g = Graph()
    peopleL = {}    # people list as a dictionary
    appearancesL = []   # appearances list as a list
    
    wfile = open(appearances,'r')
    print()
    print()

    # open appearances
    with open(appearances, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            appearancesL.append({"playerID":row["playerID"], "teamID":row["teamID"], "yearID":row["yearID"]})
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1  
            line_count += 1
        print(f'Processed {line_count} lines.')
    #print (appearancesL)

    # open people
    with open(people, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            peopleL[row["playerID"]] = row["nameFirst"] + " " + row["nameLast"]
            g.addVertex(row["playerID"])
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1  
            line_count += 1
        print(f'Processed {line_count} lines.')
    #print (peopleL)

    # add vertices and edges for related players 
    line_count = 0
    for playerA in appearancesL:
        for playerB in appearancesL:
            if playerA["teamID"] == playerB["teamID"] and playerA["yearID"] == playerB["yearID"] and playerA["playerID"] != playerB["playerID"]:
                g.addEdge(playerA["playerID"], playerB["playerID"], playerA["teamID"])
    
    return g


g = buildGraph('people.csv.txt', 'appearances.csv.txt', 'teams.csv.txt')


print(g)
