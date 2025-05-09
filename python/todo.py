"""
This script defines command-line arguements using the argparse module.
"""
import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """
    with open(TASK_FILE,"a", encoding="utf-8") as file:
        file.write(task +"\n")
def list_tasks():
    """
    Lists the tasks in the provided task list with their index.
    
    Args:
        list_tasks: A list of strings, where each string represents a task
        
    Returns:
        str: A formatted string containing the numbered tasks,or will be empty
    
"""
    with open (TASK_FILE,"r", encoding= "utf-8") as file:
        tasks = file.readlines()
    output_string= "Your task list:\n"
    formatted_tasks = []
    for index,task in enumerate(tasks):
        formatted_tasks.append(f"{index + 1}. {task}")
    output_string += "".join(formatted_tasks)
    return output_string.rstrip('\n')



def remove_task(index):
    """Function: remove_task

    Input: index - the number of the task to remove from the list
    Return: nothing
    """
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        if 1 <= index <= len(tasks):
            with open(TASK_FILE, "w", encoding="utf-8") as file:
                for i, task in enumerate(tasks, start=1):
                    if i != index:
                        file.write(task)
            print(f"Task at index {index} removed.")
        else:
            print(f"Invalid task number: {index}.Enter a number between 1")
    else:
        print("No tasks found.")


def main():
    """The main function of the script"""
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
