class Employee:
    """This is a representation of an emplyee."""
    def __init__(self,name,id):
        print(f"Employee {self.name} created with id {self.id}")

    def add_task(self,task):


        print(f"Employee {self.name} created with id {self.id}")
        self.tasks.append(task)


employee_1=Employee("Richard","123")
employee_2=Employee("Jelly","456")
print("Employee 1 Name:", employee_1.name)


