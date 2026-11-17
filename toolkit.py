# toolkit.py - Personal Mini-Toolkit Final Project
# Author: Degraph Engineer

def number_guessing_game():
    """Tool 1: A number guessing game using conditionals and a loop."""
    print("\n--- NUMBER GUESSING GAME ---")
    secret_number = 7
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == secret_number:
        print("🎉 Incredible! You guessed the secret number right away!")
    elif guess < secret_number:
        print("📉 Too low! The secret number was 7.")
    else:
        print("📈 Too high! The secret number was 7.")

def manage_todo_list(todo_list):
    """Tool 2: A dynamic to-do list manager using lists and a loop."""
    print("\n--- DYNAMIC TO-DO LIST ---")
    while True:
        action = input("Type 'add' to add a task, 'view' to view tasks, or 'back' to return to menu: ").strip().lower()
        if action == "add":
            task = input("Enter the new task: ")
            todo_list.append(task)
            print(f"✅ Success! Added: '{task}'")
        elif action == "view":
            if not todo_list:
                print("📭 Your to-do list is currently empty.")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(todo_list, start=1):
                    print(f"{index}. {task}")
        elif action == "back":
            break
        else:
            print("❌ Invalid command. Please type 'add', 'view', or 'back'.")

def calculate_bill():
    """Tool 3: A bill and tip calculator using conditionals and f-strings."""
    print("\n--- BILL & TIP CALCULATOR ---")
    try:
        bill = float(input("Enter the total bill amount ($): "))
        service = input("How was the service? (good / average / bad): ").strip().lower()
        
        if service == "good":
            tip_percent = 0.20
        elif service == "average":
            tip_percent = 0.15
        else:
            tip_percent = 0.10
            
        tip_amount = bill * tip_percent
        total_amount = bill + tip_amount
        print(f"💰 Tip ({int(tip_percent * 100)}%): ${tip_amount:.2f} | Total to pay: ${total_amount:.2f}")
    except ValueError:
        print("❌ Please enter a valid numerical amount for the bill.")

def main():
    """Main menu loop to navigate the toolkit."""
    # Shared dynamic list for the to-do tool
    my_tasks = ["Learn Python functions", "Build GitHub repository"]
    
    print("\n=========================================")
    print("      WELCOME TO MY PYTHON TOOLKIT 🚀    ")
    print("=========================================")
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Number Guessing Game")
        print("2. Manage To-Do List")
        print("3. Calculate Bill & Tip")
        print("4. Quit Program")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            manage_todo_list(my_tasks)
        elif choice == "3":
            calculate_bill()
        elif choice == "4":
            print("\n👋 Thank you for using Personal Mini-Toolkit. Keep building amazing things! Goodbye!")
            break
        else:
            print(f"❌ Invalid choice '{choice}'. Please select a valid option between 1 and 4.")

if __name__ == "__main__":
    main()
