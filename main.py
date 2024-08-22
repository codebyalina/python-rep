def convert(amount, rate):
    return amount * rate

if __name__ == "__main__":
    amount = float(input("Enter amount in USD: "))
    rate = float(input("Enter conversion rate to another currency: "))
    converted_amount = convert(amount, rate)
    print(f"Converted amount: {converted_amount:.2f}")
