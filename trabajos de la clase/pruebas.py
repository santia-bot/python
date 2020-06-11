cafe_chico = {"Expresso": 15,"Capuchino": 20,"Americano": 18,"Cafe con leche": 22,"Cafe au lait": 25,"Cafe moca":24,"Caramelo macchiato": 27}
cafe_grande ={"Expresso": 25,"Capuchino": 35,"Americano": 33,"Cafe con leche": 38,"Cafe au lait": 45,"Cafe moca": 43,"Caramelo macchiato": 48}

cafe =input("cafe:").capitalize()
grande_pequeño = input("grande o chico")
if grande_pequeño =="grande":
    print(cafe_grande.get(cafe))