import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    self.original_contents = []
    for key, value in kwargs.items():
      for _ in range(value):
        self.contents.append(key)
        self.original_contents.append(key)

  def refill(self):
    self.contents = copy.deepcopy(self.original_contents)

  def draw(self, num):
    drawn = []
    for _ in range(num):
      if len(self.contents) == 0:
        self.refill()
      item = random.choice(self.contents)
      drawn.append(item)
      self.contents.remove(item)
    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_successes = 0.0

  for _ in range(num_experiments):
    hat.refill()
    hand = hat.draw(num_balls_drawn)
    #print(hand)
    if compare_hand(hand, expected_balls):
      num_successes += 1
  return num_successes / num_experiments


def compare_hand(hand, expected):
  for key in expected:
    if hand.count(key) < expected[key]:
      return False
  return True
