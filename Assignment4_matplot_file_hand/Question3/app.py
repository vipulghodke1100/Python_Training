# import os
# import hashlib


# def create_directory():
#     """
#         function creates the 3 directories 
#         1.Employee
#         2.Admin
#         3.Manager    
#     """
#     dir_list=['EMPLOYEE','ADMIN','MANAGER']
#     for item in dir_list:
#         try:
#             os.mkdir(item)
#         except FileExistsError as e:
#             pass
#         except PermissionError as e:
#             print(f"{e}")
#         except Exception as e:
#             print(f"{e}")
        
# def hashed_password(password):
#     password=password.encode('utf-8')
#     hashed_pass=hashlib.sha256(password)
#     return hashed_pass.hexdigest()


 
# def new_registration(username,password,role):
#     if os.path.isfile(f"./{role.upper()}/{username}.txt"):
#         print(f"user already exists. cant register")
#         return
#     email=input("Enter Email: ")
#     phone=input("Enter phone No: ")
#     hash_pass=hashed_password(password)
    
#     print('---------User Registration-----------')
#     lst=[username , hash_pass , role]
    
#     with open(f"./{role.upper()}/{username.lower()}.txt",'w+') as file:
#         file.write(f'{username},{hash_pass},{role},{email},{phone}')
    
#     print(f"User created with role {role}")
#     return 
    

    
# def user_login(username,password,role):
#     if not os.path.isfile(f"./{role.upper()}/{username}.txt"):
#         print("No user Found")
#         return
    
#     hash_pass=hashed_password(password)
    
#     with open(f"./{role.upper()}/{username.lower()}.txt",'r') as file:
#         file_content= file.read().split(',')
                   
#     if file_content[1]==hash_pass:
#         print("LOGGED IN SUCESSFULLY")
#     else:
#         print("INCORRECT PASSWORD")
#     return 
        
# def change_password(username,new_pass,password,role):
#     if not os.path.isfile(f"./{role.upper()}/{username}.txt"):
#         print("No user Found")
#         return 
    
#     new_hash_pass=hashed_password(new_pass)
#     with open(f"./{role.upper()}/{username.lower()}.txt", 'w') as file:
#         file.write(f'{username},{new_hash_pass},{role}')
#         print("Password changed")
#     return new_pass
    
    
# def main_fun():
#     create_directory()
#     username=input("Enter the username :")
#     password=input("Enter password :")
#     role=input("Enter valid Role :")
#     while True :
#         print("1. User_registration")
#         print("2. User_login")
#         print("3. Change User Password")
#         print("4. Exit ")
#         option=int(input("Enter your choice: "))
        
#         match option:
#             case 1 :
#                 new_registration(username,password,role)
#             case 2 :
#                 user_login(username,password,role)
#             case 3:
#                 password=change_password(username,password,role)
#             case 4:
#                 break
#             case _:
#                 print("Enter valid Choice: ")
            
    
# if __name__=='__main__':
#     main_fun()


def user_exist(username,role):
    try:
        with open(f"./{role.upper()}/{role.lower()}.txt", 'r') as file:
            file_content=file.readlines()
            for line in file_content:
                name,role=line.strip().split(',') 
                if name==username:
                    print('user found')
                    return 
            else:
                print("user not found")
    except Exception as e:
        print(e)
            
            
def update_role(username,role,new_role): 
    try:
        with open(f"./{role.upper()}/{role.lower()}.txt", 'r') as file:
            lines=file.readlines()
            
        for idx,line in enumerate(lines):
            user,role_=line.strip().split(",")
            if user==username and role.upper()==role_:
                lines[idx]=f"{username},{new_role}\n"
                
        with open(f"./{role.upper()}/{role.lower()}.txt", 'w') as file:
            file.writelines(lines)
            
    except Exception as e:
        print(f"Error updating role: {e}")  
    print("new role overited")     
    return 
            
            
            
    
user_exist("vipul","admin")

update_role("sham","employee","emp")
