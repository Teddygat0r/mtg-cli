#Include Globally used functions here

def formatList(myList):
    str = ""
    for x in myList:
        str += x.__str__() + "\n"
    return str