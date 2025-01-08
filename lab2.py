#zadanie 1
def greet(name):
    return 'Привет ' + name + '!'
print(greet('sasha'))

def square(number):
    return number ** 2
print(square(9))

def max_of_two(x, y):
    return max(x, y)
print(max_of_two(9, 10))

#zadanie 2
def describe_person(name, age=30):
    return name, age
print(describe_person('sasha'))

# zadanie 3
def is_prime(number):
    res = set()
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            res.add(i)
            res.add(i // 2)
    if len(res) == 0:
        return True
    else:
        return False
print(is_prime(11))