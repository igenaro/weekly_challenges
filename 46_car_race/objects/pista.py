import random

class Pista:

    def __init__(self, length, car_icon):
        self.length = length
        self.car_icon = car_icon

    
    # Inicia una pista de longitud deseada
    def init_pista(self):
        pista_string = "_"*self.length
        return pista_string
    
    # Imprime el carro y los arboles en la pista.
    # Falta agregar que dos arboles no se sobrepongan
    def cars_and_trees_in_road(self, road):
        num_trees = random.randint(1, 3)
        l = len(road)
        road_list = list(road)
        for i in range(num_trees):
            pos_tree = random.randint(1,l-2)
            road_list[pos_tree] = "🌲"
        road_list[0] = "🏁"
        road = ''.join(road_list)
        return road

    
    def run(self):
        road = self.init_pista()
        road = self.cars_and_trees_in_road(road)
        return road
