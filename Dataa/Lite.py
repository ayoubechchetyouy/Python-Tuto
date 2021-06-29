input_message = """
What Do You Want T o DO ?
"s" => Show All Skills
"a" => Add New Skills
"s" => Delete A Skills
"u" => Update Skills Progress
"q" => Quit The App
Choose Option: 
"""
user_input = input(input_message).strip().lower()
cammands_list = ["s", "a", "d", "u", "q"]

def show_skills():
    print('Show Skills')
def add_skills():
    print('Add Skill')
def delete_skills():
    print('Delete Skill')
def update_skills():
    print('Update Skill')


if user_input in cammands_list:
    print(f'Command Found {user_input}')
    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skills()
    elif user_input == "d":
        update_skills()
    elif user_input == "u":
        update_skills()
else:
    print(f'Sorry This Command {user_input} Is Not Found')
