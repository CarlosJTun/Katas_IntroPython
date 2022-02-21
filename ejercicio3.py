asteroide_size = 40
asteroide_vel = 35

if asteroide_vel < 20:
    print(f"El asteroide viaja muy lento, no será detectable al entrar a la atmosfera")
elif asteroide_vel >= 20:
    if asteroide_vel > 25:
        print(f"Se emite alerta por velocidad del asteroide. Viaja a {asteroide_vel} km/s. Será visible el destello al entrar a la atmosfera.")
    else:
        print(f"El asteroide va a mostrar un destello al entrar a la atmosfera.")

if asteroide_size <= 25:
    print(f"Por su tamaño se quemará al entrar a la atmosfera")
elif asteroide_size > 25 and  asteroide_size < 1000:
    print(f"Por el tamaño representa un alto peligro a la población, causará mucho daño.")
else:
    print(f"El tamaño es catastrófico, Look Up.")
