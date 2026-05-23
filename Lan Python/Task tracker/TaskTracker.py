import datetime
class Task:
    def __init__(self, id, description, createdAt, updatedAt, status = False ) -> None:
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        
    def add_task(self):
        self.id = input("Enter the no of the task: ")
        self.description = input("Enter the description of the task: ")
        self.createdAt = {}
        
        
    
    def update_task(self):
        choice = input("Enter your choice of update:\n1. ID\n2. Description")
        if choice == "ID":
            self.id = input("Enter the updated ID: ")
        elif choice == 2:
            self.description = input("Enter the updated description:")
        else:
            raise ValueError("Please enter the correct number of choice.")
        self.updatedAt = {}
    
    def delete_task(self, num):
        self.num = num
        num = input("Please enter the number of task you want to delete: ")
        if self.id == num:
            del self.id
            del self.description
            del self.createdAt
            del self.updatedAt
        else:
            print("Wrong input.")
                                           
    
    def mark_task(self):
        choice = input("Enter Done after completion of task: ")
        if choice == 'done':
            self.status = True
            
    def list_task(self):
        choice = input("Do you want to see the list of all tasks?\n1. Yes\n2. No\n")
        if choice == 1:
            
        
        