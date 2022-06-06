# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15)
food.withdraw(15.89, "restaurant and more food for dessert")
# # print(food.ledger)
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
# print(food.percentage())
# # print(len(clothing.ledger))
# # print(len(food.ledger))
# # print(clothing.ledger)
# # print(food.ledger)
# auto = budget.Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)
def test_create_spend_chart(self):
        self.food.deposit(900, "deposit")
        self.entertainment.deposit(900, "deposit")
        self.business.deposit(900, "deposit")
        self.food.withdraw(105.55)
        self.entertainment.withdraw(33.40)
        self.business.withdraw(10.99)
# test_create_spend_chart(self)
# print(food)
# print(clothing)
# print(auto)

# print(create_spend_chart([food, clothing, auto]))
# print(create_spend_chart([food]))
# Run unit tests automatically
main(module='test_module', exit=False)