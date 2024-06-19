from ms_sc_greedy import ms_sc_greedy,generate_graph
from ms_sc_g_dc import ms_sc_decomp,generate_graph1,ms_sc_conflict_reconcile
from g_value import *


def calc_costgreedy(list_of_tasks,list_of_workers):
    G = generate_graph(list_of_tasks,list_of_workers)
    G1 = generate_graph1(list_of_tasks,list_of_workers)
    degw = calculate_degree(G)
    degt = calculate_degree(G1)
    m = len(list_of_tasks)
    n = len(list_of_workers)
    costg = m*n + n*degt*(3*m + degw) + m*degt**2
    return costg

def calc_costgdc(n,degree,m,g):
    return (m*g+n)(degree-1)


def ms_sc_adaptive(list_of_workers,list_of_tasks):
    Ip = []
    cost_greedy = calc_costgreedy(list_of_tasks,list_of_workers)
    cost_gdc = calc_costgdc()
    if cost_gdc < cost_greedy:
        Ip = ms_sc_greedy(list_of_workers,list_of_tasks)
    else:
        graph = generate_graph1(list_of_tasks,list_of_workers)
        degree = calculate_degree(graph)
        g = calculate_g(len(list_of_tasks),degree)
        sub_problems = ms_sc_decomp(list_of_workers,list_of_tasks,g)
        Ips = []
        for i in range(g):
            Ips.append([])
        for i in sub_problems : 
            Ips[i] = ms_sc_adaptive(i[0],i[1])
        for i in range(g):
            Ip = ms_sc_conflict_reconcile(Ip,Ips[i])
    return Ip