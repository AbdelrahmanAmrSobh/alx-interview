# Pascal triangle

## Goal

Create a method that check if list of boxes each box with list of keys can be unlocked.

## Knowledge

- First box is always unlocked.

- Keys can be repeated.

- There can be keys with no boxes.

## Thinking

- checking if each box can be opened is same as checking if each key can be obtained.

- if each key can be obtained we can check size of keys at the end and if it equal to number of boxes then we can open each box.

- but to do so we have to make conditions for adding keys, these conditions should ensure that keys are unique and useful.

- key must not be in keys and key must be of range(1, size)

## Solutaion

- Create list for keys.

- Create method that add keys (if key is in range and unique) add it.

- Use method to add first box (always unlocked)

- Iterate over keys and add each box using the method.

- if by the end you have len(keys) == size return True else return False

- Could be written as return len(keys) == size
