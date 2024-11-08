def yesterday_task():
    if os.path.isfile(yesterday) or os.path.getsize(today):
        with open(yesterday, 'r') as file:
            yesterday_tasks = file.readlines()
        with open(today, 'a') as file:
            for line in yesterday_tasks:
                task_name, status = line.split(',')
                if status.strip() == "Not done":
                    file.write(f'{task_name},Not done\n')
