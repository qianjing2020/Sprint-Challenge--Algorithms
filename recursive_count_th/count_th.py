'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):    
    # base case no th in word
    search = 'th'
    len1 = len(search)
    len2 = len(word)
    # special case: word = []
    if len2 == 0:
        return 0
    # base case: word has less letter than th:
    if len2 < len1:
        return 0
    # recursve case, start from first len1 in word
    # if search match first two character, add 1 
    if search == word[0:len1]: 
        return 1 + count_th(word[1:])
    # otherwise, search the right by jump to the next character    
    else:
        return count_th(word[1:])   
