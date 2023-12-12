from objects.cars import Cars

blue_car = Cars("blue", 0)
red_car = Cars("red", 0)



print(blue_car.mileage)

blue_car.advance(blue_car)
print(blue_car.mileage)

blue_car.advance(blue_car)
print(blue_car.mileage)