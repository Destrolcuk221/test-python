import datetime
dia=int(input("Dia de nacimiento : "))
mes=int(input("Mes de nacimiento : "))
año=int(input("Año de nacimiento : "))

fecha_de_nacimiento=datetime.datetime(año,mes,dia)

fecha_de_hoy=datetime.datetime.now()

diferencia=fecha_de_hoy -  fecha_de_nacimiento

dia_vividos=diferencia.days

segundos_vividos=diferencia.seconds

horas_vividas,segundos_vividos=divmod(segundos_vividos,3600)
minutos_vividos,segundos_vividos = divmod(segundos_vividos,60)

mensaje="Has vivido {} dias(s),{} horas(s),{} minutos(s) y {} segundo(s)".format(
    dia_vividos,horas_vividas,minutos_vividos,segundos_vividos
)

print(mensaje)