# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie La Joie
#               Shweta Kumaran
#               Eugenio Casaubon
# Section:      521
# Assignment:   Lab: Topic 11
# Date:         14 November 2022

# Take an input file and determine how many of the passports are valid :)

file = input("Enter the name of the file: ")
scanned = open(file, "r")
valid = open("valid_passports.txt", "w")
scannedstr = scanned.read()
scannedlist = scannedstr.split("\n\n")
met = 0
for i in range(len(scannedlist)):
    #check if valid passport
    if ((scannedlist[i].find('byr') != -1) and
            (scannedlist[i].find('iyr') != -1) and
            (scannedlist[i].find('eyr') != -1) and
            (scannedlist[i].find('hgt') != -1) and
            (scannedlist[i].find('ecl') != -1) and
            (scannedlist[i].find('pid') != -1) and
            (scannedlist[i].find('cid') != -1)):
        met += 1
        valid.write(scannedlist[i])
        valid.write('\n\n')

print(f'There are {met} valid passports')

scanned.close()
valid.close()
