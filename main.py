from typing import List, Any

from PyQt5 import QtWidgets, uic, QtGui
from Controllers import rabbit_types_controller as rtc


class MyWindow(QtWidgets.QMainWindow):
    LIST_OF_RABBITS: List[Any] = []

    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('RabbitRanchMain.ui', self)
        self.setWindowIcon(QtGui.QIcon("images/barn-512.png"))  # Sets Start Bar Icon
        self.statusbar.showMessage('Ready')

        self.init()

    def init(self):
        global LIST_OF_RABBITS

        # label to image
        mypixmap = QtGui.QPixmap('images/image.jpg')
        self.labelImg.setPixmap(mypixmap)
        self.labelImg.resize(mypixmap.width(), mypixmap.height())
        self.labelImg.resize(126, 180)  # portrait
        # self.labelImg.resize(180,110) #landscape
        myscaledpixmap = mypixmap.scaled(self.labelImg.size())
        self.labelImg.setPixmap(myscaledpixmap)
        # label to image.

        LIST_OF_RABBITS = rtc.RabbitTypesController.getrabbittypes()

        for each in LIST_OF_RABBITS:
            self.cbPizzaTypes.addItem(each.get_name())

        self.twPizzaToppings.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Sauce"))
        self.twPizzaToppings.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Meat"))
        self.twPizzaToppings.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Cheese"))
        self.twPizzaToppings.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Veggies"))

        self.lbOrdered.hide()

        self.cbPizzaTypes.currentIndexChanged.connect(self.pizza_selected)
        self.btnOrder.clicked.connect(self.order)

        self.pizza_selected()

    def pizza_selected(self):
        try:
            cb_pizza_index = self.cbPizzaTypes.currentIndex()
            selected_pizza = LIST_OF_RABBITS[cb_pizza_index]
            pizza_type_id = selected_pizza.get_type_id_type()

            list_of_pizza_toppings = rtc.RabbitTypesController.getpizzatoppings(pizza_type_id)

            self.twPizzaToppings.setRowCount(0)
            for row_number, row_data in enumerate(list_of_pizza_toppings):
                self.twPizzaToppings.insertRow(row_number)
                self.twPizzaToppings.setItem(row_number, 0,
                                             QtWidgets.QTableWidgetItem(row_data.get_sauce()))
                self.twPizzaToppings.setItem(row_number, 1,
                                             QtWidgets.QTableWidgetItem(row_data.get_meat()))
                self.twPizzaToppings.setItem(row_number, 2,
                                             QtWidgets.QTableWidgetItem(row_data.get_cheese()))
                self.twPizzaToppings.setItem(row_number, 3,
                                             QtWidgets.QTableWidgetItem(row_data.get_veggies()))
        except Exception as e:
            print(e)

    def order(self):
        self.lbOrderStatus.hide()
        self.lbOrdered.show()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
