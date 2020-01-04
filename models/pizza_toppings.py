class PizzaToppings:

    def __init__(self, pizza_topping_id, type_id, sauce, meat, cheese, veggies):
        self.__pizza_topping_id = pizza_topping_id
        self.__type_id = type_id
        self.__sauce = sauce
        self.__meat = meat
        self.__cheeses = cheese
        self.__veggies = veggies

        # getters

    def get_pizza_topping_id(self):
        return self.__pizza_topping_id

    def get_type_id_top(self):
        return self.__type_id

    def get_sauce(self):
        return self.__sauce

    def get_meat(self):
        return self.__meat

    def get_cheese(self):
        return self.__cheeses

    def get_veggies(self):
        return self.__veggies
