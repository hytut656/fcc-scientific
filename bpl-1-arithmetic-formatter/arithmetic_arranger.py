def arithmetic_arranger(problems, calc=False):
  
  res_list = []
  
  # Check problem length
  if len(problems) > 5:
    return "Error: Too many problems."
  
  for problem in problems:

    # 3 is minimum when 0 + 0 for ex.
    max_word = 3
    
    # Split to get 2 numbers and the operator
    str_list = problem.split(sep=' ')

    # Check operator
    if str_list[1] not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    # Check numbers
    for string in str_list[::2]:
      try:
        
        # Too big
        if int(string) > 9999:
          return "Error: Numbers cannot be more than four digits."
          
      # Not a number
      except ValueError:
        return "Error: Numbers must only contain digits."

      # End of Validity checks

      max_word = max(max_word, len(string) + 2)

    # Add item to dictionary
    add_item = {
      'row1': str_list[0],
      'row2': str_list[2],
      'operator': str_list[1],
      'length': max_word
    }

    res_list.append(add_item)

  # Generate string
  result = ''

  # 1st row
  for item in res_list:
    for _ in range(item['length'] - len(item['row1'])):
      result += ' '
    result += item['row1']
    if item != res_list[-1]:
      result += '    '
  result += '\n'

  # 2nd row
  for item in res_list:
    result += item['operator']
    for _ in range(item['length'] - len(item['row2']) - 1):
      result += ' '
    result += item['row2']
    if item != res_list[-1]:
      result += '    '
  result += '\n'

  # 3rd row
  for item in res_list:
    for _ in range(item['length']):
      result += '-'
    if item != res_list[-1]:
      result += '    '

  # Check for end param
  if not calc:
    return result
    
  result += '\n'
  
  # 4th row
  for item in res_list:
    res = eval(f"{item['row1']} {item['operator']} {item['row2']}")
    for _ in range(item['length'] - len(str(res))):
      result += ' '
    result += str(res)
    if item != res_list[-1]:
      result += '    '

  return result