class RabbitTypes:

    def __init__(self, type_id_type, name, abv):  # constructor
        self.__type_id_type = type_id_type
        self.__name = name
        self.__abv = abv

    # setters
    def set_name(self, name):
        self.__name = name

    def set_abv(self, abv):
        self.__abv = abv

    # Getters
    def get_type_id_type(self):
        return self.__type_id_type

    def get_name(self):
        return self.__name

    def get_abv(self):
        return self.__abv
