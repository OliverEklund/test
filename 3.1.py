print("Vilket av denna tre abonnemang är du intreserad i?")
print("Kontant: rekomenderad för högst 33 minuter av samtal per månad.")
print("Normal: Rekomenderad för mellan 33 och 66 minuter av samtal per månad.")
print("Plus: Rekomenderad för dom som har mer än 66 minuter av samtal per månad.")
while True:
    print("Upskatta hur många minuter du rigner per månad:")
    användar_val = input("")
    användar_val = int(användar_val)


    if användar_val <= 33:
        print(f"Du upskattar att du kommer ringa {användar_val}")
        print("Då är det bäst om du tar kontant.")

        YN = input("Skriv 1 för att acceptera, 2 för att neka: ")
        if YN == "1":
            break
        if YN == "2":
            print("OK")

    if användar_val > 33 and användar_val < 66:
        print(f"Du upskattar att du kommer ringa {användar_val}")
        print("Då är det bäst om du tar Normal.")

        YN = input("Skriv 1 för att acceptera, 2 för att neka: ")
        if YN == "1":
            break
        if YN == "2":
            print("OK")

    if användar_val >= 66:
        print(f"Du upskattar att du kommer ringa {användar_val}")
        print("Då är det bäst om du tar Plus.")

        YN = input("Skriv 1 för att acceptera, 2 för att neka: ")
        if YN == "1":
            break
        if YN == "2":
            print("OK")

print("Tack för att du valt ett abbonemang!")