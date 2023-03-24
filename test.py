"""Tests functions in main"""
import pytest

from main import get_score, get_letters, get_letters_from_bag

def test_get_score_returns_number():
    """Tests that get score returns a number"""

    assert isinstance(get_score("WORD"), int)

def test_get_score_returns_correct_score():
    """Tests that get score returns correct score for a word"""

    assert get_score("WORD") == 8

def test_get_score_throws_error_if_not_word():
    """Tests get score throws error for number"""

    with pytest.raises(TypeError):
        get_score(37)

def test_get_letters_returns_a_list():
    """Tests get letters returns a list"""

    assert isinstance(get_letters(), list)

def test_get_letters_returns_7_letters():
    """Tests get letters returns 7 letters"""

    assert len(get_letters()) == 7

def test_get_letters_from_bag_returns_list():
    """Tests get letters from bag returns a list"""

    assert isinstance(get_letters_from_bag(), list)

def test_get_letters_from_bag_returns_7_letters():
    """Test get letters from bag returns 7 letters"""

    assert len(get_letters_from_bag()) == 7
