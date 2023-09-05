def main():
    due = 50
    accepted = [25,10,5]
    while due >0:
        print(f"Amount Due: {due}")
        amount = int(input("Insert Coin: "))
        if amount in accepted:
            due = due-amount

    print (f"Change Owed: {abs(due)}")

main()