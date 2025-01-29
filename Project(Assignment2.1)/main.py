from user_management import user_handler
from file_management import file_manager
from utils import string_tools


summery=[]
users=[]

def main_Menu():
    while True:
        print("1. Text Analysis")
        print("2. user Management")
        print("3. File Management")
        print("4. Exit")
        option = int(input("Enter your Choice:"))
        
        match option:
            case 1: 
                text_analysis()
            case 2:
                user_management()
            case 3:
                file_management()
            case 4:
                break 
            case _:
                print("\n----Enter valid Choice-----")

def text_analysis():
    while True:
        print("-------text Analysis--------")
        try:
            text=input("Enter input Sting: ")
            if not text.isalpha() and text.isdigit():     
                raise ValueError("Enter valid string ")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            break
    summery.append(f"text: {text}   ")    
    while True:
        print("1. print Word Count")
        print("2. print most Common word")
        print("3. printing the reverse of string")
        print("4. Check string is pallindrom or not")
        print("5. Back to Main Menu ")
        option = int(input("Enter your Choice: "))
        
        match option:
            case 1: 
                res=string_tools.word_count(text)
                summery.append(f"word count:{res}   ")
                print(f"word count : {res}\n")
            case 2:
                res=string_tools.most_common_word(text.lower())
                summery.append(f"most_common:{res}  ")
                print(f"most common word: {res}\n")
            case 3:
                res=string_tools.reverse_text(text)
                summery.append(f"reverse:{res}  ")
                print(f"reverse of given string: {res}\n")
            case 4:
                res=string_tools.check_pallindrome(text)
                summery.append(f"is_pallindrome:{res}   ")
                if res:
                    print(f"{text} is pallindrome\n")
                else:
                    print(f"{text} is not a pallindrome\n")
            case 5: 
                break                
            case _:
                print("\n----Enter valid Choice-----")
        
def user_management():
    while True:
        print('-------user_management-------')
        print("1. Add User")
        print("2. Remove User (age is optional paramter)")
        print("3. Get User Info (age is optional parameter)")
        print("4. Update Age of the User")
        print("5. Back to Main menu")
        option = int(input("Enter your Choice: "))
        match option:
            case 1:
                user=user_input_validation()
                username=user[0]
                age=user[1]
                try:
                    res=user_handler.add_user(users,username,age)
                    print(f"{res} Added")
                except ValueError as e:
                    print(f'Error:{e}')
            case 2:
                username=user_input_validation()[0]
                try:
                    res=user_handler.remove_user(users,username)
                    print(f"{list(res.values())[0]} deleted from user info ")
                except ValueError as e:
                    print(f"Error:{e}")
            case 3:
                username=user_input_validation()[0]
                try:
                    res=user_handler.get_user_info(users,username)
                    print(res)
                except ValueError as e:
                    print(f"Error:{e}")
            case 4:   
                user=user_input_validation()
                username=user[0]
                age=user[1]
                try:
                    res=user_handler.update_user_age(users,username,age)
                    print(res)
                except ValueError as e:
                    print(f"Error:{e}")              
            case 5:
                break
            case _:
                print("\n----Enter valid Choice-----")
                
                
def file_management():
    while True:
        print("--------file_manager-------")
        print("1. Save user list to file")
        print("2. Load user list from file ")
        print("3. Write summery of Text Analysis to file")
        print("4. Back to Main Menu")
        print("-----Note:All files created, updated under files folder in project----- ")
        option=int(input("Enter correct Choice: "))
        
        match option:
            case 1:
                file_manager.save_users_to_file(users,'files/users.txt')
            case 2:
                userloaded=file_manager.load_data_from_file('files/users.txt')
                print(userloaded)
            case 3:
                file_manager.write_summery(summery,'files/textAnalysisSummery.txt')
            case 4:
                break


def user_input_validation():
    while True:
        try:
            username=input("Enter Username: ")
            age=int(input("Enter the User's Age: "))
            if age > 100:
                raise ValueError("Enter the valid Age !! ")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            break
    return [username,age]
    

if __name__=='__main__':
    main_Menu()
    

