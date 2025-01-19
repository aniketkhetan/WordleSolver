import streamlit as st
import random
from wordle import wordle_solver, word_list

# Set the target word
 # Add your word list here
if "target_word" not in st.session_state:
    st.session_state.target_word = random.choice(word_list)  # Random target word
if "guesses" not in st.session_state:
    st.session_state.guesses = []  # Store user guesses
if "feedback" not in st.session_state:
    st.session_state.feedback = []  # Store feedback for each guess


def check_guess(guess, target_word):
    """
    Compare the guessed word with the target word and provide feedback.
    Ensures that letters are only marked as green or yellow once per occurrence in the target word.
    """
    feedback = ["⬜"] * len(guess)  # Default feedback
    target_word_used = [False] * len(target_word)  # Track which letters in the target word are "used"

    #Check for correct letters in the correct positions (🟩)
    for i, letter in enumerate(guess):
        if letter == target_word[i]:
            feedback[i] = "🟩"
            target_word_used[i] = True  # Mark this letter as "used"

    #Check for correct letters in the wrong positions (🟨)
    for i, letter in enumerate(guess):
        if feedback[i] == "⬜":  # Only process if not already green
            for j, target_letter in enumerate(target_word):
                if letter == target_letter and not target_word_used[j]:  # Match and not already used
                    feedback[i] = "🟨"
                    target_word_used[j] = True 
                    break

    return feedback


# Title and instructions
st.title("Wordle VS Bot 🎮")
st.write(
    "Guess the 5-letter word and see if you can outperform our AI bot! Use the text box below to submit your guesses. Feedback will appear below:"
)

# Input for the user to guess
guess = st.text_input("Enter your guess:", max_chars=5).lower()

# Validate input and process the guess
if st.button("Submit Guess"):
    if len(guess) != 5:
        st.warning("Please enter a 5-letter word!")
    elif guess not in word_list:
        st.warning("Word not in the word list. Try another one!")
    else:
        # Check the guess and generate feedback
        feedback = check_guess(guess, st.session_state.target_word)
        st.session_state.guesses.append(guess)
        st.session_state.feedback.append(feedback)

# Display previous guesses and feedback
if st.session_state.guesses:
    st.subheader("Your Guesses:")
    for i, guess in enumerate(st.session_state.guesses):
        st.write(f"**{guess.upper()}** → {' '.join(st.session_state.feedback[i])}")

# End game conditions
if st.session_state.guesses and st.session_state.guesses[-1] == st.session_state.target_word:
    st.success(f"🎉 Congrats! You guessed the word: {st.session_state.target_word.upper()}!")
    flag, attempts = wordle_solver(word_list, st.session_state.target_word)
    if flag:
        st.success(f"The Bot guessed the word: {st.session_state.target_word.upper()} in {attempts} attempts!")
    else:
        st.error(f"The Bot failed to guess the word: {st.session_state.target_word.upper()}.")
    st.stop()  # Stop further execution
elif len(st.session_state.guesses) >= 6:
    st.error(f"❌ Out of guesses! The word was: {st.session_state.target_word.upper()}.")
    flag, attempts = wordle_solver(word_list, st.session_state.target_word)
    if flag:
        st.success(f" The Bot guessed the word: {st.session_state.target_word.upper()} in {attempts} attempts!")
    else:
        st.error(f"The Bot failed to guess the word: {st.session_state.target_word.upper()}.")

# Reset button to restart the game
if st.button("Restart Game"):
    st.session_state.target_word = random.choice(word_list)
    st.session_state.guesses = []
    st.session_state.feedback = []
    st.rerun()  

