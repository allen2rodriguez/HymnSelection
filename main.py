from openingChoice import get_opening_num, get_opening_title
from sacramentChoice import get_sac_num, get_sac_title
from specialChoice import get_special_num, get_special_title

#Get the hymns needed
opening_num = get_opening_num()
opening_title = get_opening_title()

sac_num = get_sac_num()
sac_title = get_sac_title()

num_of_hymns = int(input("How many hymns will you be playing? "))

if num_of_hymns == 2:
    print("Ok, wheres what to play:")
    print('Opening: %d "%s"' % (opening_num, opening_title[0]))
    print('Sacrament: %d "%s"' % (sac_num, sac_title[0]))
    

elif num_of_hymns == 3:
    spl_num = get_special_num()
    spl_title = get_special_title(spl_num)
    

    print("Ok, wheres what to play:")
    print('Opening: %d "%s"' % (opening_num, opening_title[0]))
    print('Sacrament: %d "%s"' % (sac_num, sac_title[0]))
    print('Closing: %d "%s"' % (spl_num, spl_title[0]))

elif num_of_hymns == 4:
    spl_num = get_special_num()
    spl_title = get_special_title(spl_num)

    spl_num2 = get_special_num()
    spl_title2 = get_special_title(spl_num2)

    print("Ok, wheres what you should play Allen:")
    print('Opening: %d "%s"' % (opening_num, opening_title[0]))
    print('Sacrament: %d "%s"' % (sac_num, sac_title[0]))
    print('Intermediate: %d "%s"' % (spl_num, spl_title[0]))
    print('Closing: %d "%s"' % (spl_num2, spl_title2[0]))
  
else:
    print("Invalid Input")