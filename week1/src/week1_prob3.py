# Given a string, find the length of the longest substring without repeating characters. For
# example, the longest substring without repeating letters for "abcabcbb" is "abc", which the
# length is 3.
#
# For "bbbbb" the longest substring is "b", with the length of 1.

#Solution1 Complexity n^2

def substr1(string):
    #unique_symbol is an empty list which will keep track of the unique symbols encountered
    #so far in the string passed as the argument to the current function
    unique_symbol=[]

    for i in string:
        if i not in unique_symbol:
            unique_symbol.append(i)
            #print (unique_symbol)
        else:
            break

    subsequence=''.join(unique_symbol)
    print(subsequence)
    print(len(subsequence))

#Solution2 Complexity n
def substr2(string):
    #max is an integer variable which will keep track of the highest character index without repitition
    max=-1
    for i in string:
        if string.index(i)>max:
            max=string.index(i)
            #indices.append(symbols.index(i))
            #print(indices)
        else:
            break

    subsequence = string[:max+1]
    print(subsequence)
    print(len(subsequence))




def main(string):
    #substr1(string)
    substr2(string)


if __name__ == "__main__":
    main("abcabcbb")