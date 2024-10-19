import streamlit as st

# Set up initial page configuration
st.set_page_config(page_title="Date Proposal", layout="centered")

# Use session state to manage button clicks and behavior
if 'clicked_no' not in st.session_state:
    st.session_state.clicked_no = False
if 'clicked_yes' not in st.session_state:
    st.session_state.clicked_yes = False

# Function to display the "Yes" scenario with love animation
def show_love():
    st.markdown("<h1 style='text-align: center; color: pink;'>💖💖 Yes! 💖💖</h1>", unsafe_allow_html=True)
    st.markdown("<div style='background-color: pink; padding: 20px;'>"
                "<h2 style='text-align: center;'>Thank you! You've made my day! 💕💞💓</h2>"
                "</div>", unsafe_allow_html=True)

    # Love heart animation using HTML & CSS
    love_animation = """
    <div style="text-align:center; background-color: pink;">
        <div class="heart"></div>
        <div class="heart"></div>
        <div class="heart"></div>
        <style>
        .heart {
            position: relative;
            width: 100px;
            height: 90px;
            background-color: red;
            margin: 50px auto;
            transform: rotate(-45deg);
            animation: beat 1s infinite;
        }
        .heart:before,
        .heart:after {
            content: "";
            position: absolute;
            width: 100px;
            height: 90px;
            background-color: red;
            border-radius: 50%;
        }
        .heart:before {
            top: -50px;
            left: 0;
        }
        .heart:after {
            left: 50px;
            top: 0;
        }
        @keyframes beat {
            0%, 100% {
                transform: scale(1) rotate(-45deg);
            }
            50% {
                transform: scale(1.1) rotate(-45deg);
            }
        }
        </style>
    </div>
    """
    st.markdown(love_animation, unsafe_allow_html=True)

# Function to display the "No" scenario
def show_hypnotized():
    st.markdown("<div style='background-color: black; padding: 20px;'>"
                "<h2 style='color: white; text-align: center;'>You can only select 'Yes'... "
                "You have been hypnotized by me... 😏✨</h2>"
                "</div>", unsafe_allow_html=True)

# Display the question
st.title("Made in _A_T_'s Lab")
st.title("Will you accompany me during my lows, promise to listen to Sunday suspense, watch movies, and listen to the songs I share?")
st.write("Please select your answer below:")

# Handle the Yes button
if st.button("Yes 💖"):
    st.session_state.clicked_yes = True
    show_love()

# Handle the No button behavior
if st.session_state.clicked_no:
    # If No has been clicked, display the hypnotized message
    show_hypnotized()
else:
    if st.button("No ❌"):
        st.session_state.clicked_no = True
        # Apply dark theme immediately after clicking "No"
        st.markdown(
            """
            <style>
            .main {
                background-color: black;
                color: white;
            }
            </style>
            """, unsafe_allow_html=True
        )
        show_hypnotized()
