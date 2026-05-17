# logic_tools.py

def assign_badge(score):

    if score >= 90 and score <= 100:
        return "Elite Gold"

    elif score >= 70 and score <= 89:
        return "Professional Silver"

    elif score >= 50 and score <= 69:
        return "Starter Bronze"

    else:
        return "Needs Retraining"

# main_app.py

from logic_tools import assign_badge

while True:

    try:
        print("\n===== NOVA LAB SYSTEM =====")

        choice = input("Enter E to Exit or press Enter to continue: ")

        if choice.lower() == 'e':
            print("Exiting system...")
            break

        team_name = input("Enter Team Name: ")
        member_name = input("Enter Member Name: ")

        score = float(input("Enter Score: "))

        badge = assign_badge(score)

        print("\n===== RESULT =====")
        print("Team:", team_name)
        print("Member:", member_name)
        print("Rank:", badge)

        with open("nova_database.txt", "a") as file:
            file.write(
                f"Team: {team_name} | Member: {member_name} | Rank: {badge}\n"
            )

        print("Data saved successfully!")

    except ValueError:
        print("⚠ Input Error: Please enter numbers only for the score!")

    finally:
        print("Nova System Shutdown: Data is safely stored.")
