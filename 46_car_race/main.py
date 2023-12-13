from objects.cars import Cars
from objects.pista import Pista
import time

def turn(road, car):
    l = len(road)
    road_list = list(road)
    if car.working:
        car.advance()
        if (l-1-car.mileage) <= 0:
            road_list[0] = car.icon
            car.winner_flag()
        else:
            if road_list[l-1-car.mileage] == "T":
                road_list[l-1-car.mileage]= "*"
                car.crash()
            else:
                road_list[l-1-car.mileage] = car.icon
    else:
        road_list[l-1-car.mileage]= car.icon
        car.repair()
    road = ''.join(road_list)
    return print(road + " " + car.color)

def init_turn(road,car):
    l = len(road)
    road_list = list(road)
    road_list[l-1]= car.icon
    road = ''.join(road_list)
    return print(road + " " + car.color)

blue_car = Cars("blue","#")
red_car = Cars("red","#")

# Longitud de la pista
length = 30

blue_road = Pista(length, blue_car.icon).run()
red_road = Pista(length,red_car.icon).run()

turno = 0

while True:
    print("Turno: "+ str(turno))
    if turno == 0:
        init_turn(blue_road,blue_car)
        init_turn(red_road,red_car)
    else:
        turn(blue_road,blue_car)
        turn(red_road,red_car)
        if (blue_car.winner and red_car.winner):
            print("Draw")
            break
        if (blue_car.winner and (not red_car.winner)):
            print("The winner is "+blue_car.color+" car")
            break
        if ((not blue_car.winner) and red_car.winner):
            print("The winner is "+red_car.color+" car")
            break
    
    turno += 1
    time.sleep(1)
