import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break
print('Congratulations, you figured it out.')

print('jk, how about trying again in spinach?')
while True:
    prompt = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
    response = pyip.inputYesNo(prompt, yesVal='sí', noVal='no')
    if response == 'sí':
        break
print('Felicitaciones, lo descubriste')
