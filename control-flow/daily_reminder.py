task = input("Enter task description: ").lower()
priority = input("Enter priority level (high/medium/low): ").lower()
time_bound = input("Is your task time-bound (yes/no)?: ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high-priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high-priority task. Complete it as soon as possible.")
    case "medium":
        print(f"Reminder: {task} is a medium-priority task. Complete it in your spare time.")
    case "low":
        if time_bound == "no":
            print(f"Note: {task} is a low-priority task. Do it when you have free time.")
        else:
            print(f"Note: {task} is a low-priority but time-bound task. Don’t forget to finish it.")
    case _:
        print("Invalid priority level entered. Please choose high, medium, or low.")
