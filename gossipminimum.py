from threading import Lock, Thread
import math
import timeit
import json
import os
import random
import socket
from threading import Thread
import time
from enum import Enum
import sys

import grpc
import ast

sys.path.append('./proto')
sys.path.append('./service')
import grpc
from proto import fileService_pb2, fileService_pb2_grpc

import time
import math
import cache
from threading import Lock, Thread
import collections
import numpy as np


class GossipProtocol:
    capacity_of_neighbors_fixed = [1200, 3100, 7000, 5558]  # maintains the list of nodes
    totalNodes = [1234, 3456, 7899, 7543]
    sys.setrecursionlimit(200000)
    localMinimumCapacity = -sys.maxsize - 1
    IPaddress = "169.105.246.3"
    localPort = 21000
    local_message = None
    bufferSize = 1024
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Bind to address and ip
    UDPServerSocket.bind((IPaddress, localPort))
    blacklisted_nodes = []
    minimum_IP = None
    minimum_Capacity = None
    listofNeighbors = []
    path = ["(0,0)", "(0,1)", "(0,2)"]
    counter = 1


    def __init__(self):
        self.initiateReplication()
        # self.start_threads()

    def input_message(self):
        message_to_send = "message"

    def checkforConvergence(self, data, BlackListedNodes):
        print("data = ", data)
        message_received = data.get("Dictionary")
        print(self.blacklisted_nodes)
        print("MG-", message_received)
        print("LM", self.local_message)

        if BlackListedNodes == None:
            if self.local_message == message_received:
                print("COUNTER =", self.counter)
                self.counter += 1
                if self.counter >= 5:
                    BlackListedNodes = []
                    BlackListedNodes.append(self.IPaddress)
                    listofNeighbors = self.fetch_all_neighbors()
                    print("listofNeighbors", listofNeighbors)
                    print("BL NODES = ", BlackListedNodes)
                    for ip in range(len(listofNeighbors)):
                        if ip in BlackListedNodes:
                            continue
                        else:
                            BlackListedNodes.append(listofNeighbors[ip])
                    if len(BlackListedNodes) >= 4:
                        print("CAME HERE-111")
                        self.counter = 1
                        return True
                    self.blacklisted_nodes = BlackListedNodes
                return False
            else:
                self.local_message = message_received
                self.counter = 1
                self.blacklisted_nodes = BlackListedNodes
                return False

        if BlackListedNodes != None:
            if self.local_message == message_received:
                self.counter += 1
                if self.counter >= 5:
                    print("Final Msg : ", message_received)
                    if self.IPaddress not in BlackListedNodes:
                        BlackListedNodes.append(self.IPaddress)
                    print("listofNeighbors", self.listofNeighbors)
                    listofNeighbors = self.fetch_all_neighbors()
                    for ip in range(len(listofNeighbors)):
                        if ip in BlackListedNodes:
                            continue
                        else:
                            BlackListedNodes.append(listofNeighbors[ip])
                    print("NEW BL", BlackListedNodes)
                    # if len(self.blacklisted_nodes) >= 0.75 * len(self.totalNodes):
                    if len(BlackListedNodes) >= 4:
                        print("CAME HERE-222")
                        self.counter = 1
                        return True
                self.blacklisted_nodes = BlackListedNodes
                return False
            else:
                self.local_message = message_received
                self.counter = 1
                self.blacklisted_nodes = BlackListedNodes
                return False

    def updated_message_util(self, data, minimum_capacity, leastUsedIP, gossip_phase, BlackListedNodes):
        # update message
        print("DATA = ", leastUsedIP)
        Dictionary = {self.minimum_IP: self.minimum_Capacity}
        Dict = data.get("Dictionary")
        IPaddress = data.get("IPaddress")
        gossip = gossip_phase
        return IPaddress, gossip, Dictionary

    def find_minimum_in_dictionary(self, dictionary):
        result = []
        min_value = None
        print("SICT = ", dictionary)
        mini = min(dictionary, key=lambda k: dictionary[k])
        print("MINIMUM = ", [mini, dictionary[mini]])
        self.minimum_IP = mini.strip('\n')
        self.minimum_Capacity = dictionary[mini]
        return [mini.strip('\n'), dictionary[mini]]

    def fetch_all_neighbors(self):
        list_of_neigbors = []
        filepath = 'data/neighbors.txt'
        with open(filepath, "r") as ins:
            for line in ins:
                print(line)
                line = line.strip('\n')
                list_of_neigbors.append(line)

        return list_of_neigbors

    def get_minimum_capacity_neighbors(self, initalReplicaServer):
        list_of_neigbors = []
        capacity_of_neighbors = { self.IPaddress : 7939 }
        filepath = 'data/neighbors.txt'
        with open(filepath, "r") as ins:
            for line in ins:
                print(line)
                line = line.strip('\n')
                list_of_neigbors.append(line)
        counter = 0
        self.listofNeighbors = list_of_neigbors
        if initalReplicaServer in list_of_neigbors:
            list_of_neigbors.remove(initalReplicaServer)
        while len(list_of_neigbors) > 0:
            print("number of neighbours: ",len(list_of_neigbors))
            
            forwardIP = random.choice(list_of_neigbors)
            print("SENDING NEXT TO = ", forwardIP)
            hostname = str.encode(forwardIP)
            hostname2 = forwardIP

            print("HOSTNAME = ", hostname2, "INT REPL =", initalReplicaServer)
            if hostname2 != initalReplicaServer:
                print("ping -c 1 " + hostname.decode("utf-8"))
                response = os.system("ping -c 1 " + hostname.decode("utf-8"))
                # and then check the response
                if response == 0:
                    print(hostname, 'up')
                    # Call to check capacity
                    if hostname2 == "169.105.246.3":
                        coordinates = "(0,1)"
                    elif hostname2 == "169.105.246.6":
                        coordinates = "(1,1)"
                    else:
                        coordinates = "(-1,0)"

                    print("GET COORDINATES CAP OF", coordinates)
                    IPaddress, capacity = self.getneighborcapacity(coordinates)
                    print("GET CAPACITY OF NEIGHBORS = ", IPaddress, capacity)
                    capacity_of_neighbors[IPaddress] = capacity
                    counter += 1
                    list_of_neigbors.remove(hostname2)
                else:
                    print(hostname, 'down')
                    counter += 1
                    list_of_neigbors.remove(hostname2)

        if len(capacity_of_neighbors) == 0:
            return None
        else:
            print("capacity_of_neighbors = ", capacity_of_neighbors)
            first_minimum = self.find_minimum_in_dictionary(capacity_of_neighbors)
            return [first_minimum[0], first_minimum[1]]

    def receive_message(self):
        while True:
            messageReceived, address = self.UDPServerSocket.recvfrom(1024)
            self.getPath()
            data = json.loads(messageReceived.decode())
            print("GOT DATA ", data, " FROM", address[0])
            IPaddress = data.get("IPaddress")
            gossip_flag = data.get("gossip")
            Dictionary = data.get("Dictionary")
            BlackListedNodes = data.get("BlackListedNodes")

            Convergence_Value = self.checkforConvergence(data, BlackListedNodes)
            print("LOCAL BLACKLISTED", self.blacklisted_nodes, "RECEIVED BLACK LISTED", BlackListedNodes)
            print("LATEST VALUES", IPaddress, gossip_flag, Convergence_Value)
            if str(IPaddress) == "169.105.246.9" and gossip_flag == False:
                # make data.gossip == true
                list_of_neighbors = self.fetch_all_neighbors()
                minimum_capacity_neighbor = self.get_minimum_capacity_neighbors(IPaddress)
                max_size = sys.maxsize
                print("minimum_capacity_neighbor - ", minimum_capacity_neighbor)
                minimum_capacity = min(minimum_capacity_neighbor[1], max_size)
                self.counter = 1
                print("------------", minimum_capacity, minimum_capacity_neighbor[0], "------------")
                IPaddress, gossip, Dictionary = self.updated_message_util(data, minimum_capacity,
                                                                          minimum_capacity_neighbor[0], True)
                for ip in range(len(list_of_neighbors)):
                    response = os.system("ping -c 1 " + list_of_neighbors[ip].strip('\n'))
                    if response == 0:
                        BlackListedNodes = self.blacklisted_nodes
                        IPaddressOne = list_of_neighbors[ip].strip('\n')
                        print("SENDING----------", IPaddressOne, IPaddress, True, Dictionary, BlackListedNodes)
                        self.transmit_message(IPaddressOne, IPaddress, True, Dictionary, BlackListedNodes)
                    else:
                        continue
                time.sleep(6)
                # self.replicateData()
            # bestnode_coordinates = self.get_best_node()
            # path =  self.bfs(self.grid,self.coordinates, bestnode_coordinates)
            # print("PATH to next replica" , path)
            # get_next_ip = self.get_next_ipaddress(path,self.coordinates)
            # make a grpc call to send data to nodes ( DATA to be written to memory, path)
            # self.replicateData()
            elif gossip_flag == True and Convergence_Value == False:
                print("IN ELIF")
                list_of_neighbors = self.fetch_all_neighbors()
                minimum_capacity_neighbor = self.get_minimum_capacity_neighbors(IPaddress)
                print("MINIMUM of minimum_capacity_neighbor", minimum_capacity_neighbor)
                if minimum_capacity_neighbor != None:
                    dict = data.get("Dictionary")
                    received_minimum_capacity = dict[list(dict.keys())[0]]
                    print("minimum_capacity_neighbor - ", minimum_capacity_neighbor)
                    minimum_capacity = min(minimum_capacity_neighbor[1], received_minimum_capacity)
                    print("------------", minimum_capacity, minimum_capacity_neighbor[0], "------------")
                    print("minimum_capacity_neighbor", minimum_capacity_neighbor[0])
                    print("received_minimum_capacity", received_minimum_capacity)
                    if received_minimum_capacity != minimum_capacity:
                        IPaddress, gossip, Dictionary = self.updated_message_util(data, minimum_capacity,
                                                                                  minimum_capacity_neighbor[0], True)
                    for ip in range(len(list_of_neighbors)):
                        response = os.system("ping -c 1 " + list_of_neighbors[ip].strip('\n'))
                        if response == 0:
                            BlackListedNodes = self.blacklisted_nodes
                            IPaddressOne = list_of_neighbors[ip].strip('\n')
                            print("SENDING----------", IPaddressOne, IPaddress, True, Dictionary, BlackListedNodes)
                            self.transmit_message(IPaddressOne, IPaddress, True, Dictionary, BlackListedNodes)
                        else:
                            continue
                else:
                    for ip in range(len(list_of_neighbors)):
                        response = os.system("ping -c 1 " + list_of_neighbors[ip].strip('\n'))
                        if response == 0:
                            IPaddressOne = list_of_neighbors[ip].strip('\n')
                            BlackListedNodes = self.blacklisted_nodes
                            print("SENDING----------", IPaddressOne, IPaddress, True, Dictionary, BlackListedNodes)
                            self.transmit_message(IPaddressOne, IPaddress, True, Dictionary, BlackListedNodes)
                        else:
                            continue
            elif Convergence_Value == True:
                sys.exit(0)

    def transmit_message(self, hostname, IPaddress, gossip, Dictionary, BlackListedNodes):
        serverAddressPort = (hostname, 21000)
        bufferSize = 1024
        # message = json.dumps(message_to_be_gossiped)
        message = json.dumps(
            {"IPaddress": IPaddress, "gossip": gossip, "Dictionary": Dictionary,
             "BlackListedNodes": self.blacklisted_nodes})
        print("Sending message to", message)
        self.UDPServerSocket.sendto(message.encode(), serverAddressPort)

    # def replicateData()
    # if(self.node == initialReplciateServer)
    #   check node which has minimum memory utilization
    #   call shortestPath function(self_coordinates,set_minimum_coordinates)
    #             returns the path list
    #   initiate a counter
    #   grpc_call(payload(file,counter,(path_list)))
    # else
    #    # unwrap the payload.counter
    #    # if(payload.counter != len(payload.pathlist)-1)
    # payload.counter+1
    # establish GRPC channel between nodes in the pathlist -> grpc_call(payload(file,counter,(path_list)))
    # send data through the channel
    # else
    # replicate the file(write)
    # send acknwoledgment back using same pathlist ()

    def getneighbordata(self, next_node):
        with open('data/metadata.json', 'r') as f:
            metadata_dict = json.load(f)
        nodes = metadata_dict['nodes']
        return nodes[next_node]

    def getneighborcapacity(self, next_node):
        with open('data/metadata.json', 'r') as f:
            metadata_dict = json.load(f)
        nodes = metadata_dict['capacities']
        print("all nodes", nodes[next_node])
        return nodes[next_node][0], nodes[next_node][1]

    def ReplicateFile(self, request, context):
        print("request", request.shortest_path)
        # next_node = request.shortest_path[request.currentpos]
        if request.currentpos == len(request.shortest_path) - 1:
            cache.set(request, request)
            return fileService_pb2.ack( success=True, message="Data Replicated." )
        else:
            # forward_server_addr = self.getneighbordata(next_node)
            forward_server_addr = "169.105.246.6"
            forward_port = 50051
            forward_channel = grpc.insecure_channel(forward_server_addr + ":" + str(forward_port))
            forward_stub = fileService_pb2_grpc.FileserviceStub(forward_channel)
            request.currentpos += 1
            rList = [1, 2, 3, 4, 5]
            arr = bytearray(rList)
            updated_request = fileService_pb2.FileData(initialReplicaServer=request.initialReplicaServer,
                                                       bytearray=request.bytearray, vClock=request.vClock,
                                                       shortest_path=request.shortest_path,
                                                       currentpos=request.currentpos + 1)
            forward_resp = forward_stub.ReplicateFile(updated_request)
            print("forward_resp", forward_resp)
            return fileService_pb2.ack(success=True, message="Data Forwarded.")
    
    def initiateReplication(self):
        serverAddress = "169.105.246.6"
        serverPort = 50051
        rList = [1, 2, 3, 4, 5]
        arr = bytes(rList)
        channel = grpc.insecure_channel(serverAddress + ":" + str(serverPort))
        replicate_stub = fileService_pb2_grpc.FileserviceStub(channel)
        request = fileService_pb2.FileData(initialReplicaServer="169.105.246.4", bytearray=arr,
                                           vClock="My V Clock", shortest_path = self.path, currentpos=0)
        resp = replicate_stub.ReplicateFile(request)
        print("Replication response", resp)

    def getPath(self):
        my_list = [(1, -1), (1, 0), (-1, 0), (0, 0), (0, 1), (1, 1)]
        my_list = sorted(my_list, key=lambda k: [k[1], k[0]])
        my_list = sorted(my_list, key=lambda k: [k[0], k[1]])
        # print(my_list)
        dicty = {}
        counter = 0
        listy = []
        for i in my_list:
            dicty[counter] = i
            listy.append(counter)
            counter += 1
        # print(dicty)
        x = np.array(listy)
        a = np.reshape(x, (2, 3))
        string_list = []
        for i in range(len(a)):
            temp = ""
            for j in range(len(a[i])):
                temp += str(a[i][j])
            string_list.append(temp)
        col = 0
        row = 0
        goal = "5"
        columns = 3
        rows = 2

        def bfs(grid, start):
            queue = collections.deque([[start]])
            seen = set([start])
            while queue:
                path = queue.popleft()
                x, y = path[-1]
                if grid[y][x] == goal:
                    return path
                for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= x2 < columns and 0 <= y2 < rows and grid[y2][x2] != -1 and (x2, y2) not in seen:
                        queue.append(path + [(x2, y2)])
                        seen.add((x2, y2))

        path = bfs(string_list, (col, row))
        print("PATHHHH==", path)

        # my_list = [(1, -1), (1, 0), (-1, 0), (0, 0), (0, 1), (1, 1)]
        # # my_list = metadata
        # my_list = sorted(my_list, key=lambda k: [k[1], k[0]])
        # my_list = sorted(my_list, key=lambda k: [k[0], k[1]])
        # # print(my_list)
        # dicty = {}
        # counter = 0
        # listy = []
        # for i in my_list:
        #     dicty[counter] = i
        #     listy.append(counter)
        #     counter += 1
        # # print(dicty)
        # x = np.array(listy)
        # # number_of_rows = self.get_number_of_rows(metadata)
        # number_of_rows = 2
        # # number_of_cols = self.get_number_of_cols(metadata)
        # number_of_cols = 3
        # a = np.reshape(x, (number_of_rows, number_of_cols))
        # string_list = []
        # for i in range(len(a)):
        #     temp = ""
        #     for j in range(len(a[i])):
        #         temp += str(a[i][j])
        #     string_list.append(temp)
        # destination = 5
        # width, height = number_of_cols, number_of_rows
        # # grid = [
        # # "012",
        # # "345"]
        # start = (0, 0)
        # path = self.bfs(string_list, start, destination, width, height)
        # print(path)

    def start_threads(self):
        # Thread(target=self.replicateContent()).start()
        # Thread(target=self.retries).start()
        Thread(target=self.receive_message).start()

# initalt repl
# calling main
# best nodes
