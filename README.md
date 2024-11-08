# To-Do List Manager

This Python script helps you manage daily tasks by creating a new to-do list file for each day, allowing you to add, view, mark tasks as done, and delete tasks. Additionally, it provides the option to view tasks from previous days.

## Features

1. **Daily Task Files**: The script creates a new to-do list file each day named `dd-mm-yy_todo.txt`. It records tasks for the current day.
2. **Carry Over Tasks**: It copies tasks marked as "Not done" from the previous day's to-do list into the new day's list.
3. **Task Management**: You can:
   - Add new tasks.
   - View tasks for today or any previous day.
   - Mark tasks as done.
   - Delete tasks from the list.
4. **View Old Tasks**: You can view tasks for any specified day by entering the desired date in `dd-mm-yyyy` format.

## Requirements

- Python 3.x

## Script Workflow

### Task Flow
1. **Daily To-Do File**: A new file is created every day, named using the current date in the format `dd-mm-yy_todo.txt`.
2. **Carry Over Not Done Tasks**: If the previous day's tasks exist and are marked "Not done," those tasks will be copied over to today's file.
3. **Task Operations**:
   - **Add a Task**: You can enter a new task, which will be added to today's list as "Not done."
   - **View Tasks**: You can view today's tasks or view tasks for a specific date.
   - **Mark as Done**: You can mark a specific task as done by entering its task number.
   - **Delete a Task**: You can delete a task from today's list by its task number.

### File Format

Each task in the `.txt` file is stored as:
```
task_name, status
```
Where:
- `task_name` is the name/description of the task.
- `status` is either "Not done" or "Done."

### Example of a `dd-mm-yy_todo.txt` file:
```
Buy groceries, Not done
Finish homework, Not done
Clean room, Done
```

## Functions

### `yesterday_task()`
Checks for the previous day's file and copies over tasks marked as "Not done" to today's to-do file.

### `add_task()`
Prompts the user to input a task and adds it to the current day's to-do list as "Not done."

### `view_task()`
Displays all tasks for today, showing task numbers, names, and their status.

### `mark_done()`
Marks a specific task as "Done" based on the task number input by the user.

### `delete_task()`
Deletes a specific task based on the task number input by the user.

### `view_old_tasks()`
Allows the user to input a date (in `dd-mm-yyyy` format) and view the tasks for that day.

## How to Use

1. **Run the script**: The script will automatically create a new to-do list for the current day.
2. **Menu Options**:
   - **Add New Task**: Choose option 1 to add a task.
   - **View All Tasks**: Choose option 2 to see today's tasks.
   - **Mark as Done**: Choose option 3 to mark a task as completed.
   - **Delete Task**: Choose option 4 to delete a task.
   - **View Old Tasks**: Choose option 5 to view tasks from a previous day by entering the date in `dd-mm-yyyy` format.
3. **Exit**: Choose option 0 to exit the program.

## Example Usage

### Example Menu Interaction

```
!!!! MENU !!!!
1. Add New Task
2. View All Tasks
3. Mark as Done
4. Delete Task
5. View Old Task
0. Exit

Enter choice: 1
Enter task: Finish Python homework
Task is added

Enter choice: 2
1   Finish Python homework                 Not done
2   Buy groceries                          Not done

Enter choice: 3
Enter task_no: 1
Task marked as done

Enter choice: 4
Enter task_no: 2
Task is deleted

Enter choice: 5
Enter date (dd-mm-yyyy): 05-11-2024
1   Complete project                       Done
```

## Future Enhancements

- **Task Prioritization**: Add support for task priority (e.g., High, Medium, Low).
- **Due Dates**: Allow users to set due dates for tasks.
- **Persistent Data Storage**: Save tasks in a database instead of text files for better scalability.

## License

This script is free to use and modify under the MIT license. 

---
