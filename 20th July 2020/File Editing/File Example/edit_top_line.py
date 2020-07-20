# Create a program that opens the text file called "teams.txt", and replaces the first team.
# Print out the edited file line by line.

# Declare Functions ------------------------------------------------------------------------------------------------

def add_line(list_of_teams):
    teams_file = None

    with open('teams.txt', 'r') as teams_file:
        lines = teams_file.readlines()
        lines[0] = new_line_message

    with open('teams.txt', 'w') as teams_file:
        teams_file.writelines(lines)

    for line in lines:
        print(line)

# Define Variables -------------------------------------------------------------------------------------------------

new_line_message = "This is a new line.\n"

# Execute Code -----------------------------------------------------------------------------------------------------

add_line(new_line_message)
