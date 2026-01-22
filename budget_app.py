# freeCodeCamp Python Certification
# Certification Project: Build a Simple Budget App
# Author: R.K.Swetha

class Category:
    
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}" )
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self,amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = f"{item['description'][:23]:23}"
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    # Calculate total spent per category (withdrawals only)
    spent = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    # Calculate percentages rounded down to nearest 10
    percentages = [(s / total_spent) * 100 for s in spent]
    percentages = [int(p // 10) * 10 for p in percentages]

    # Build chart
    result = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        result += f"{i:>3}| "
        for p in percentages:
            result += "o  " if p >= i else "   "
        result += "\n"

    # Horizontal line
    result += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        result += "     "
        for name in names:
            result += (name[i] if i < len(name) else " ") + "  "
        if i != max_len - 1:
            result += "\n"

    return result

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
    
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "deposit")
food.withdraw(105.55)
food.withdraw(15.89)

clothing.deposit(500)
clothing.withdraw(33.40)

auto.deposit(1000)
auto.withdraw(50)

print(create_spend_chart([food, clothing, auto]))
