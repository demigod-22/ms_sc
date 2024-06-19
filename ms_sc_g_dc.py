import math
import numpy as np
from g_value import *
from ms_sc_greedy import check_valid,ms_sc_greedy,generate_graph

def distance(loc1,loc2):
    return math.dist(loc1,loc2)


def generate_graph1(list_of_workers,list_of_tasks):
    k = {}
    worker_no=-1
    for i in list_of_workers:
        worker_no = worker_no + 1
        for j in range(len(list_of_tasks)):
            if(check_valid(i,list_of_tasks[j])):
                if list_of_tasks[j] in k.keys():
                    k[list_of_tasks[j]].append(i)
                else:
                   k[list_of_tasks[j]] = [i]
    return k


def find_nearest_tasks(task,list_of_tasks,g):
    nearest_tasks = []
    distances = {}
    l = math.ceil(len(list_of_tasks)/g) 
    l = min(l,len(list_of_tasks))
    for i in list_of_tasks:
        loc = distance(task.location,i.location)
        distances[i] = loc
    keys = list(distances.keys())
    values = list(distances.values())
    sorted_value_index = np.argsort(values)
    sorted_tasks = [keys[i] for i in sorted_value_index]
    nearest_tasks = sorted_tasks[:l]
    return nearest_tasks


def ms_sc_decomp(list_of_workers,list_of_tasks,g):
    P = []
    for i in range(g):
        P.append([])
    G = generate_graph1(list_of_tasks,list_of_workers)
    print("Graph : ",G)
    for s in range(g):
        small = float('inf')
        max_index = 0
        cur_index = 0
        print("list of tasks : ",list_of_tasks)
        for y in list_of_tasks:
            if y.location[1] < small:
                small = y.location[1]
                max_index = cur_index
            cur_index = cur_index+ 1
        anchor = list_of_tasks[max_index]
        nearest_tasks = find_nearest_tasks(anchor,list_of_tasks,g)
        print("anchor : ",anchor)
        print("nearest tasks : ",nearest_tasks)
        sub_prob = {}
        for t in nearest_tasks:
            sub_prob[t] = G[t]
        P[s] = sub_prob
        list_of_tasks = [i for i in list_of_tasks if i not in nearest_tasks]
    return P[g-1]

def ms_sc_conflict_reconcile(Ip,Ips):
    worker_Ip = [i[0] for i in Ip]
    worker_Ips = [i[0] for i in Ips]
    conflicting_workers = list(set(worker_Ips).intersection(set(worker_Ip)))
    while(len(conflicting_workers)!=0):
        k=0
        max_index = 0
        max = 0
        for i in conflicting_workers:
            if i.cost>max:
                max = i.cost
                max_index = k
            k = k+1
        highest_costworker = conflicting_workers[max_index]
        conflicting_workers.remove(highest_costworker)
    return Ip

def ms_sc_gdc(list_of_tasks,list_of_workers):
    Ip = []
    graph = generate_graph1(list_of_tasks,list_of_workers)
    degree = calculate_degree(graph)
    g = calculate_g(len(list_of_tasks),degree)
    sub_problems = ms_sc_decomp(list_of_workers,list_of_tasks,g)
    for i in sub_problems:
        if len(graph[i]) != 1:
            Ip[i] = ms_sc_gdc(i,graph[i])
        else:
            Ip[i] = ms_sc_greedy(i,graph[i])
    Sol = []
    for i in range(1,g+1):
        Sol = ms_sc_conflict_reconcile(Sol,Ip[i])
    return Sol