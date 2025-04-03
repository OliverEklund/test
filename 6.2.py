# Station_1 = {'namn':"Mätstation 1", 'temp': 0}
# Station_2 = {'namn':"Mätstation 2", 'temp': 0}
# Station_3 = {'namn':"Mätstation 3", 'temp': 0}
# Station_4 = {'namn':"Mätstation 4", 'temp': 0}

# Station_1['temp'] = int(input("skriv temperatur:" ))
# Station_2['temp'] = int(input("skriv temperatur:" ))
# Station_3['temp'] = int(input("skriv temperatur:" ))
# Station_4['temp'] = int(input("skriv temperatur:" ))

# total = Station_1['temp'] + Station_2['temp'] + Station_3['temp'] + Station_4['temp']
# medelvärde = total/4
# print(f"{medelvärde}")



def get_station_temperature():
    try:
        temp = int(input("Skriv in temp: "))
        return temp
    except ValueError:
        print(ValueError)

temperatures = []

for i in range(0, 5):
    temp = get_station_temperature()
    temperatures.append(temp)

print(temperatures)