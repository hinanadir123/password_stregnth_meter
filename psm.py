# PRroject no 2 , password Stregnth Meter 

import re
import streamlit as st

# pagestyling
st.set_page_config(page_title= "Password stregnth meter created by HINA NADIR MUGHAL", page_icon="🌘" ,layout="centered")

# custom css
st.markdown("""
<style>
    .main{text-align: center;}
    .stTextInput {width: 60% |important; margin:auto;} 
    .stButton button {width:50%; background-color : blue; color:white; font-size:18px;}                       
    .stButton button:hover { background-color: red; color: white;}         
</styles>
""", unsafe_allow_html=True)

# page title and description
st.title("🔑Password Stregnth Meter")
st.write("⚠️Enter your password to check its security level.✅")

# function to check password stregnth

def check_passowrd_stregnth(password):
    score = 0
    feedback = []
     
    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("Password should be **atleast 8 character long**⚠️.")     
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("password should be included both upper and lowercase letters.")    
    if re.search(r"\d" , password):
        score +=1
    else:
        feedback.append("password shoulde be include ** atleast one number (0-9).")        
    #special characters
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("include **at least one special character (!@#$%&*)**.")

    # display password stregnth  
    if score == 4:
        st.success("**strong password**  your password is secure🖲️.")
    elif score == 3:
        st.info("**Moderate password - consider improving security by adding more features")    
    else:
        st.error("**week passowrd** - Follow the instruction below to stragnthen it.")    

    if feedback:
        with st.expander(" **Improve your password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type= "password", help="enter your passowrd is strong")                

# button working
if st.button("check strength"):
    if password:
        check_passowrd_stregnth(password)
    else:
        st.warning  ("🎉Please enter a password first!") #show warning if password empty.  


                    




