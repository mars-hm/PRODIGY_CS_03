import streamlit as st
import re

def passwordchecker(password):
    strength = 0
    missing_criteria = []

    if len(password) >= 8:
        strength += 1
    else:
        missing_criteria.append("\tIncrease password length\n")
    
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        missing_criteria.append("\tUppercase letters\n")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        missing_criteria.append("\tLowercase letters\n")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        missing_criteria.append("\tDigits\n")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        missing_criteria.append("\tSpecial characters")

    return strength, missing_criteria

# ---- Streamlit ----
st.markdown(
    "<h1 style='text-align: center;'>Password Complexity Checker</h1>", 
    unsafe_allow_html=True
)

st.info("""Password should be at least 8 characters long. 
        \n Password should contain at least one uppercase letter [A-Z]. 
        \n Password should contain at least one lowercase letter [a-z].
        \n Password should contain at least one digit [0-9].
        \n Password should contain at least one special character ( !, @, #, $, ...).""")
password = st.text_input("Input a Password", type="password")

if password:
    strength, missing_criteria = passwordchecker(password)
    st.write("### Password Strength: " + "★" * strength + "☆" * (5 - strength))
    
    if strength == 5:
        st.info("Strong Password!")
    elif strength >= 3:
        st.info("MODERATE Password!")
        if missing_criteria:
            st.info("Add the following to increase the password complexity: " + ", ".join(missing_criteria))
    else:
        st.info("WEAK Password!")
        if missing_criteria:
            st.info("Add the following to increase the password complexity: " + ", ".join(missing_criteria))
