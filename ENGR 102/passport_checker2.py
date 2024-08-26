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

# Oh no there's requirements for the aspects of the passport! :o

file = input("Enter the name of the file: ")
scanned = open(file, "r")
valid = open("valid_passports2.txt", "w")
scannedstr = scanned.read()
scannedlist = scannedstr.split("\n\n")
for i in range(len(scannedlist)):
    scannedlist[i] = scannedlist[i].split()
met = 0
num = 0
for i in range(len(scannedlist)):
    for j in range(len(scannedlist[i])):
        if scannedlist[i][j].find("byr") != -1:
            byr = scannedlist[i][j]
            yr = int(byr[4:])
            if 1920 <= yr <= 2005:
                num += 1
        if scannedlist[i][j].find("iyr") != -1:
            iyr = scannedlist[i][j]
            yr = int(iyr[4:])
            if 2012 <= yr <= 2022:
                num += 1
        if scannedlist[i][j].find("eyr") != -1:
            eyr = scannedlist[i][j]
            yr = int(eyr[4:])
            if 2022 <= yr <= 2032:
                num += 1
        if scannedlist[i][j].find("hgt") != -1:
            hgt = scannedlist[i][j]
            if "cm" in hgt:
                if len(hgt) < 9:
                    num += 0
                else:
                    tall = int(hgt[4:7])
                    if 150 <= tall <= 193:
                        num += 1
            if "in" in hgt:
                tall = int(hgt[4:6])
                if 59 <= tall <= 76:
                    num += 1
        if scannedlist[i][j].find("ecl") != -1:
            ecl = scannedlist[i][j]
            if "amb" or "blu" or "brn" or "gry" or "grn" or "hzl" or "oth" in ecl:
                num += 1
        if scannedlist[i][j].find("pid") != -1:
            pid = scannedlist[i][j]
            if len(pid) == 13:
                num += 1
            else:
                num += 0
        if scannedlist[i][j].find("cid") != -1:
            cid = scannedlist[i][j]
            if int(cid[4]) != 0:
                num += 1
        if num == 7:
            met += 1
            for k in range(len(scannedlist[i])):
                valid.write(str(scannedlist[i][k]))
                valid.write(" ")
            num = 0
            valid.write("\n\n")
    num = 0

print(f'There are {met} valid passports')


valid.close()
scanned.close()
