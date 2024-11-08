import os
from datetime import datetime,timedelta
# 1) Create a dd-mm-yy_todo.txt file for every day
today = datetime.now().strftime("%d-%m-%Y") + '_todo.txt'
yesterday = (datetime.now() - timedelta(days=1)).strftime("%d-%m-%Y") + '_todo.txt'
def yesterday_task():
    if os.path.isfile(yesterday) or os.path.getsize(today):
        with open(yesterday, 'r') as file:
            yesterday_tasks = file.readlines()
        with open(today, 'a') as file:
            for line in yesterday_tasks:
                task_name, status = line.split(',')
                if status.strip() == "Not done":
                    file.write(f'{task_name},Not done\n')
def add_task():
    yesterday_task()
    task_name = input('Enter task ').strip().capitalize()
    with open(today,'a') as file:
        file.write(f'{task_name},Not done\n')
    print('Task is added')
def view_task():
    if not os.path.isfile(today):
        print('No task added')
        return
    if not os.path.getsize(today):
        print('All task have been deleted')
        return
    with open(today) as file:
        todo_list = file.readlines()
    for i,line in enumerate(todo_list,1):
        task_name,status = line.split(',')
        print(f'{i:<3}{task_name:30}{status}',end='')
def mark_done():
    if not os.path.isfile(today):
        print('No task added')
        return
    if not os.path.getsize(today):
        print('All task have been deleted')
        return
    task_no = int(input('Enter task_no '))
    with open(today) as file:
        todo_list = file.readlines()
    flag = False
    with open(today,'w') as file:
        for i, line in enumerate(todo_list, 1):
            task_name, status = line.split(',')
            if i == task_no:
                file.write(f'{task_name},Done\n')
                flag = True
            else:
                file.write(line)
    if flag:
        print('Task marked as done')
    else:
        print(f'{task_no} is invalid')
def delete_task():
    if not os.path.isfile(today):
        print('No task added')
        return
    if not os.path.getsize(today):
        print('All task have been deleted')
        return
    task_no = int(input('Enter task_no '))
    with open(today) as file:
        todo_list = file.readlines()
    flag = False
    with open(today,'w') as file:
        for i, line in enumerate(todo_list, 1):
            task_name, status = line.split(',')
            if i == task_no:
                flag = True
            else:
                file.write(line)
    if flag:
        print('Task is deleted')
    else:
        print(f'{task_no} is invalid')
# 3) Add option to view todo for older date.
def view_old_tasks():
    date_input = input("Enter date (dd-mm-yyyy): ")
    old_file = date_input + '_todo.txt'
    if not os.path.isfile(old_file) or not os.path.getsize(old_file):
        print(f'No tasks found for {date_input}')
        return
    with open(old_file) as file:
        todo_list = file.readlines()
    for i, line in enumerate(todo_list, 1):
        task_name, status = line.split(',')
        print(f'{i:<3}{task_name:30}{status}', end='')
yesterday_task()
while True:
    print()
    print('-'*30)
    print(f'!!!! MENU !!!! \
          \n1.Add New Task \
          \n2.View All Tasks \
          \n3.Mark as Done \
          \n4.Delete Task \
          \n5.View Old Task \
          \n0.Exit ')
    choice = input('Enter choice ')
    if not choice.isdigit():
        print('Invalid input ')
        continue
    choice = int(choice)
    if choice == 0:
        print('Good bye')
        break
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_done()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        view_old_tasks()
    else:
        print('Invalid choice')
#end
'''
1) Create a dd-mm-yy_todo.txt file for every day
2) Copy Not Done task from previous day in every todo
3) Add option to view todo for older date. 
'''