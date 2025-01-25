import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Date Proposal", layout="centered")

# Initialize session state for button visibility
if "show_yes" not in st.session_state:
    st.session_state.show_yes = False  # Initially, "Yes" button is disabled
if "show_no" not in st.session_state:
    st.session_state.show_no = True   # "No" button is visible by default

# Function to display the "Yes" scenario with love animation
def show_love():
    st.markdown("<h1 style='text-align: center; color: pink;'>💖💖 Yes! 💖💖</h1>", unsafe_allow_html=True)
    st.markdown("<div style='background-color: pink; padding: 20px;'>"
                "<h2 style='text-align: center;'>Thank you! You've made my day! 💕💞💓</h2>"
                "</div>", unsafe_allow_html=True)

# Function to display the hypnotized message
def show_hypnotized():
    st.markdown("<div style='background-color: black; padding: 20px;'>"
                "<h2 style='color: white; text-align: center;'>You can only select 'Yes'... "
                "You have been hypnotized by me... 😏✨</h2>"
                "</div>", unsafe_allow_html=True)

# Main question
st.title("Made in India By Hritesh.... :)")
st.title("Hey Ma'am, hope you're doing well! I was thinking, with Valentine’s Day around the corner, it might be fun to try something a little different. How about a virtual movie date? We could pick a movie we both enjoy, sync it up, and watch together while on a call. Let me know what you think!😊 yes or no?")
st.write("Please select your answer below:")

# Display the "No" button (if visible)
if st.session_state.show_no:
    if st.button("No ❌"):
        st.session_state.show_no = False  # Hide the "No" button after clicking
        st.session_state.show_yes = True  # Make the "Yes" button visible
        show_hypnotized()  # Display the hypnotized message

# Display the "Yes" button (if visible)
if st.session_state.show_yes:
    if st.button("Yes 💖"):
        show_love()  # Display the love animation
