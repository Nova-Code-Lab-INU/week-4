#logic_tools

def assign_badge(score):
    
    if 90 <= score <= 100:
        return "Elite Gold"
    
    elif 70 <= score < 90:
        return "Professional Silver"
    
    elif 50 <= score < 70:
        return "Starter Bronze"
    
    else:
        return "Needs Retraining"
    

    #main_app
    from logic_tools import assign_badge

    while True:

        try:
            team_name = input ("Enter the team name :")
            if team_name.upper() == "E":
                break
            member_name =input("Enter the member name:")

            score =float(input("Enter the score:"))

            badge = assign_badge(score)

            print("Rank:", badge)
            with open("nova_database.txt", "a") as file:
                file.write(f"team :{team_name} | Member : {member_name} | Rank : {badge} \n")
        except ValueError:
            print("Input error: Please enter a valid score.")

        finally :
            print("Nova System Shutdown : Data is safely stored")