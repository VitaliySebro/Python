import math

def process_input(file_path='input.txt'):
    with open(file_path, 'r') as file:
        x = float(file.read())
        l = math.e**(2*x - 1.3) / (math.cbrt(abs(x)) + 2)
        a = 1 + (l/3)

    return x, l, a

result = process_input()

result_str = f"x = {result[0]}\nl = {result[1]}\na = {result[2]}"
print(result_str)

with open("output.txt", 'w') as f:
    f.write(result_str)