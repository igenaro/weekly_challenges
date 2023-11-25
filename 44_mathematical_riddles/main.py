import random

def main():
    # Tu código va aquí
    op = random.randint(0,3)
    print(random_operation(random_number(11),op,random_number(11)))

def random_number(i):
    input_number = i-1
    residue = input_number % 5
    quotient = (input_number - residue)/5
    limit = 10**(quotient + 1)
    number = random.randint(0,limit - 1)
    return number

def random_operation(x,op,y):
    if op == 0:
        result = x + y
    elif op == 1:
        result = x - y
    elif op == 2:
        result = x * y
    elif op == 3:
        result =  int(x / random_divisor(x))
    return result

def random_divisor(x):
    divisores = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisores.append(i)
    
    divisor_aleatorio = random.choice(divisores)
    return divisor_aleatorio



if __name__ == "__main__":
    main()