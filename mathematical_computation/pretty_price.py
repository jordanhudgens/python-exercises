def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01

    return int(gross_price) + extension


print(pretty_price(3.20, 99))
print(pretty_price(3.99, 0.20))
print(pretty_price(3.20, .95))
print(pretty_price(3, 95))
print(pretty_price(3, 2))
