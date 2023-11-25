import random
import time

def main():
    print('Tienes 3 segundos para resolver las operaciones:')
    input('Presiona ENTER para empezar')
    i = 1
    while True:
        x = random_operation(i)
        start_time = time.time()
        numero_string = input( print_operation(x))
        try:
            numero = int(numero_string)
        except:
            print('No ingresaste un número')
            break
        end_time = time.time()
        delta_time = end_time - start_time
        if delta_time >= 3:
            print('Persite, tardaste '+ str(delta_time) + ' segundos. Respuesta: ' + str(x[2]))
            break
        if numero == x[2]:
            i+=1
        else:
            print('Perdiste. Respuesta Correcta: ' + str(x[2]))
            break

def random_number(i):
    input_number = i-1
    residue = input_number % 5
    quotient = (input_number - residue)/5
    limit = 10**(quotient + 1)
    number = random.randint(0,limit - 1)
    return number

def random_operation(i):
    x = random_number(i)
    y = random_number(i)
    op = random.randint(0,3)
    if op == 0:
        result = x + y
    elif op == 1:
        result = x - y
    elif op == 2:
        result = x * y
    elif op == 3:
        y = random_divisor(x)
        result =  int(x / y)
    return [x,y,result,op]

def random_divisor(x):
    divisores = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisores.append(i)
    
    divisor_aleatorio = random.choice(divisores)
    return divisor_aleatorio

def print_operation(x):
    if x[3] == 0:
        op = '+'
    elif x[3] == 1:
        op = '-'
    elif x[3] == 2:
        op = '*'
    elif x[3] == 3:
        op = '/'
    operation ='Resuelve: ' + str(x[0]) + ' ' + op + ' ' + str(x[1]) + ' ' + '= '
    return operation 


if __name__ == "__main__":
    main()