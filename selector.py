import random

#Check to see if file is full, if it is then clear it
def check_if_full(count, filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)

    if line_count >= count:
        open(filename, 'w')

#select a hymn that has not been selected before 
def select_hymn(count, filename, ):
    fp = open(filename, 'r')
    prevValues = fp.read().splitlines()

    i = 0
    while i != 1:
        random_number = random.randint(0, count - 1)

        if str(random_number) not in prevValues:
            i = 1
            prevValues.append(str(random_number))
            with open(filename, 'a') as fp:
                fp.write(str(random_number) + '\n')
                
    return random_number