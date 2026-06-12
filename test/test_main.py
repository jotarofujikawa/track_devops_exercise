from src.main import add
import pytest

def test_add():
  assert add(7, 2, 2) == 11
  assert add(5, 4, 3) == 12
  assert add(10, 10, 10) == 30
  assert add("a", 1, 3.6) == -1
  assert add("a", 1, 2) == -1
  assert add(1, None, "5") == -1
  assert add(-1, 5, 5) == -2
  assert add(11, 3, 5) == -2
  assert add(3, 3, 11) == -2
