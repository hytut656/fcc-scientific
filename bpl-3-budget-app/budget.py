class Category:
  def __init__(self, name: str):
    self.name : str = name
    self.ledger : list = []

  def __str__(self):
    result : str = ''
    result += self.name.center(30, '*') + '\n'

    for item in self.ledger:

      result += item['description'].ljust(23, ' ')[:23]
      result += '{0:>7.2f}\n'.format(item['amount'])

    result += 'Total: {0:.2f}'.format(self.get_balance())
    return result
  
  def deposit(self, amount, description : str = ''):
    self.ledger.append({
      'amount': amount, 
      'description': description
    })

  def withdraw(self, amount, description : str = ''):
    if not self.check_funds(amount):
      return False
    self.ledger.append({
      'amount': (amount * -1),
      'description': description
    })
    return True

  def get_balance(self):
    summed = 0.0
    for item in self.ledger:
      summed += item['amount']
    return summed
  
  def transfer(self, amount, other):
    if not self.check_funds(amount):
      return False
    self.ledger.append({
      'amount': amount * -1,
      'description': f'Transfer to {other.name}'
    })
    other.ledger.append({
      'amount': amount,
      'description': f'Transfer from {self.name}'
    })
    return True
  
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True
    

def create_spend_chart(categories):
  
  result : str = 'Percentage spent by category\n'
  
  max_name_len : int = 0
  total_spent : float = .0
  expenses : list = []
  names : list = []

  for category in categories:
    new_expense = sum([-x['amount'] for x in category.ledger if x['amount'] < 0])
    
    total_spent += new_expense
    max_name_len = max(max_name_len, len(category.name))

    expenses.append(new_expense)
    names.append(category.name)

  expenses = [(exp / total_spent) * 100 for exp in expenses]
  names   = [name.ljust(max_name_len, ' ') for name in names]

  for height in range(100, -1, -10):
    result += str(height).rjust(3, ' ') + '|'
    for exp in expenses:
      result += ' o ' if exp >= height else '   '
    result += ' \n'

  result += '    ' + '---' * len(names) + '-\n'

  for length in range(max_name_len):
    result += '    '
    for name in names:
      result += ' ' + name[length] + ' '
    result += ' \n'
    
  return result.strip('\n')
  
  