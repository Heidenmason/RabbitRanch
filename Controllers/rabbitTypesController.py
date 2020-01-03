import DBConnection as DB
from models import RabbitTypes as PT
from models import pizzaToppings as PTo


class rabbitTypesController():

    @staticmethod
    def getRabbitTypes():
        try:
            listOfRabbitTypes = []

            conn = DB.DBConnection.getConnection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM rabbittypes")
            for row in cur:
                rabbitType = PT.RabbitTypes(row[0], row[1], row[2])  # typeID, name, ABV
                listOfRabbitTypes.append(rabbitType)
            return listOfRabbitTypes
        except Exception as e:
            print(e)
        finally:
            conn.close()

    #    @staticmethod
    #    def getPizzaToppings(typeID):
    #        try:
    #            listOfPizzaToppings = []
    #
    #            conn = DB.DBConnection.getConnection()
    #            cur = conn.cursor()
    #            cur.execute("SELECT * FROM pizzatoppings WHERE typeID = ?", (typeID))
    #            for row in cur:
    #                pizzaToppings = PTo.PizzaToppings(row[0], row[1], row[2], row[3], row[4], row[5])
    #                                                 #pizzaToppingID, typeID, sauce, meat, cheese, veggies
    #                listOfPizzaToppings.append(pizzaToppings)
    #            return listOfPizzaToppings
    #        except Exception as e:
    #            print(e)
    #        finally:
    #            conn.close()

    @staticmethod
    def getPizzaToppings(typeID):
        try:
            listOfPizzaToppings = []

            conn = DB.DBConnection.getConnection()
            cur = conn.cursor()
            typeIDSecure = typeID
            cur.execute("SELECT * FROM PizzaToppings WHERE typeID = ?", (typeIDSecure,))
            for row in cur:
                pizzaToppings = PTo.PizzaToppings(row[0], row[1], row[2], row[3], row[4], row[5])
                # pizzaID, typeID, sauce, meat, cheese, veggies
                listOfPizzaToppings.append(pizzaToppings)
            return listOfPizzaToppings
        except Exception as e:
            print(e)
        finally:
            conn.close()
