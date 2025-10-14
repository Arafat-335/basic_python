expenses = []


def add_expense():
    description = input("enter your describtion: ").strip()
    amount = input('enter your amount: ')
    expense = {
        "description": description,
        "amount": int(amount)
        }
    expenses.append(expense)
    print("expense added")
    
def view_expenses():
    if not expenses:
        print("expense not added")
        return
    print("/n----your expenses-----")
    for index, exp in enumerate(expenses, 1):
        print(index,exp.get('description'), " = ", exp.get("amount"))

def total_spending():
    total= sum(expense["amount"] for expense in expenses)
    print(f"total spend: tk {total:.2f}")
    
while True:
    print("/n----your expenses-----")
    print("1. expense added")
    print("2. view all expenses")
    print("3. total_spending")
    print("4. exit")

    choose = input("choose options(1-5): ").strip()
    if choose == "1":
        add_expense()
    elif choose == "2":
        view_expenses()
    elif choose == "3":
        total_spending()
    elif choose == "4":
        exit()

    else:
      print("Invalid choice. Please pick 1–5.")