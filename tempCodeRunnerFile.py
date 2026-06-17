rint(f"{'Sr':<5}|{'Category':<14}|{'Name':<16}|{'Price':<10}|{'Brand'}")
print("-"*60)

for i, (category, name, price, brand) in enumerate(products, start=1):
    print(f"{i:<5}|{category:<14}|{name:<16}|₹{price:<10}|{brand}")
