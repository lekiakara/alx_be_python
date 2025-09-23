# Prompt for single task details

task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ") 
priority = input("Priority (high/medium/low): ")


# Process using match case for priority

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task. Finish project report' is a high priority task that requires immediate attention today!" 
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task. Make sure you finish it today."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task. Consider completin it today."
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level."

# Modify reminder if task is time-sensitive

if time_bound == "yes":
    print(reminder)
if time_bound == "no":
    print(reminder)
if time_bound == "medium":
    print(reminder)
else:
    print(reminder)
    
    
    