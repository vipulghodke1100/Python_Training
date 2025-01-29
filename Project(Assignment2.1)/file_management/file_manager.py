import json 
from datetime import datetime


def save_users_to_file(users ,path):
    with open(path,'w') as file:
        json.dump(users,file,indent=2)
        
        
def load_data_from_file(path):
    try:
        with open (path ,'r') as file:
            users=json.load(file)
            return users
    except FileNotFoundError as e:
        print( f"Error : {e}")
    
    
def write_summery(text_analysis_list,path):
    file=open(path,'a')
    file.write('\n')
    file.write(f"timestamp:{datetime.now()}\n")
    for item in text_analysis_list:
        file.write(f"{item} " )
    file.write('\n')
    file.close()
    

    