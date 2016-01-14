"""
Simple number crunching/ASCII converting script to solve hackthissite.org's 
Realistic Mission #6. Adds triplets of numbers together to get a valid ASCII value,
then subtracts the total ASCII value of the pass phrase to get the desired message.
Numbers are delimited by periods. Newlines are removed before processing.

WARNING: SOME ASCII CHARACTERS, ESPECIALLY NON-ALPHANUMERIC ONES, ARE CONTROL
SEQUENCES IN VARIOUS TERMINAL PROGRAMS (for example, ESC c and ESC ^ for OSX terminal). 
CAREFULLY CHECK YOUR OUTPUT TO ENSURE NOTHING UNUSUAL HAS HAPPENED TO THE TEXT.
For more information, see del.py.
"""

from collections import Counter

def decrypt(one, two, three, passtotal):
    return int(one) + int(two) + int(three) - passtotal

inp = open("XEcrypt_text.txt", 'r').read()
passtotal=int(input("Enter the total sum of the passphrase's ASCII values: "))
nums = inp.replace("\n", "").split(".")
result = ""
nums.pop(0)
asciiarray = list()
chararray = list()
while len(nums) > 0:
    intvalue = decrypt(nums.pop(0), nums.pop(0), nums.pop(0), passtotal)
    result = result + chr(intvalue)
    asciiarray.append(intvalue)
    chararray.append(chr(intvalue))
print(asciiarray)
print(chararray)



#extra stuff
for i in range(len(result)):
    input()
    print(result[i])

print("Pass: ", passtotal, "   Result: ",result)
nums = inp.replace("\n", "").split(".")
nums.pop(0)
print(nums)
print(Counter(nums))