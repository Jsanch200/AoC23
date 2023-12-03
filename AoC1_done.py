def getDigits(line):
    firstDigits = None
    lastDigits = None
    #since im using the isdigit function, it will return 
    #an interger or "None" if it detects a string
    for digit in line:
        #looping through the file
        if digit.isdigit():
            if firstDigits == None:
                firstDigits = digit
                #if firstDigits is a string, it will return "None". otherwise,
                #it will return an interger
            else:
                lastDigits = digit
                #i was curious as to why my code was not outputting more than 2 intergers
                #because i know some lines in this puzzle contained more than 2 intergers
                #but this else statement would be constantly replacing itself until it reaches
                #the last interger. a bit of an oversight, BUT IT WORKS.
    if lastDigits == None:
        lastDigits = firstDigits
        #just in case some lines only had 1 interger, lastDigits was
        #outputting "None"
    return int(str(firstDigits) + str(lastDigits))
    #change string output into intergers for later on


with open("C:\\Users\\Mike\\Documents\\AdventOfCode23\\puzzle input day 1.txt") as file:
    lines = file.readlines()
    #opening the file to read line by line
    lol = 0
    for line in lines:
        lol += getDigits(line)
        #add up each line to the next one, with the final line being the answer to
        #AdventOfCyber level 1
        #this took me a couple of hours, i touch python maybe once a week ;__;
        print(lol)
