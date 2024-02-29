
origianl = "OBA@VMEBOxTbi'ljbQlErkqfkdz"

for singleChar in origianl:
    asciiValue = ord(singleChar); #ord() function returns the ASCII value of the character
    add3toAscii = asciiValue + 3;
    print(chr(add3toAscii), end="") 

print(origianl)