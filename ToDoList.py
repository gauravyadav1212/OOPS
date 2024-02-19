# To make a to do list.
class Task:
    def __init__(self,title,description,due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def display_task(self):
        print(f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}\n")


class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print("The task has been added successfully")

    def display_task(self, task):
        if self.tasks == []:
            print("No tasks found!")
            return
        for task in self.tasks:
            task.display_task()

    def remove_task(self, task_title):
        for task in self.tasks:
            if(task.title == task_title):
                self.tasks.remove(task)
                print(f"Task '{task_title}' removed successfully!")
                return        
            print("Task Not found")
    
    def marked_as_completed(self, task_title):
        for task in self.tasks:
            if(task.title == task_title):
                task.status = "Complete"
                print(f"Task: {task_title} has been marked as complete")
                return
            print("Task not found")


def main():
    List = ToDoList()
    while(True):

        print("Please enter your choice:\n1.)Add new task\n2.)Remove task\n3.)Mark as complete\n4.)Display all tasks\n5.)Exit Program")
        choice1 = int(input())

        if choice1 == 1:
            print("Please enter the task title: ")
            task_title = input()
            print("Please enter the task description: ")
            task_description = input()
            print("Please enter the due date: ")
            due_date = input()

            task1 = Task(task_title, task_description, due_date)
            List.add_task(task1)

        elif choice1 == 2:
            print("Please enter the task title: ")
            task_title = input()

            List.remove_task(task_title)

        elif choice1 == 3:
            print("Please enter the task title: ")
            task_title = input()

            List.marked_as_completed(task_title)

        elif choice1 == 4:
            List.display_task(task1)

        elif choice1 == 5:
            print("Warning! This will wipe out the to do list, press y to continue or any other key to return: ")
            choice2 = input()
            if choice2 == 'y':
                break
        
        else:
            print("Please enter the correct choice")

if __name__ == '__main__':
    main()

