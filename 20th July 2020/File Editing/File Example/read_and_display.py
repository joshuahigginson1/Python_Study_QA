# Create a program that opens a new text file called "teams.txt", and adds the names of 5 sports teams.
# Reads and displays the names of the 1st and 4th team in the file.

# Declare Functions ------------------------------------------------------------------------------------------------

def add_teams(list_of_teams):
    teams_file = None
    with open('teams.txt', 'w') as teams_file:

        for count, team in enumerate(list_of_teams, 1):  # Cycles through every team in the list...
            newline = str(f"Team {count}: {team}\n")
            teams_file.write(newline)  # Writes a new line.

    with open('teams.txt', 'r') as teams_file:

        lines = teams_file.readlines()
        for count, team in enumerate(lines):
            if count == 1 or count == 4:
                print(team)
            else:
                continue


# Define Variables -------------------------------------------------------------------------------------------------

football_teams = ["Liverpool FC", "Everton", "West Brom", "Chelsea", "Manchester United"]

# Execute Code -----------------------------------------------------------------------------------------------------

add_teams(football_teams)
