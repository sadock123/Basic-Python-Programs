money_transaction= int(input("Enter the amount to be transcated"))
bank_balance= int(input("Enter the bank balance"))
if (money_transaction % 5==0):
    if (bank_balance > money_transaction):
        bank_balance= bank_balance- money_transaction - 0.5
        print("the money transcated is",money_transaction)
        print("the current balance is",bank_balance)
    else:
        print("insufficient balance")
else:
    print("Incorrect money transcation")