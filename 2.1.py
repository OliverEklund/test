print("Vad står mätarställningen på?")
dagens_mätare = input()
dagens_mätare = int(dagens_mätare)

print("Vad stod mätarställningen på föra året?")
årets_mätare = input()
årets_mätare = int(årets_mätare)

print("Hur många liter bensin har använts?")
liter_använt = input()
liter_använt = float(liter_använt)

mil_körda = dagens_mätare - årets_mätare
liter_per_mil = liter_använt / mil_körda

print(f"antal mil körda ({mil_körda})")
print(f"antal liter bensin ({liter_använt})")
print(f"Förbrukning per mil ({liter_per_mil})")