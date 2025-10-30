def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")

    print()
    for value in kwargs.values():
        print(value, end="\n")

shipping_label("Dr.", "Spongebob", "Squarepants", "III", street="123 Fake str.", apartment="100", state="MI")