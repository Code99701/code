to_do_list = ["Buy Groceries", "Clean the house", "Pay bills"]

# Adding a new task to the to-do list
to_do_list.append("schedule meeting")
to_do_list.append("Go for a run")

# Removing a completed task from the to-do list
to_do_list.remove("Clean the house")

# checking if a task is in the to-do list
if "Pay bills" in to_do_list:
    print("Don't forget to pay the bills!")

print("Current To-Do List:")
for task in to_do_list:
    print(f"- {task}")