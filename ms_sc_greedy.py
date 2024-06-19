#from worker import list_of_workers
#from task import list_of_tasks

import math

def distance(loc1,loc2):
    return math.dist(loc1,loc2)

def check_skillmatch(worker,task):
    k = set(worker.skills)&set(task.skills)
    if(k == None):
        return False
    else:
        return True

def check_valid(task,worker):
    if((check_skillmatch(worker,task)) & (worker.cost<=task.budget) & (distance(worker.location,task.location)<= worker.max_distance) & (distance(worker.location,task.location)*worker.velocity<=task.arrival_deadline)):
        return True
    return False

def generate_graph(list_of_tasks,list_of_workers):
    k = {}
    worker_no=-1
    for i in list_of_workers:
        worker_no = worker_no + 1
        for j in range(len(list_of_tasks)):
            if(check_valid(i,list_of_tasks[j])):
                if i in k.keys():
                    k[i].append(list_of_tasks[j])
                else:
                    k[i] = [list_of_tasks[j]]
    return k

def calculate_score(worker,task):
    s = (task.budget - worker.cost)*len(list(set(worker.skills).intersection(set(task.skills))))
    s = s/len(task.skills)
    return s

def ms_sc_greedy(list_of_workers,list_of_tasks):
    Ip = []
    k = generate_graph(list_of_workers,list_of_tasks)
    while((len(list_of_tasks) !=0) & (len(list_of_workers)!=0)):
        S_cand = []
        assigned_w = 0
        for task in list_of_tasks:
            print(task)
            for worker in k[task]:
                S_cand.append([worker,task])
            score = 0
            for g in S_cand:
                cur_score = calculate_score(g[0],g[1])
                if cur_score>score:
                    score = cur_score
                    assigned_w = g[0]
                    assigned_t = g[1]
        Ip.append([assigned_w,assigned_t])
        list_of_workers.remove(assigned_w)
        skills_covered = list(set(assigned_w.skills).intersection(set(assigned_t.skills)))
        assigned_t.skills = [ele for ele in assigned_t.skills if ele not in skills_covered]
    return Ip
           