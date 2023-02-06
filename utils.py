#Include Globally used functions here
import os
import psutil


def formatList(myList):
    str = ""
    for x in myList:
        str += x.__str__() + "\n"
    return str

def printMemory():
    print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
