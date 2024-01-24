def add_time(start, duration, day_of_the_week='none'):
  new_time = ''
  weekdays = [
      'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
      'sunday', 'none'
  ]

  # Extract data
  hour = int((start.split()[0]).split(':')[0])
  minute = int((start.split()[0]).split(':')[1])
  noon = start.split()[1]
  weekday = weekdays.index(day_of_the_week.lower())
  days_later = 0

  # Convert to 24h mode
  if noon == 'PM':
    hour += 12

  # Extract duration data
  hour_to_add = int(duration.split(':')[0])
  minute_to_add = int(duration.split(':')[1])

  # Do addition
  new_minute = (minute + minute_to_add) % 60
  new_hour = hour + hour_to_add + (minute + minute_to_add) // 60
  days_later = new_hour // 24
  new_weekday = (weekday + days_later) % 7 if weekday != 7 else 7
  # Format back to 12h mode
  new_hour = new_hour % 24
  noon = 'AM' if new_hour < 12 else 'PM'
  new_hour = new_hour % 12 if (new_hour != 12 and new_hour != 0) else 12

  # Assemble output
  new_time = f'{new_hour}:'
  if new_minute < 10:
    new_time += '0'
  new_time += f'{new_minute} {noon}'
  if new_weekday != 7:
    new_time += f', {weekdays[new_weekday].capitalize()}'
  if days_later != 0:
    if days_later == 1:
      new_time += ' (next day)'
    else:
      new_time += f' ({days_later} days later)'

  return new_time
