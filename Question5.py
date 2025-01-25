'''Write function which takes string as input and returns dictionary that contains each 
word and its frequency. Take input from user and use regex for matching patterns 
E.g text = "Hello world, hello python. Python is a programming language."'''
import re

def convertToDict(text):
    """_summary_

    Args:
        text (str): takes the string input

    Returns:
        dict: dictionary with count of each word
    """
    dict={}
    arr=[x for x in re.split(r"[,.\s]",text.lower()) if x]
    # arr=[x for x in arr if x]
    while '' in arr:
        arr.remove('')
    print(arr)
    for item in arr:
        if item not in dict.keys():
            dict[item]=1
        else:
            dict[item]+=1
    return dict
            

if __name__=='__main__':
    text=input("Enter the string:")
    dict=convertToDict(text)
    print(dict)
