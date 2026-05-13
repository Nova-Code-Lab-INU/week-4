# logic_tools.py

def assign_badge(score):
   
    if 90 <= score <= 100:
        return "Elite Gold"
    elif 70 <= score <= 89:
        return "Professional Silver"
    elif 50 <= score <= 69:
        return "Starter Bronze"
    else:
        return "Needs Retraining"
    

# main_app.py
from logic_tools import assign_badge

def start_system():
    print("--- Nova Lab Security and Ranking System ---")
    
    # Getting User Inputs
    team_name = input("Enter Team Name: ")
    member_name = input("Enter Member Name: ")
    
    # Using a loop to handle potential input errors
    while True:
        try:
            # Error Handling (The Security Shield)
            score_input = input("Enter the score: ")
            score = float(score_input)
            
            # Getting the result from the imported function
            badge = assign_badge(score)
            
            # Permanent Storage (File Handling)
            # Opening the file in Append Mode ('a') as required
            with open("nova_database.txt", "a") as file:
                # Formatting the record according to the required structure
                record = f"Team: [{team_name}] | Member: [{member_name}] | Rank: [{badge}]\n"
                file.write(record)
            
            print(f"Success! {member_name} has been ranked as: {badge}")
            print("Progress saved to nova_database.txt")
            break # Exit loop after successful execution
            
        except ValueError:
            # Catching non-numeric values to prevent system crash
            print("Input Error: Please enter numbers only for the score!")

# Starting the application
if __name__ == "__main__":
    start_system()

