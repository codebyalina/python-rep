def convert(amount, rate):
    return amount * rate

def get_rate(currency):
    rates = {
        'EUR': 0.85,
        'GBP': 0.75,
        'JPY': 110.0
    }
    return rates.get(currency, None)

if __name__ == "__main__":
    amount = float(input("Enter amount in USD: "))
    currency = input("Enter target currency (EUR, GBP, JPY): ")
    rate = get_rate(currency)
    if rate is None:
        rate = float(input("Enter custom conversion rate: "))
    converted_amount = convert(amount, rate)
    print(f"Converted amount: {converted_amount:.2f} {currency}")
