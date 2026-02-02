class Solution:
  def fizzBuzz(self, n: int) -> list[str]:
    answers = []
    for answer in range(1, n+1):
      if answer % 5 == 0 and answer % 3 == 0:
        answers.append("FizzBuzz")
      elif answer % 3 == 0:
        answers.append("Fizz")
      elif answer % 5 == 0:
        answers.append("Buzz")
      else:
        answers.append(f"{answer}")
    return answers