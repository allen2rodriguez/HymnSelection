from connect2server import hymndb, cursor
from selector import select_hymn, check_if_full

# List of all SQL queries to be used in selecting an opening hymns
opening_numbers = "SELECT hymnNum FROM openingHymn"
count_opening = "SELECT COUNT(hymnNum) FROM openingHymn"
find_title = "SELECT title FROM openingHymn WHERE hymnNum = %s"

#File name to store all the previous hymns
prevOpenings = "prevSelections/PrevOpenings.txt"

#Get the total number of opening hymns
cursor.execute(count_opening)
countresult = cursor.fetchone()
num_opening_hymns = countresult[0] 

#Get a list of all the hymn numbers 
cursor.execute(opening_numbers)
num_results = cursor.fetchall()

opening_map = {}

for i in range(num_opening_hymns):
    opening_map[i] = num_results[i][0]

check_if_full(num_opening_hymns, prevOpenings)

selection = opening_map[select_hymn(num_opening_hymns, prevOpenings)]

cursor.execute(find_title, (selection,))
opening_title = cursor.fetchone()

def get_opening_num():
    return selection

def get_opening_title():
    return opening_title

