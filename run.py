from worker import Worker,list_of_workers
from task import Task,list_of_tasks
from ms_sc_greedy import generate_graph,ms_sc_greedy
from ms_sc_g_dc import ms_sc_decomp
i=0
Ip = []
while(i<3):

    entry = input("Add worker or task. Enter 1 for worker and 2 for task : ")

    print(entry)



    if(entry == "1"):
        instance = Worker(0,0,0,0,0,0)
        instance.new_entry()
    else:
        instance = Task(0,0,0,0,0)
        instance.new_entry()
    i = i+1

b = ms_sc_decomp(list_of_workers,list_of_tasks,2)

print(b)
print("Done")


