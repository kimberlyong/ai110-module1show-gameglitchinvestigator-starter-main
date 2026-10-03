# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game seemed functional with clear buttons to submit a guess or to restart the game. However, after running it, a couple of errors became clear. The game was still functional as the bugs didn't affect the usability of the site, just how the game functioned. After clicking submit guess once, the history section in the Developer Debug Info didn't seem to work until you ran it again. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The first bug that stood out was that the hints to go higher or lower were backwards making it impossible to win if you followed the clues. Another problem was that when you clicked "New Game" the history didn't reset while the number changed, making it harder to remember what you guessed. another issue was that sometimes when "Submit Guess" was clicked, it didn't give a hint (even when show hint was selected) until you clicked "Submit Guess" again. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input      | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location|
|-------     |-------------------|-----------------|------------------------|
|   25       | "Go HIGHER!"      | "Go LOWER!"     | None                   | check_guess in app.py
|Submit Guess| Hint to appear    | Nothing         | None                   | check_guess in app.py
|New Game    | History cleared   | History not clear| None                  | new_game in app.py

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI was able to refactor the code so that the functions from app.py were moved to logic_utils.py. The program continue to run smoothly even with the fixes to the bugs. AI suggested moving the each individual function to the logic_utils.py and I was able to accept each change and ensure there wre no changes to the result. 


- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
I asked Copilot to add one line specifically in the app.py file to reset the History. Copilot ended up refactoring app.py and logic_utils.py in addition to adding the line. I undid the changes to make sure the original change worked before asking specifically for it to refactor the code. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I double checked the changes to make sure I understood what was changes/added. Then I went to the app page and ran through the game a few times to check for multiples cases how it responded. If necessary, I would also ask Copilot to generate a pytest to check. If the code worked and the specific change didn't come up again, I decided the bug was fixed. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran a pytest and in the terminal it said 4 passed. The test was to check if the History would clear when a new game started. This meant that the 4 tests that it tested all worked and showed that the changes made to app.py functioned correctly. 


- Did AI help you design or understand any tests? How?
It helped me design the pytests to check if the code worked. For one bug, it added in a placeholder value then checked to see if clicking "New Game" would reset the space. It worked successfully and all 4 test cases passed. When the pytest did not pass, I was able to go through again and identify the problem with the refactoring before I tested the page myself. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
