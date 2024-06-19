list_of_tasks = []

class Task: 

    identity = "Task"



    def __init__(self,name,skills,location,budget,arrival_deadline) -> None:
        self.name = name
        self.skills = skills
        self.location = location
        self.budget = budget
        self.arrival_deadline = arrival_deadline

    def new_entry(self):

        name = input("Enter the name : ")
        skills = [skill for skill in input("Enter the skills : ").split(',')]
        location =[int(loc) for loc in input("Enter the location : ").split(',')]
        budget = int(input("Enter the budget : "))
        arrival_deadline = int(input("Enter the deadline : "))

        instance = Task(name,skills,location,budget,arrival_deadline)

        list_of_tasks.append(instance)








        
