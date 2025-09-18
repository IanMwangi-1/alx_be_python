# daily_reminder.py

# Prompt for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Handle priority with if/elif (instead of match case)
if priority == "high":
    reminder = f"'{task}' is a high priority task."
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task."
elif priority == "low":
    reminder = f"'{task}' is a low priority task."
else:
    reminder = f"'{task}' has an unknown priority level."

# Add time sensitivity
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print final reminder
print("\nReminder:", reminder)
