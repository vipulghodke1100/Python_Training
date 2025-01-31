import streamlit as st
import os
import hashlib
import json

def create_directory():
    """
        function creates the 3 directories 
        1.Employee
        2.Admin
        3.Manager    
        
    """
    dir_list = ['EMPLOYEE', 'ADMIN', 'MANAGER']
    for item in dir_list:
        try:
            os.mkdir(item)
        except FileExistsError as e:
            pass
        except PermissionError as e:
            print(f"{e}")
        except Exception as e:
            print(f"{e}")
            
def user_exist(username,role):
    with open(f"./{role.upper()}/{role.lower()}.txt", 'r') as file:
        file_content = json.load(file)
        print(file_content)


def hashed_password(password):
    password = password.encode('utf-8')
    hashed_pass = hashlib.sha256(password)
    return hashed_pass.hexdigest()

def new_registration(username, password,confirm_password, role):
    
    create_directory()
    if os.path.isfile(f"./{role.upper()}/{role.lower()}.txt"):
        st.error("Username already exists!")
        return False
    
    if password!=confirm_password:
        st.error("password wont match!!")
    hash_pass = hashed_password(password)
    print('---------User Registration-----------')
    lst = [username, hash_pass, role]
    with open(f"./{role.upper()}/{role.lower()}.txt", 'w+') as file:
        file.write(f'{username},{hash_pass},{role}')
    st.success(f"Registration successful! You are registered as {role}.")

def user_login(username, password, role):
    if not os.path.isfile(f"./{role.upper()}/{role.lower()}.txt"):
        print("No user Found")
        return False

    hash_pass = hashed_password(password)

    with open(f"./{role.upper()}/{role.lower()}.txt", 'r') as file:
        file_content = file.read().split(',')

    if file_content[1] == hash_pass:
        return True
    return False


def change_password(username, current_password,new_password, confirm_password, role):
    
    if not os.path.isfile(f"./{role.upper()}/{role.lower()}.txt"):
        st.error("User does not exist!")
        return False
    
    if not user_login(username,current_password,role):
        st.error("Current password dont match. Cant change")
        return False

    if new_password != confirm_password:
        st.error("New passwords do not match!")
        return False

    new_hash_pass = hashed_password(new_password)
    with open(f"./{role.upper()}/{role.lower()}.txt", 'w') as file:
        file.write(f'{username},{new_hash_pass},{role}')
    return True


# Page title
st.title("Login, Register, and Change Password")

# Available options: Login, Register, Change Password
page = st.radio("Choose an option", ("Login", "Register","Change Password"))

if page == "Register":
    # Registration Form
    st.subheader("Register a new account")

    with st.form(key="register_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        # Dropdown for selecting user role
        role = st.selectbox("Select Role", ["ADMIN", "EMPLOYEE", "MANAGER"])

        submit_button = st.form_submit_button("Register")

        if submit_button:
            if password != confirm_password:
                st.error("Passwords do not match!")
            elif username == "" or password == "":
                st.error("Username and Password are required!")
            else:
                new_registration(username, password,confirm_password, role)

elif page == "Login":
    # Login Form
    st.subheader("Login to your account")

    with st.form(key="login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Select Role", ["ADMIN", "EMPLOYEE", "MANAGER"])
        submit_button = st.form_submit_button("Login")

        if submit_button:
            if user_login(username, password, role):
                st.success(f"Login successful! You are logged in as {role}.")
            else:
                st.error("Invalid username or password!")


elif page=="Change Password":
    with st.form(key="change_password_form"):
        username = st.text_input("Username")
        current_password = st.text_input("Current Password", type="password")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm New Password", type="password")
        role = st.selectbox("Select Role", ["ADMIN", "EMPLOYEE", "MANAGER"])
        change_password_button = st.form_submit_button("Change Password")

        if change_password_button:
            if change_password(username,current_password,new_password, confirm_password, role):
                st.success(f"Password for {username} changed successfully!")
            
        