# ЧАСТЬ I : Основы Python
# ГЛАВА 1 Python: с чем его едят
# Пример 1.1. countdown.py
for countdown in 5, 4, 3, 2, 1, "hey!":
 print(countdown)
 # Пример 1.2. spells.py
 spells =[
  "Riddikulus",
  "Wingardium Leviosa!",
  "Avada Kedavra!",
  "Expectro Patronum!",
  "Nox!",
  "Limos!",
 ]
 print(spells[3])
#Пример 1.3. quotes.py
quotes = {
 "Moe": "A wise guy, huh?",
 "Larry": "Ow!",
 "Curly": "Nyuk nyuk!",
 }
stooge = "Curly"
print(stooge, "says:", quotes[stooge])
#ГЛАВА 3 Числа
#Упражнения
print(60*60)
seconds_per_hour=3600
print(seconds_per_hour)
seconds_per_day = 24*seconds_per_hour
print(seconds_per_day)
seconds_per_day/seconds_per_hour
print(seconds_per_day/seconds_per_hour)
seconds_per_day//seconds_per_hour
print(seconds_per_day//seconds_per_hour)
#ГЛАВА 4 Выбираем с помощью оператора if
#Упражнения 4.1
secret=9
guess=9
if guess<secret:
 print('too low')
elif guess>secret:
 print('too high')
else:
 print('just right')
 #4.2
 small = False
 green = True
 if small:
  if green:
   print('вишня')
  else:
   print('горошек')
 else:
  if green:
   print('арбуз')
  else:
   print('тиква')