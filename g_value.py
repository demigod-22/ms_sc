import math

def calculate_degree(graph):
    count1 = 0
    count2 = 0
    for i in graph.keys():
        count1 = count1 + 1
        count2 = count2 + len(graph[i])
    degree = count2/count1
    return degree

def calculate_g(m,degree):
    g=2
    l = ((m*(math.log10(m))*(g*math.log10(g) - g - 1))/(g*math.log10(2*g))) + ((1-m)/((1-g)**2))*(degree**2)
    while(l<0):
        g = g+1
        if(g==m):
            break
        l =  l = ((m*(math.log(m))*(g*math.log(g) - g - 1))/(g*math.log(2*g))) + ((1-m)/((1-g)**2))*(degree**2)
    return g



