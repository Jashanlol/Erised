file=open("cogs/utils/Testbankpdf.txt","r")

from random import getrandbits
n = 0
splitLines = file.read().split("\n\n")
output = ""

for questionN in splitLines:
    if n == 10:
        break
    if bool(getrandbits(1)):
        output += questionN
    #print(questionN, "END")

    n += 1
print(output)
file.close()