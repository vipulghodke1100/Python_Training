def word_count(text):
    arr=list(text.split())
    return len(arr)

def most_common_word(text):
    dict={}
    arr=list(text.split())
    
    for item in arr:
        if item in dict.keys():
            dict[item]+=1
        else:
            dict[item]=1
    
    maxval=max(dict.values())
    most_common=[]
    for key,value in dict.items():
        if value==maxval:
            most_common.append(key)
    return most_common

def reverse_text(text):
    arr=list(text.split())
    strg=arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        strg+=f" {arr[i]}"        
    return strg


def check_pallindrome(text):
    arr=list(text.split())
    for i in range(len(arr)//2):
        if arr[i].lower()!=arr[len(arr)-1-i].lower():
            return False
    return True