class ToDoList:
    def __init__(self):
        self.tasks = {}
        
    def Add_task(self,taskName,task):
        self.tasks[taskName] = task
        print(f"\n             Task - '{task}' Add successfully.")
        
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("        Tasks Are      ")
            for index, task in self.tasks.items():
                print(f"Name: {index} => Task: {task}")
    def mark_completed(self, task_index):
        if task_index in self.tasks:
            print(f"   '{self.tasks[task_index]}' Tasks completed.")
        else:
            print("Invalid task Name. Please enter a valid Name.")
        
    def delete_task(self, task_index):
        if task_index in self.tasks:
            del self.tasks[task_index]
            print("\nTask Deleted Successfully !")
        else:
            print("Invalid task index. Please enter a valid index.")
        
        



def main():
    todo = ToDoList()
    
    while True:
        print("\n Hi every one!")
        print("1.Add")
        print("2.view")
        print("3.make task")
        print("4.Delete Task")
        print("5.Exist")
        
        ch = input("\nEnter your chose: ")
        
        if ch == '1':
            taskName = input("\nEnter the task Name: \n")
            task = input("Enter the task: \n")
            todo.Add_task(taskName,task)
        elif ch == '2':
            todo.view_tasks()
        elif ch == '3':
                task_index = input("\nEnter the Name of the task to mark as completed: ")
                todo.mark_completed(task_index)
        elif ch == '4':
            option = input("\nDo you want to Delete (Yes/No): ")
            if option == 'Yes':
                task_index = input("\nEnter the Name of the task to Delete : ")
                todo.delete_task(task_index)
            elif option == 'No':
                print("\nOK It DONE !")
        else:
            break
       

main()