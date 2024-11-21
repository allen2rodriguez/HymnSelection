from connect2server import hymndb, cursor
from selector import select_hymn, check_if_full

# List of all SQL queries to be used in selecting an special hymns
special_numbers = "SELECT hymnNum FROM specialHymns"
count_special = "SELECT COUNT(hymnNum) FROM specialHymns"
find_title = "SELECT title FROM specialHymns WHERE hymnNum = %s"
find_topic = "SELECT * FROM specialHymns WHERE topic = %s"

#File name to store all the previous hymns
prevspecials = "prevSelections/Prevspecials.txt"

#Get the total number of special hymns
cursor.execute(count_special)
countresult = cursor.fetchone()
num_special_hymns = countresult[0] 

#Get a list of all the hymn numbers 
def get_special_num():
    cursor.execute(special_numbers)
    num_results = cursor.fetchall()

    special_map = {}

    for i in range(num_special_hymns):
        special_map[i] = num_results[i][0]

    check_if_full(num_special_hymns, prevspecials)

    selection = special_map[select_hymn(num_special_hymns, prevspecials)]
    return selection

def get_special_title(selection):
    selection = selection
    cursor.execute(find_title, (selection,))
    specialTitle = cursor.fetchone()

    return specialTitle





# WIP ===============================================================================================================
def determine_numOf_hymns(input):
    if input == 3:
        return selection, specialTitle
    
def determine_topic():
    response = input("Is there a topic? y/n: ")
    if response == 'y':
        print("Choose From the Following")
        topic = input("'Temples', 'Service', 'Restoration', 'Prophets','Gratitud', 'Family', 'Faith'")

        cursor.execute(find_topic, (topic))
        topics_found = cursor.fetchall()



