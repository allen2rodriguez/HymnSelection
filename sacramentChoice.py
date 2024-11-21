from connect2server import hymndb, cursor
from selector import select_hymn, check_if_full

# List of all SQL queries to be used in selecting an sacrament hymns
sacrament_numbers = "SELECT hymnNum FROM sacramentHymns"
count_sac = "SELECT COUNT(hymnNum) FROM sacramentHymns"
find_title = "SELECT title FROM sacramentHymns WHERE hymnNum = %s"

#File name to store all the previous hymns
prevSacraments = "prevSelections/PrevSacraments.txt"

#Get the total number of sacrament hymns
cursor.execute(count_sac)
countresult = cursor.fetchone()
num_sac_hymns = countresult[0] 

#Get a list of all the hymn numbers 
cursor.execute(sacrament_numbers)
num_results = cursor.fetchall()

sac_map = {}

for i in range(num_sac_hymns):
    sac_map[i] = num_results[i][0]

check_if_full(num_sac_hymns, prevSacraments)

selection = sac_map[select_hymn(num_sac_hymns, prevSacraments)]

cursor.execute(find_title, (selection,))
sacTitle = cursor.fetchone()

# Funtions to return to main
def get_sac_num():
    return selection

def get_sac_title():
    return sacTitle
