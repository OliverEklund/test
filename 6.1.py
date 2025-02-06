nummer = []
while True:
    heltal = input("Skriv in ett heltal:" )
    heltal = int(heltal)
    if heltal not in nummer:
        nummer.append(heltal)
    YN = input("[1] Ett till heltal, [2] Skriv ut: ")
    if YN == "2":
        print(f"{nummer}")