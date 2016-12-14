import textwrap

file = open("text.txt", "r")
cont = file.read()

wrapper = TextWrapper(wrap())


def word_wrap(string, width=80, ind1=0, ind2=0, prefix='|'):
    """ word wrapping function.
        string: the string to wrap
        width: the column number to wrap at
        prefix: prefix each line with this string (goes before any indentation)
        ind1: number of characters to indent the first line
        ind2: number of characters to indent the rest of the lines
    """
    string = prefix + ind1 * " " + string
    newstring = ""
    while len(string) > width:
        # find position of nearest whitespace char to the left of "width"
        marker = width - 1
        while not string[marker].isspace():
            marker = marker - 1

        # remove line from original string and add it to the new string
        newline = string[0:marker] + prefix + "\n"
        newstring = newstring + newline
        string = prefix + ind2 * " " + string[marker + 1:]
    test = newstring + string    
    return textwrap.fill(test, width=70)    
    ##return newstring + string

print(word_wrap(cont))
##print(textwrap.with(30).wrap(cont))
