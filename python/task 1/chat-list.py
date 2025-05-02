import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_task(self, task, priority="medium", category=None, due_date=None):
        new_task = {
            "id": len(self.todos) + 1,
            "task": task,
            "priority": priority.lower(),
            "category": category,
            "due_date": due_date,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.todos.append(new_task)
        self.save_todos()
        return new_task
    
    def list_tasks(self, filter_type="all"):
        if filter_type == "completed":
            return [task for task in self.todos if task["completed"]]
        elif filter_type == "pending":
            return [task for task in self.todos if not task["completed"]]
        elif filter_type.startswith("priority:"):
            priority = filter_type.split(":")[1].lower()
            return [task for task in self.todos if task["priority"] == priority]
        elif filter_type.startswith("category:"):
            category = filter_type.split(":")[1]
            return [task for task in self.todos if task["category"] and task["category"].lower() == category.lower()]
        else:
            return self.todos
    
    def complete_task(self, task_id):
        for task in self.todos:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_todos()
                return task
        return None
    
    def delete_task(self, task_id):
        self.todos = [task for task in self.todos if task["id"] != task_id]
        self.save_todos()
        return True
    
    def update_task(self, task_id, new_task=None, new_priority=None, new_category=None, new_due_date=None):
        for task in self.todos:
            if task["id"] == task_id:
                if new_task:
                    task["task"] = new_task
                if new_priority:
                    task["priority"] = new_priority
                if new_category:
                    task["category"] = new_category
                if new_due_date:
                    task["due_date"] = new_due_date
                self.save_todos()
                return task
        return None

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nTask List:")
    print("-" * 80)
    print(f"{'ID':<5}{'Task':<30}{'Priority':<10}{'Category':<15}{'Due Date':<15}{'Status':<10}")
    print("-" * 80)
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f"{task['id']:<5}{task['task'][:28]:<30}{task['priority'].capitalize():<10}"
              f"{task['category'] or 'None':<15}{task['due_date'] or 'None':<15}{status:<10}")
    print()

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. List Pending Tasks")
        print("4. List Completed Tasks")
        print("5. Complete Task")
        print("6. Delete Task")
        print("7. Update Task")
        print("8. Filter by Priority")
        print("9. Filter by Category")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            priority = input("Enter priority (high/medium/low): ") or "medium"
            category = input("Enter category (optional): ") or None
            due_date = input("Enter due date (YYYY-MM-DD, optional): ") or None
            todo_list.add_task(task, priority, category, due_date)
            print("✅ Task added successfully!")
        
        elif choice == "2":
            tasks = todo_list.list_tasks()
            display_tasks(tasks)
        
        elif choice == "3":
            tasks = todo_list.list_tasks("pending")
            display_tasks(tasks)
        
        elif choice == "4":
            tasks = todo_list.list_tasks("completed")
            display_tasks(tasks)
        
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                if todo_list.complete_task(task_id):
                    print("✅ Task marked as complete!")
                else:
                    print("❌ Task not found.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid number.")
        
        elif choice == "6":
            try:
                task_id = int(input("Enter task ID to delete: "))
                if todo_list.delete_task(task_id):
                    print("✅ Task deleted successfully!")
                else:
                    print("❌ Task not found.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid number.")
        
        elif choice == "7":
            try:
                task_id = int(input("Enter task ID to update: "))
                new_task = input("Enter new task description (leave empty to keep current): ") or None
                new_priority = input("Enter new priority (high/medium/low, leave empty to keep current): ") or None
                new_category = input("Enter new category (leave empty to keep current): ") or None
                new_due_date = input("Enter new due date (YYYY-MM-DD, leave empty to keep current): ") or None
                if todo_list.update_task(task_id, new_task, new_priority, new_category, new_due_date):
                    print("✅ Task updated successfully!")
                else:
                    print("❌ Task not found.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid number.")
        
        elif choice == "8":
            priority = input("Enter priority to filter (high/medium/low): ")
            tasks = todo_list.list_tasks(f"priority:{priority}")
            display_tasks(tasks)
        
        elif choice == "9":
            category = input("Enter category to filter: ")
            tasks = todo_list.list_tasks(f"category:{category}")
            display_tasks(tasks)
        
        elif choice == "0":
            print("👋 Goodbye!")
            break
        
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
