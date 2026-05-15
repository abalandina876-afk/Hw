class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            status = "Done" if task.done else "Not done"
            print(task.title, "-", status)


task1 = Task("Math homework")

manager = TaskManager()
manager.add_task(task1)

manager.show_tasks()

task1.complete()

manager.show_tasks()