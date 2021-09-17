#!/usr/bin/python3


from CS312Graph import *
import time


def insert_val(array, value):
    index = 0

    for x in range(len(array)):
        if array[x].length < value.length:
            index = x

    stor = value

    if array != []:
        if (index == 0 and value.length < array[0].length):
            for y in range(len(array)):
                stor2 = array[y]
                array[y] = stor
                stor = stor2

        else:
            for y in range(len(array)):
                if y <= index:
                    x = x
                else:
                    stor2 = array[y]
                    array[y] = stor
                    stor = stor2

    array.append(stor)


def delete_min(array):
    node = array[0]
    array.remove(array[0])
    return node

network_list = []

def initialize_networklist(rows, cols):
    network_list = [[0] * cols] * rows

def get_networklist():
    return network_list

class NetworkRoutingSolver:
    def __init__( self):
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath( self, destIndex ):
        self.dest = destIndex
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        path_edges = []
        total_length = 0
        node = self.network.nodes[self.dest]
        print(node)
        counter = 3

        while (counter > 0):

            total_length = total_length + network_list[node.node_id][1]

            back_node = self.network.nodes[network_list[node.node_id][2]]
            forward_node = node

            edge = forward_node.neighbors[0]

            for ab in range(3):
                if forward_node.neighbors[ab] == back_node:
                    edge = forward_node.neighbors[ab]

            path_edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))

            node = forward_node

            counter = counter -1

        #edges_left = 3
        #while edges_left > 0:
         #   edge = node.neighbors[2]
          #  path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
           # total_length += edge.length
            #node = edge.dest
            #edges_left -= 1
        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths( self, srcIndex, use_heap=False ):

        val = 0

        for q in range(len(self.network.nodes)):
            val += 1

        #print(val)
        #network_list = []

        #network_list = [len(self.network.nodes)][3]

        self.source = srcIndex
        t1 = time.time()

        node = self.network.nodes[self.source]

       #visit the unvisited vertex with the smallest known distance from the starting vertex

        visited_nodes = []
        unvisited_nodes = []

        for k in range(val):
            unvisited_nodes.append(self.network.nodes[k])


        #print(len(unvisited_nodes))

        it = 10000000000000000000000000
        for m in range(len(unvisited_nodes)):
            print(m)
            network_list.append([m, it, m])

        for j in range(len(unvisited_nodes)-1):
            edge_list = []
            for a in range(3):
                insert_val(edge_list, node.neighbors[a])

            id = edge_list[0].dest.node_id
            if edge_list[0].length < network_list[id][1]:
                network_list[id][1] = (edge_list[0].length)
                network_list[id][2] = node.node_id

            id2 = edge_list[1].dest.node_id
            if (edge_list[1].length) < network_list[id2][1]:
                network_list[id2][1] = (edge_list[1].length )
                network_list[id2][2] = node.node_id


            id3 = edge_list[2].dest.node_id
            if edge_list[2].length < network_list[id3][1]:
                network_list[id3][1] = (edge_list[2].length )
                network_list[id3][2] = node.node_id

            delete_min(unvisited_nodes)
            node = unvisited_nodes[0]

            print(network_list)

        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        t2 = time.time()
        return (t2-t1)