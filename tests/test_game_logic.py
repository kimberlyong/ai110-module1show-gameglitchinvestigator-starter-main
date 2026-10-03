from pathlib import Path

from logic_utils import check_guess
from streamlit.testing.v1 import AppTest

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_new_game_clears_history():
    app_path = Path(__file__).resolve().parents[1] / "app.py"
    app = AppTest.from_file(str(app_path)).run()
    app.session_state["history"] = [42]

    new_game_button = next(
        button for button in app.button if button.label == "New Game 🔁"
    )
    new_game_button.click().run()

    assert app.session_state["history"] == []
