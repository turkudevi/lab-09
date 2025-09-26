count = 0
sum_vlera = 0.0
min_vlera = None
max_vlera = None

while True:
    txt = input("Vlera: ").lower().strip()
    if txt == "stop":
        break
    try:
        vlera = float(txt)
        count += 1
        sum_vlera += vlera
        if min_vlera is None or vlera < min_vlera:
            min_vlera = vlera
        if max_vlera is None or vlera > max_vlera:
            max_vlera = vlera
    except ValueError:
        print("Vlerë e pavlefshme")
        continue

print("-----------------")
if count == 0:
    print("Nuk u dhanë të dhëna.")
else:
    mesatare = sum_vlera / count
    print("Count:", count)
    print("Min:", round(min_vlera, 2))
    print("Max:", round(max_vlera, 2))
    print("Mesatare:", round(mesatare, 2))
