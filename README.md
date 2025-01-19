# 🟩 Wordle Solver UI with Algorithm Comparison 🟨  

This project is a **Streamlit-based Wordle game** that allows users to play the popular word-guessing game while also competing against a simple algorithm. The UI not only lets you guess the target word within six attempts but also shows how the algorithm approached the same puzzle.  

**Can you guess smarter and faster than the algorithm? Try it out and find out!**

---

## 🎮 Features
- **Interactive Gameplay**: Enter your guesses and get feedback (🟩, 🟨, ⬜) for each word.
- **Algorithm Comparison**: See how an algorithm solved the same puzzle and compare your performance.
- **Dynamic Feedback**: The UI highlights correct letters (🟩), misplaced letters (🟨), and incorrect letters (⬜) for clarity.
- **Replayability**: Reset the game with a single click and face a new challenge every time.
- **Fun and Educational**: Explore how a simple algorithm mimics human guessing strategies.

---

## 🛠 How It Works
### Game Logic
1. **Target Word**: A random 5-letter word is selected from a predefined word list at the start of the game.
2. **User Guesses**: You have 6 attempts to guess the word.
3. **Feedback System**:
   - 🟩: Correct letter in the correct position.
   - 🟨: Correct letter but wrong position.
   - ⬜: Letter not in the target word.
4. **Algorithm Guesses**: The app simulates the algorithm solving the same puzzle using strategies like **epsilon-greedy exploration**.
5. **Comparison**: After the game ends, see how many attempts you needed versus how many the algorithm needed.

---
## 🤖 How the Algorithm Works
The algorithm mimics human-like exploration and exploitation strategies:

- **Exploration**: Occasionally guesses a less likely word to gather new information.
- **Exploitation**: Focuses on the most likely words based on feedback so far.
- The algorithm narrows down the possible words dynamically, just like a player would.  

### Why This Algorithm Handles Complexity:
- **Dynamic Word Lists**: The list of potential words changes after every guess, just like how a player would adjust based on feedback.
- **Deterministic Rewards**: Unlike classic MAB problems with random payouts, Wordle feedback is deterministic and depends on how well the guess matches the target word.

---
## Try it out your self



---

## 🤓 How to Contribute
1. Fork the repository.
2. Add new features, such as:
   - A leaderboard for user vs. algorithm scores.
   - Enhanced algorithms (e.g., more advanced heuristics or NLP-based approaches).
   - Dynamic word lists with customizable difficulty levels.
3. Submit a pull request. Let's improve this project together!

---

## 🙌 Acknowledgments
- **Wordle** by Josh Wardle for inspiring this project.
- **Streamlit** for making app development fun and easy.
- The open-source community for resources and feedback.

---

## 📝 License
This project is licensed under the **MIT License**. Feel free to use, modify, and share!

---
