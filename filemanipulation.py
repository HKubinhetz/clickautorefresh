import re

with open('coordinates.txt', "r+") as f:
    data = f.read()
    numbers = re.findall(r'\d+', data)
    print(numbers)

    f.write('500\n')
    f.write('600\n')
    f.write('700\n')
    f.write('800\n')

    # f.seek(0)
    # f.write(output)
    # f.truncate()