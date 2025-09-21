# Prompt for single task details

task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Enter the priority level (high/medium/low): ")


# Process using match case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority level."

# Modify reminder if task is time-sensitive
if time_bound == "yes":
    reminder = " This task requires immediate attention today!"

# Print final customized reminder
print(reminder)