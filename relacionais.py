'''
    and
V | V = V
V | F = F
F | V = F
F | F = F
'''


a = 5
b = 6
c = 10

print(f'"a" é maior ou igual "c": {a >= c}')
print(f'"a" é maior que "c": {not b == a}')
print(f'"a" é menor que "c": {c < b}')
print(f'"c" é maior que "a": {a < c}')
print(f'"a" é maior ou igual "c": {a >= c}')

print(f'c >= a e b == a {a >= c and b == a}')
print(f'c <= a e b == a {a <= c or b == a}')