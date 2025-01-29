def add_user(users,uname,age):
    for item in users:
        if item['username']==uname:
            raise ValueError("Duplicate value Can't add new User")
    users.append({'username':uname,'age':age})
    return users
        
def remove_user(users,uname):
    for item in users:
        if item['username']==uname:
            temp=item
            del item
            return temp
    raise ValueError("User not Found Can't delete") 
    
    
def get_user_info(users,uname):
    for item in users:
        if item['username']==uname:
            return item
    raise ValueError("User not Found") 


def update_user_age(users,uname,new_age):
    for item in users:
        if item['username']==uname:
            item['age']=new_age
        return item
    raise ValueError("User not Found")
       
    