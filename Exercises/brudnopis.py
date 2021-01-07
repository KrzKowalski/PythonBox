def format_name(f_name, l_name):
    # f_name = input("What's your name?")
    # l_name = input("What's your surname?")

    return f_name.title(), l_name.title()

formatted = format_name("KrzyszTOF", "KOWALSKI")
print(type(formatted))