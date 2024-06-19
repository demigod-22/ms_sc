list_of_workers =  []


class Worker: 

    identity = "worker"



    def __init__(self,name,skills,location,velocity,distance,cost) -> None:
        self.name = name
        self.skills = skills
        self.location = location
        self.velocity = velocity
        self.max_distance = distance
        self.cost = cost

    def new_entry(self):

        name = input("Enter the name : ")
        skills = [skill for skill in input("Enter the skills : ").split(',')]
        location =[int(loc) for loc in input("Enter the location : ").split(',')]
        velocity = int(input("Enter the velocity : "))
        distance = int(input("Enter the maximum distance : "))
        cost = int(input("Enter the travelling cost : "))

        instance = Worker(name,skills,location,velocity,distance,cost)

        list_of_workers.append(instance)
        





        
