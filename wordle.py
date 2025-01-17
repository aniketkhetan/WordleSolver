import random
import nltk
from nltk.corpus import words

nltk.download("words")

# Filter 5-letter words
word_list = [word.lower() for word in words.words() if len(word) == 5]


# Choose a random word from the list
target_word = random.choice(word_list)
#target_word = 'prose'

def wordle_solver(word_list, target_word, max_attempts=6):
    epsilon = 0.3
    rewards = {word: 0 for word in word_list}  
    target_word = target_word.lower()
    print(f"\n\n The Target word to guess: {target_word}\n\n\n")
    
    for attempt in range(1, max_attempts + 1):
        #epislon greedy
        if random.random() < epsilon:  
            # Explore
            guess = random.choice(word_list)
        else:  
            # Exploit
            guess = max(word_list, key=lambda w: rewards[w])
        
        # Get feedback for the guess
        feedback = get_feedback(guess, target_word)
        
        print(f"Attempt {attempt}: {guess} -> {''.join(feedback)}")
        
        # Calculate reward
        reward = calculate_reward(feedback)
        rewards[guess] += reward
        
        # Filter the word list
        word_list = filter_words(word_list, guess, feedback)
        
        # Check if the word was guessed correctly
        if guess == target_word:
            print(f"\nWord guessed successfully in {attempt} attempts! \n")
            return
        # Check if there are any words remaining
        if not word_list:
            print("\nNo words remaining! The solver failed. \n")
            return
    # Failed to guess the word
    print("\nFailed to guess the word within the maximum attempts. \n")


def get_feedback(guess, target):
    """Simulates Wordle feedback."""
    feedback = []
    for g, t in zip(guess, target):
        if g == t:
            feedback.append("🟩")  # Correct letter and position
        elif g in target:
            feedback.append("🟨")  # Correct letter, wrong position
        else:
            feedback.append("⬜")  # Incorrect letter
    return feedback

def calculate_reward(feedback):
    """Assigns numerical rewards based on feedback."""
    reward_map = {"🟩": 2, "🟨": 1, "⬜": 0}
    return sum(reward_map[f] for f in feedback)

def filter_words(word_list, guess, feedback):
    """Filters the word list based on feedback."""
    filtered_list = []
    for word in word_list:
        valid = True
        for i, (g, f) in enumerate(zip(guess, feedback)):
            if f == "🟩" and word[i] != g:  # Must match position
                valid = False
            elif f == "🟨" and (g not in word or word[i] == g):  # Must exist, but not in this position
                valid = False
            elif f == "⬜" and g in word:  # Must not exist in the word
                valid = False
        if valid:
            filtered_list.append(word)
    return filtered_list

# Run the solver
wordle_solver(word_list, target_word)
