# ----------- Fix String ----------
# DESCRIPTION:
# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.
# EXAMPLES
# fix_string('T0PP1NG5') => 'TOPPINGS'
# fix_string('5OUR') => 'SOUR'
# fix_string('1GLO0') => 'IGLOO'

#fixing three different mistakes 5 back to S, 0 back to 0, and 1 back to I

#takes a string
#convert special mistakes to letters
#return the string fixed

def fix_string(word):
    mistakes = { '5':'S', '0': 'O', '1':'I'}
    fixed_word = ''
    for letter in word:
        if letter in mistakes:
            fixed_word += mistakes[letter]
        else:
            fixed_word += letter
    return fixed_word

# Time Complexity O(n) Space complexity: 2n?

def ip_fix(word):
    mistakes = {'5':'S', '0': 'O', '1':'I'}
    wlst = [*word]
    for i, v in enumerate(wlst):
        if v in mistakes:
            wlst[i] = mistakes[v]
    return ''.join(wlst)
    
# Time complexity: O(n) Space complexity: make a list and a string

# def one_fix(word):
#     wlst = [x for x in word {'5':'S', '0': 'O', '1':'I'}]




print(ip_fix('T0PP1NG5'))
print(fix_string('5OUR'))
print(fix_string('1GLO0'))

