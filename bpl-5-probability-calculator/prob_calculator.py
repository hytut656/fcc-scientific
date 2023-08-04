import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **args):
    
    self.contents = []
    
    for key, value in args.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num):
    
    res_list = []
    
    if num >= len(self.contents):
      return self.contents

    for _ in range(num):
        color = self.contents.pop(random.randrange(len(self.contents)))
        res_list.append(color)
      
    return res_list
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  final = 0
  
  for _ in range(num_experiments):
    
    cpy_hat = copy.deepcopy(hat)
    tmp = cpy_hat.draw(num_balls_drawn)
    success = True
    
    for key, value in expected_balls.items():
      if tmp.count(key) < value:
        success = False
        break
        
    if success:
      final += 1
      
  return final / num_experiments