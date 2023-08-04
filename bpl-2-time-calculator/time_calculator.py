def add_time(start, duration, weekday=None):

  weekdays = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
  ]

  # If weekday_num = 0, means index is not given.
  weekday_num: int = 0
  if weekday:
    weekday_num = weekdays.index(weekday.lower()) + 1
  
  start_list = start.split(sep=' ')[0]
  
  am_pm = start.split(sep=' ')[1]
  
  start_h: int = int(start_list.split(sep=':')[0])
  start_m: int = int(start_list.split(sep=':')[1])

  dur_h: int = int(duration.split(sep=':')[0])
  dur_m: int = int(duration.split(sep=':')[1])

  days: int = 0

  # Swap to 24h system
  if am_pm == 'PM' and start_h != 12:
    start_h += 12

  if am_pm == 'AM' and start_h == 12:
    start_h = 0

  # Sum up minutes and iterate hours
  start_m += dur_m
  while start_m >= 60:
    start_h += 1
    start_m -= 60  

  # Sum up hours and iterate days
  start_h += dur_h
  while start_h >= 24:
    days += 1
    start_h -= 24

  # Swap back to 12h (AM PM) system
  if start_h > 12:
    am_pm = 'PM'
    start_h -= 12
  elif start_h == 12:
    am_pm = 'PM'
  elif start_h == 0:
    am_pm = 'AM'
    start_h += 12
  else:
    am_pm = 'AM'

  # Print
  format_min = str(start_m) if start_m > 9 else '0' + str(start_m)
  result = f"{start_h}:{format_min} {am_pm}"
  if weekday_num:
    week_i_now = weekday_num - 1 + days
    while week_i_now >= len(weekdays):
      week_i_now -= len(weekdays)
    result += f", {weekdays[week_i_now].capitalize()}"
  if days == 1:
    result += " (next day)"
  if days > 1:
    result += f" ({days} days later)"
  
  return result