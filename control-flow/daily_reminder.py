#daily reminder uses conditional statemen match case and loops to remind the user about a single task for the day based on time sensitivity.

while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter something.")

priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound?(yes/no): ").lower().strip()

reminder = f"'{task}' is a {priority} priority task"

match priority:
    case "high":
        reminder += " that is very important."
    case "medium":
        reminder += " that you should work on soon."
    case "low":
        reminder += " that you can complete when you have free time."
    case _:
        reminder += " (priority unclear)."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " It is not time-sensitive."

print(f"Reminder: {reminder}")

