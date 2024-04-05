import pyfiglet

text = 'enter symbol text'
result = pyfiglet.figlet_format(text, font='slant')
print(result)

result = pyfiglet.figlet_format(text, font='graffiti')
print(result)

result = pyfiglet.figlet_format(text, font='starwars')
print(result)

result = pyfiglet.figlet_format(text, font='poison')
print(result)