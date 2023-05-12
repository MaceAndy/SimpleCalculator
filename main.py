def dodawanie(a, b):
    return a + b

def odejmownie(a, b):
    return a - b

def mnozenie(a, b):
    return  a * b

def dzielenie(a, b):
    if b == 0:
        raise print("NIgdy cholero nie dziel przez zero.")
    return a / b

while True:

    print("Wybierz rodzaj działania matematycznego.")
    print("1.Dodawanie")
    print("2.Odejmowanie")
    print("3.Mnożenie")
    print("4.Dzielenie")
    print("5. Zakończ Program")


    wybor = input("Wybierz działanie.")
    if wybor == "5":
        break
    liczba1 = float(input("wprowadz liczbe: "))
    liczba2 = float(input("Wprowadz liczbę: "))


    if wybor == "1":
        print(liczba1, "+", liczba2, "=", dodawanie(liczba1, liczba2))
    elif wybor == "2":
        print(liczba1, "-", liczba2, "=", odejmownie(liczba1, liczba2))
    elif wybor == "3":
        print(liczba1, "*", liczba2, "=", mnozenie(liczba1, liczba2))
    elif wybor == "4":
        print(liczba1, "/", liczba2, "=", dzielenie(liczba1, liczba2))
    else:
        print("TO NIE DZIAŁA.")
