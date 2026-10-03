# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->
I asked both models to fix the bug where the game incorrectly gave hints for higher or lower


| | Model A | Model B |
|-|Copilot  |Claude Code|
| **Model name** |Copilot|Claude Code|
| **Response summary** 
    |Fixed logic immediately and gave 1 sentence of the changes made|Established context of what was happening, referenced changes and the lines of code, and noted other possible errors that the user might want to keep in mind. |
| **More Pythonic?** |Copilot was very direct and focused on making the change|CC was more pythonic as it just gave more and clearer explanations of what it did|
| **Clearer explanation?** | |X|

**Which did you prefer and why?**
I preferred the Claude Code response because it first explained the context of what was happening. It also directly referenced lines like app.py:99 so that I could also pinpoint where the problem was. Additionally, it gave a nice preview of the changes it was going to make and gave me some steps if the problem continued. Claude was also better about asking to make changes before implementing them. 

<!-- Your conclusion -->
I preferred Claude Code solution as I think it was more beginner friendly. As someone who is still learning python, I liked having context, lines specifically cited, and a AI buddy rather than a AI do-er. 
