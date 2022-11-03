from source import User
from source import account
def transaction(item, user):
    if user.pay(item) :
        return "Transaction Complete"
    else:
        return "Transaction Failed"
restaurant = {
"burger": 10,
"softdrink": 5
}
bookstore = {
"comic": 10,
"magazine": 7,
"textbook": 50
}
john = User("John", 50)
print(transaction(restaurant["burger"], john)) # Output: Transaction Complete
print(transaction(restaurant["softdrink"], john)) # Output: Transaction Complete
print(transaction(bookstore["comic"], john)) # Output: Transaction Complete
print(transaction(bookstore["textbook"], john)) # Output: Transaction Failed
john.deposit(50)
print(transaction(bookstore["textbook"], john)) # Output: Transaction Complete