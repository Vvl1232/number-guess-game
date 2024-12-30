import random as rd
import streamlit as st

st.title("Number Guessing Game 🎲")
st.write("I'm thinking of a number between 1 and 100. Can you guess it? 🤔")

if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = rd.randint(1, 100)

if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

difficulty_level = st.text_input("To choose a difficulty level, type 'easy' or 'hard': ").lower()

if difficulty_level not in ["easy", "hard"]:
    st.info("Please choose a difficulty level to start the game.")
    st.stop()  

if difficulty_level == "easy" and 'initialized_easy' not in st.session_state:
    st.session_state.attempts = 10
    st.session_state.initialized_easy = True
    st.write("You've chosen **easy** mode. You have 10 attempts. Good luck! 🍀")
elif difficulty_level == "hard" and 'initialized_hard' not in st.session_state:
    st.session_state.attempts = 5
    st.session_state.initialized_hard = True
    st.write("You've chosen **hard** mode. You have 5 attempts. Bring it on! 💪")

if difficulty_level in ["easy", "hard"]:
    user_input = st.number_input("Enter a number between 1 and 100:", min_value=1, max_value=100, step=1)

    if st.button("Submit") and st.session_state.attempts > 0:
        st.session_state.attempts -= 1
        if st.session_state.number_to_guess == user_input:
            st.success(f"🎉 Congrats! You guessed it right! The number was {st.session_state.number_to_guess}")
            st.balloons()
        elif st.session_state.number_to_guess > user_input:
            st.warning(f"📉 You guessed too low! Try again. You have {st.session_state.attempts} attempts left.")
        elif st.session_state.number_to_guess < user_input:
            st.warning(f"📈 You guessed too high! Try again. You have {st.session_state.attempts} attempts left.")
        

    if st.session_state.attempts == 0 and st.session_state.number_to_guess != user_input:
        st.error(f"💥 Oops! You've run out of attempts. You lose! The number was {st.session_state.number_to_guess}")

    if st.button("Reset Game 🔄"):
        st.session_state.clear()
        st.rerun()
