# Prompt for single task details

task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ") 
priority = input("Priority (high/medium/low): ")


# Process using match case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task. Give it maximum attention."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task. Make sure you complete it within the specified period of time."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level. Do not give it any attention."

# Modify reminder if task is time-sensitive
if time_bound == "yes":
    reminder += "It requires immediate attention today!"

    

# Print final customized reminder
print(reminder) 