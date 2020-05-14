# Functions as desired

weight = int(input('What is your weight? > '))
unit = input('Is this weight in Lbs or Kg? > ').lower

while True:
    if unit == 'lbs':
        converted = weight * 0.45
        print(f'You weigh {int(converted)} kilos.')
        break
    if unit == 'kg':
        converted = weight * 2.2
        print(f'You weigh {int(converted)} pounds.')
        break
    else:
        print("Please enter a valid unit of measurement")
