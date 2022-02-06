def add_time(start, duration, day = None ):
  days=["Monday" , "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
  if day != None:
    day = day.capitalize()
    gun=days.index(day)

  hour_c = int(start.split(":")[0])
  min_c = int(start.split(" ")[-2].split(":")[1])
  ek = start.split(" ")[1]
  hour_d = int(duration.split(":")[0])
  min_d = int(duration.split(":")[1])
  next_day = None
  flipper = {"AM": "PM", "PM": "AM"}
  end_minutes= min_c+min_d
  if end_minutes >= 60:
        hour_c +=1
        end_minutes = end_minutes%60

  end_hours=(hour_c+hour_d)%12
  amtopm = int((hour_c+hour_d)/12)

  end_minutes = end_minutes if end_minutes >= 10 else "0"+str(end_minutes)
  end_hours = end_hours = 12 if end_hours == 0 else end_hours
  next_day = True if (ek == "PM" and amtopm==1) or ( amtopm>=2) else None
  ek = flipper[ek] if amtopm % 2 ==1 else ek
  if day == None:
    if next_day == True and amtopm<=2:
        new_time =f"{end_hours}:{end_minutes} {ek} (next day)"
    elif (hour_d/24)>=1:
        new_time =f"{end_hours}:{end_minutes} {ek} ({int(hour_d/24)+1} days later)"
    else:
        new_time =f"{end_hours}:{end_minutes} {ek}"

  if day != None:
    if next_day == True and amtopm<=2:
        gun += 1
        gun = gun%7
        new_time =f"{end_hours}:{end_minutes} {ek}, {days[gun]} (next day)"
    elif (hour_d/24) >= 1:
        gun = gun + (int(hour_d/24)+1)
        gun = gun%7
        new_time =f"{end_hours}:{end_minutes} {ek}, {days[gun]} ({int(hour_d/24)+1} days later)"
    else:
        new_time =f"{end_hours}:{end_minutes} {ek}, {days[gun]}"
  return new_time
