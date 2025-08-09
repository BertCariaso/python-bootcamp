

class Employee:
    """This is a representation of an employee."""
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.tasks=[]
        print(f"Employee {self.name} created with id {self.id}")

    def add_task(self,task):

        print(f"Employee {self.name} created with id {self.id}")
        self.tasks.append(task)

class Recruiter(Employee):
     def __init__(self,name,id):
         super().__init__(name,id)

     def recruit(self,task):
        self.add_task("Recuit ")

class Developer(Employee):
    def __init__(self, name, id):

        super().__init__(name, id)

    def code(self, task):
        self.add_task("Code ")

class Manager(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)

    def manage(self, task):
        self.add_task("Manage ")

