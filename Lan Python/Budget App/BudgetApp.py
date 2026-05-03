class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description = ""):
        self.ledger.append({"Amount": amount, "Description": description})
        
    
    def withdraw(self, amount, description = ""):
           if self.check_funds(amount):
               self.ledger.append({"Amount": -amount, "Description": description})
               return True
           else:
               return False
       
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True
    
    def get_balance(self):
        self.balance = 0
        for i in self.ledger:
            self.balance += i['Amount']
        return self.balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False
    def display(self):
        
        self.output = f"{self.name.center(30, '*')}\n"
        self.total = 0
        for i in self.ledger:
            self.output += f"{i['Description'][:23]:23}{i['Amount']:>7.2f}\n"
            self.total += i['Amount']
        self.output += f"Total: {self.total:.2f}"
        return self.output
    
    def __str__(self):
        return self.display()

def create_spend_chart(categories):
    # Calculate total spent across all categories (withdrawals only)
    total_spent = 0
    category_spent = []
    
    for category in categories:
        spent = sum(-entry['Amount'] for entry in category.ledger if entry['Amount'] < 0)
        category_spent.append(spent)
        total_spent += spent
    
    # Calculate percentages rounded down to nearest 10
    percentages = []
    if total_spent > 0:
        percentages = [int((spent / total_spent) * 100 // 10) * 10 for spent in category_spent]
    else:
        percentages = [0] * len(categories)
    
    # Build chart title
    chart = "Percentage spent by category\n"
    
    # Build y-axis with bars
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o "
            else:
                chart += "  "
        chart += "\n"
    
    # Build horizontal line
    chart += "    " + "-" * (len(categories) * 2 + 1) + "\n"
    
    # Build category names vertically
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + " "
            else:
                chart += "  "
        chart += "\n"
    
    return chart

# Test the Category printing and spend chart
if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "Initial deposit")
    food.withdraw(50, "Groceries")
    food.withdraw(20, "Restaurant")
    
    entertainment = Category("Entertainment")
    entertainment.deposit(500, "Initial deposit")
    entertainment.withdraw(30, "Movie")
    
    food.transfer(100, entertainment)  # Transfer to the actual entertainment object
    food.get_balance()
    entertainment.get_balance()
    
    shopping = Category("Shopping")
    shopping.deposit(800, "Initial deposit")
    shopping.withdraw(100, "Clothes")
    shopping.get_balance()
    
    print(f"Check funds result: {shopping.check_funds(1050)}")  # Should print: False

    
    print(food)
    print("\n")
    print(entertainment)
    print("\n")
    print(shopping)
    print("\n")
    print(create_spend_chart([food, entertainment, shopping]))