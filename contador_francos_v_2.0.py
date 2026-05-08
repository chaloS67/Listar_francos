
import datetime
import locale

def configurar_idioma(): # Configura el idioma para los nombres de los dias
    try:
        locale.setlocale(locale.LC_ALL, "es_ES.utf8")
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, "es_AR.utf8")
        except locale.Error:
            pass


def pedir_fecha():
    while True:
        fecha_texto = input ("ingresar fecha del ultimo franco (AAAA-MM-DD)")
        try:
           return (datetime.datetime.strptime(fecha_texto, "%Y-%m-%d").date()) # Devuelve la fecha como dato
           
        except ValueError:
            print("el formato de fecha es incorrecto. Por favor ingrese de nuevo la fecha")

def pedir_cantidad_franco():

    while True:
        cantidad = input ("ingresar cantidad de francos que tuviste (1 o 2)")
        if cantidad in ["1","2"]:
           return int (cantidad)
        print ("debe ingresar 1 o 2")
    

def calcular_francos (fecha_inicio, cantidad_francos):
    resultados = []
    año_inicio = fecha_inicio.year

    while fecha_inicio.year == año_inicio: # mientras sea dentro del mismo año

        if cantidad_francos == 1:
           
            franco_1 = fecha_inicio + datetime.timedelta(days=7) # CALCULA PRIMER FRANCO 6 dias trabajados 
            franco_2= fecha_inicio + datetime.timedelta(days=8)
        
        
            resultados.append(franco_1)
            resultados.append(franco_2)

            fecha_inicio = franco_2 
            cantidad_francos = 2 # establesco la cantidad de francos para que entre en el siguiente

        else:
      
            
            franco = fecha_inicio + datetime.timedelta(days=7)# aigno la la fecha
           
            resultados.append(franco)
       
            fecha_inicio= franco # establesco la fecha luego de mi franco
            cantidad_francos = 1 # establesco la cantidad de franco siguientes
       
    return resultados

def mostrar_resultados(francos):
    print ("\n === PROXIMOS FRANCOS === \n")

    for fecha in francos:
        print(fecha.strftime("%d de %B - %A"))

def main ():
    configurar_idioma()

    print("=== Calculadora de francos para playeros ===\n")

    fecha_inicio = pedir_fecha()
    cantidad_francos = pedir_cantidad_franco()

    francos = calcular_francos(fecha_inicio, cantidad_francos)

    mostrar_resultados(francos)


if __name__ == "__main__":
    main()
