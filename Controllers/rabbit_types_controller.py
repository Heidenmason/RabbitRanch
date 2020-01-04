import db_connection as db
from models import rabbit_types as pt
from models import pizza_toppings as pto


class RabbitTypesController:

    @staticmethod
    def getrabbittypes():
        try:
            list_of_rabbit_types = []

            conn = db.DBConnection.get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM rabbittypes")
            for row in cur:
                rabbit_type = pt.RabbitTypes(row[0], row[1], row[2])  # typeID, name, ABV
                list_of_rabbit_types.append(rabbit_type)
            return list_of_rabbit_types
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
    def getpizzatoppings(type_id):
        try:
            list_of_pizza_toppings = []

            conn = db.DBConnection.get_connection()
            cur = conn.cursor()
            type_id_secure = type_id
            cur.execute("SELECT * FROM PizzaToppings WHERE typeID = ?", (type_id_secure,))
            for row in cur:
                pizza_toppings = pto.PizzaToppings(row[0], row[1], row[2], row[3], row[4], row[5])
                # pizzaID, typeID, sauce, meat, cheese, veggies
                list_of_pizza_toppings.append(pizza_toppings)
            return list_of_pizza_toppings
        except Exception as e:
            print(e)
        finally:
            conn.close()
