# Prompt for single task details

task = input("Enter your task: ")
priority = input("Enter the priority level (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


# Process using match case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level."

# Modify reminder if task is time-sensitive
if time_bound == "yes":
    reminder = "Finish project report'is a high priority task that requires immediate attention today!"

# Print final customized reminder
print(reminder)