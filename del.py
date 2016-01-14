"""
So I found this strange feature(?) in OSX where if you print the ASCII characters
corresponding to ESC and a lowercase 'c' in that order, the terminal will delete a bunch of
previous output. This occurs with a couple other characters too. Read the full description 
at: 
"""
printme = [27, 99]
for num in printme:
    print(chr(num))
