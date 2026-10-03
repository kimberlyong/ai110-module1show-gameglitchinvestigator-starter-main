# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   The game is meant to be a fun way to guess a target number from 1 - 100 within a certain number of attempts. 
- [ ] Detail which bugs you found.
   The game incorrectly provided hints making it impossible to win if you followed the hints. It also was not resetting the history on the game so checking the history merged different games into one. 
- [ ] Explain what fixes you applied.
   I added a history reset and changed the messages on go higher or lower to be correct. I also had AI refactor the code. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 25
2. Game returns "Go Higher" and score updated
3. User enters a guess of 75
4. Game returns "Go Higher", score updated, and history updated
5. User correctly guesses 90
6. Game returns score 
7. User clicks New Game 
8. Game resets number, score, and history 

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
=========================================================== test session starts ============================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\kimbe\OneDrive\CodePath\ai110-module1show-gameglitchinvestigator-starter-main
plugins: anyio-4.15.1
collected 4 items                                                                                                                           

tests\test_game_logic.py ....                                                                                                         [100%]

============================================================ 4 passed in 1.17s ======================================================


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
