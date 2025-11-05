# Buscar país por nombre

def buscar_pais(pais_buscar):
    coincidencias = []
    if pais_buscar == "":
        print("Debe ingresar algún caracter para poder realizar una búsqueda")
        return
    elif pais_buscar == " ":
        print("Debe ingresar algún caracter para poder realizar una búsqueda")
        return
    else:
        with open("ListaPaises.csv", "r") as archivo:
            archivo.readline()
            for i in archivo:
                linea_archivo = i.split(",")
                pais = str(linea_archivo[0])
                if pais_buscar.lower() in pais.lower():
                    coincidencias.append(linea_archivo[0])
                else:
                    continue
            if coincidencias == []:
                print("Lo siento, ningún país cumple con la búsqueda ingresada")
                return
            else:
                print(f"Los países que coinciden total o parcialmente con la búsqueda ingresada son:\n{coincidencias}")
                return

# Función filtrar por continente

def filtrar_continente():
    coincidencias = []
    while True:
        try:
            continente_ingresado = input("Ingrese un continente y filtraremos los países que están ubicados en él: ")
            with open("ListaPaises.csv", "r") as archivo:
                archivo.readline()
                for i in archivo:
                    linea_archivo = i.split(",")
                    continente_pais = str(linea_archivo[3])
                    if continente_ingresado.strip().lower() == continente_pais.strip().lower():
                        coincidencias.append(linea_archivo[0])
                    else:
                        continue

                if coincidencias == []:
                    print("Lo siento, ningún país está en el continente ingresado")
                    return
                else:
                    print(f"Los países que están ubicados en el continente ingresado son:\n{coincidencias}")
                    return
                    
        except ValueError:
            print("Ingrese un nombre de continente por favor")

# Filtrar por población

def filtrar_poblacion():
    coincidencias = []
    while True:
        try:
            while True:
                rango_minimo = int(input("Ingrese un rango mínimo de población para filtrar: "))
                if rango_minimo > 0:
                    break
                else:
                    print("Por favor, ingrese un número mayor a 0")
                    continue

            while True:
                rango_maximo = int(input("Ingrese un rango máximo de población para filtrar: "))
                if rango_maximo > 0 and rango_maximo > rango_minimo:
                    break
                else:
                    print("Por favor, ingrese un número mayor a 0 y mayor al rango mínimo ingresado anteriormente")
                    continue
            with open("ListaPaises.csv", "r") as archivo:
                archivo.readline()
                for i in archivo:
                    linea_archivo = i.split(",")
                    poblacion_pais = int(linea_archivo[1])
                    if poblacion_pais >= rango_minimo and poblacion_pais <= rango_maximo:
                        coincidencias.append(linea_archivo[0])
                    else:
                        continue

                if coincidencias == []:
                    print("Lo siento, ningún país coincide con el rango de población ingresado")
                    return
                else:
                    print(f"Los países que entran en el rango de población ingresado son:\n{coincidencias}")
                    return
                
        except ValueError:
            print("Ingrese un número entero por favor")

# Función filtrar por superficie

def filtrar_superficie():
    coincidencias = []
    while True:
        try:
            while True:
                rango_minimo = int(input("Ingrese un rango mínimo de superficie en km2 para filtrar: "))
                if rango_minimo > 0:
                    break
                else:
                    print("Por favor, ingrese un número mayor a 0")
                    continue

            while True:
                rango_maximo = int(input("Ingrese un rango máximo de superficie en km2 para filtrar: "))
                if rango_maximo > 0 and rango_maximo > rango_minimo:
                    break
                else:
                    print("Por favor, ingrese un número mayor a 0 y mayor al rango mínimo ingresado anteriormente")
                    continue
            with open("ListaPaises.csv", "r") as archivo:
                archivo.readline()
                for i in archivo:
                    linea_archivo = i.split(",")
                    superficie_pais = int(linea_archivo[2])
                    if superficie_pais >= rango_minimo and superficie_pais <= rango_maximo:
                        coincidencias.append(linea_archivo[0])
                    else:
                        continue

                if coincidencias == []:
                    print("Lo siento, ningún país entra en el rango de superficie ingresado")
                    return
                else:
                    print(f"Los países que entran en el rango de superficie ingresado son:\n{coincidencias}")
                    return
                
        except ValueError:
            print("Ingrese un número entero por favor")

# Función auxiliar para cargar los datos del CSV
def obtener_datos_paises():
    datos_paises = []
    try:
        with open("ListaPaises.csv", "r") as archivo:
            archivo.readline()  # Omitir el encabezado
            for linea in archivo:
                linea_archivo = linea.strip().split(",")
                # Aseguramos que los valores numéricos sean enteros
                datos_paises.append({
                    "nombre": linea_archivo[0],
                    "poblacion": int(linea_archivo[1]),
                    "superficie": int(linea_archivo[2]),
                    "continente": linea_archivo[3]
                })
        return datos_paises
    except FileNotFoundError:
        print("Error: No se encuentra el archivo ListaPaises.csv.")
        return []
    except IndexError:
        print("Error: El formato del archivo CSV es incorrecto.")
        return []
    except ValueError:
        print("Error: Los datos de población o superficie no son números enteros válidos.")
        return []

# Ordenar por nombre (A-Z)
def ordenar_orden_alfabetico():
    datos_paises = obtener_datos_paises()
    if not datos_paises:
        return
    
    paises_ordenados = sorted(datos_paises, key=lambda pais: pais['nombre'].lower())
    nombres_ordenados = [pais['nombre'] for pais in paises_ordenados]
    
    print(f"Países ordenados alfabéticamente (A-Z):\n{nombres_ordenados}")

def ordenar_orden_alfabetico_inverso():
    datos_paises = obtener_datos_paises()
    if not datos_paises:
        return
    
    paises_ordenados = sorted(datos_paises, key=lambda pais: pais['nombre'].lower(), reverse=True)
    nombres_ordenados = [pais['nombre'] for pais in paises_ordenados]
    
    print(f"Países ordenados alfabéticamente (Z-A):\n{nombres_ordenados}")

# Ordenar por población 
def ordenar_poblacion_mayor():
    datos_paises = obtener_datos_paises()
    if not datos_paises:
        return
    
    # Ordena por el valor de 'poblacion' (que es un entero), de mayor a menor
    paises_ordenados = sorted(datos_paises, key=lambda pais: pais['poblacion'], reverse=True)
    
    # Formateamos el resultado para mostrar el nombre y la población
    resultado = [f"{pais['nombre']} ({pais['poblacion']})" for pais in paises_ordenados]
    
    print(f"Países ordenados por población (Mayor a Menor):\n{resultado}")

def ordenar_poblacion_menor():
    datos_paises = obtener_datos_paises()
    if not datos_paises:
        return
    
    # Ordena por el valor de 'poblacion' (que es un entero), de menor a mayor (reverse=False por defecto)
    paises_ordenados = sorted(datos_paises, key=lambda pais: pais['poblacion'])
    
    # Formateamos el resultado para mostrar el nombre y la población
    resultado = [f"{pais['nombre']} ({pais['poblacion']})" for pais in paises_ordenados]
    
    print(f"Países ordenados por población (Menor a Mayor):\n{resultado}")

# Ordenar por superficie 
def ordenar_superficie_ascendente():
    datos_paises = obtener_datos_paises()
    if not datos_paises:
        return
    
    paises_ordenados = sorted(datos_paises, key=lambda pais: pais['superficie'])
    resultado = [f"{pais['nombre']} ({pais['superficie']} km2)" for pais in paises_ordenados]
    
    print(f"Países ordenados por superficie (Ascendente):\n{resultado}")

def ordenar_superficie_descendente():
    datos_paises = obtener_datos_paises()
    if not datos_paises:
        return
    
    paises_ordenados = sorted(datos_paises, key=lambda pais: pais['superficie'], reverse=True)
    
    resultado = [f"{pais['nombre']} ({pais['superficie']} km2)" for pais in paises_ordenados]
    
    print(f"Países ordenados por superficie (Descendente):\n{resultado}")

# Mostrar estadísticas de países

def estadisticas_paises(opcion_estadisticas):
    try:
        with open("ListaPaises.csv", "r") as archivo:
            archivo.readline()  # Omitir encabezado
            datos = []
            for linea in archivo:
                linea_archivo = linea.strip().split(",")
                datos.append({
                    "nombre": linea_archivo[0],
                    "poblacion": int(linea_archivo[1]),
                    "superficie": int(linea_archivo[2]),
                    "continente": linea_archivo[3]
                })

        if not datos:
            print("No hay datos cargados para mostrar estadísticas.")
            return

        # Opción a: país con mayor y menor población
        if opcion_estadisticas.lower() == "a":
            mayor_poblacion = max(datos, key=lambda p: p["poblacion"])
            menor_poblacion = min(datos, key=lambda p: p["poblacion"])
            print(f"País con mayor población: {mayor_poblacion['nombre']} ({mayor_poblacion['poblacion']})")
            print(f"País con menor población: {menor_poblacion['nombre']} ({menor_poblacion['poblacion']})")

        # Opción b: promedio de población
        elif opcion_estadisticas.lower() == "b":
            total_poblacion = sum(p["poblacion"] for p in datos)
            promedio_poblacion = total_poblacion / len(datos)
            print(f"Promedio de población de todos los países: {promedio_poblacion:.2f}")

        # Opción c: promedio de superficie
        elif opcion_estadisticas.lower() == "c":
            total_superficie = sum(p["superficie"] for p in datos)
            promedio_superficie = total_superficie / len(datos)
            print(f"Promedio de superficie de todos los países (km²): {promedio_superficie:.2f}")

        # Opción d: cantidad de países por continente
        elif opcion_estadisticas.lower() == "d":
            continente_ingresado = input("Ingrese el continente del que desea conocer la cantidad de países: ")
            contador = 0
            for pais in datos:
                if pais["continente"].strip().lower() == continente_ingresado.strip().lower():
                    contador += 1
            if contador == 0:
                print("No hay países registrados en el continente ingresado.")
            else:
                print(f"Cantidad de países en {continente_ingresado.capitalize()}: {contador}")

        elif opcion_estadisticas.lower() == "fin":
            return
        else:
            print("Opción inválida. Ingrese una de las opciones válidas: a, b, c o d.")

    except FileNotFoundError:
        print("Error: No se encuentra el archivo ListaPaises.csv.")
    except ValueError:
        print("Error: Los datos del archivo no son válidos.")
        
# Función filtrar países

def filtrar_paises(opcion_filtrar):
    if opcion_filtrar.lower() == "a":
        filtrar_continente()
        return
    if opcion_filtrar.lower() == "b":
        filtrar_poblacion()
        return
    if opcion_filtrar.lower() == "c":
        filtrar_superficie()
        return

# Ordenar países por nombre, población o superficie

def ordenar_paises(opcion_ordenar):
    if opcion_ordenar.lower() == "a":
        ordenar_orden_alfabetico()
        return
    elif opcion_ordenar.lower() == "b":
        ordenar_orden_alfabetico_inverso()
        return
    elif opcion_ordenar.lower() == "c":
        ordenar_poblacion_mayor()
        return
    elif opcion_ordenar.lower() == "d":
        ordenar_poblacion_menor()
        return
    elif opcion_ordenar.lower() == "e":
        ordenar_superficie_ascendente()
        return
    elif opcion_ordenar.lower() == "f":
        ordenar_superficie_descendente()
        return
    else:
        print("No se ha seleccionado ninguna opción válida. Por favor, seleccione una de las 6 opciones disponibles")
        return

# Menú

print("¡Hola! Bienvenido al sistema de gestión de países")
while True:
    try:
        opcion_menu = input("Puede elegir 4 opciones en el menú ingresando el comando correspondiente:\na- Buscar un país por nombre (Puede coincidir total o parcialmente)\nb- Filtrar países\nc- Ordenar países\nd- Mostrar estadísticas\nSi desea terminar de usar el sistema, ingrese 'FIN': ")
        if opcion_menu.lower() == "a":
            while True:
                pais_buscar = input("Ingrese un país y buscaremos los que coincidan completa o parcialmente. Si desea terminar de buscar, ingrese 'FIN': ")
                if pais_buscar.lower() == "fin":
                    break
                else:
                    buscar_pais(pais_buscar)
        elif opcion_menu.lower() == "b":
            while True:
                opcion_filtrar = input("Elija una opción para filtrar los países que cumplan con la descripción:\na- Para filtrar por continente\nb- Para filtrar por un rango de población\nc- Para filtrar por un rango de superficie\nSi desea terminar de filtrar, ingrese 'FIN': ")
                if opcion_filtrar.lower() == "fin":
                    break
                else:
                    filtrar_paises(opcion_filtrar)
        elif opcion_menu.lower() == "c":
            while True:
                opcion_ordenar = input("Ingrese con qué criterio desea ordenar los países:\na- Para ordenar por orden alfabético\nb- Para ordenar por orden alfabético inverso\nc- Para ordenar por población de mayor a menor\nd- Para ordenar por población de menor a mayor\ne- Para ordenar por superficie de manera ascendente\nf- Para ordenar por superficie de manera descendente\nSi desea terminar de ordenar, ingrese 'FIN': ")
                if opcion_ordenar.lower() == "fin":
                    break
                else:
                    ordenar_paises(opcion_ordenar)

        elif opcion_menu.lower() == "d":
            while True:
                opcion_estadisticas = input("Ingrese qué estadísticas desea ver:\na- Para mostrar el país con la mayor y la menor población\nb- Para mostrar el promedio de población de todos los países\nc- Para mostrar el promedio de la superficie de todos los países en km2\nd- Para mostrar la cantidad de países de un continente que seleccionará a continuación\nSi desea terminar de examinar, ingrese 'FIN': ")
                if opcion_estadisticas.lower() == "fin":
                    break
                else:
                    estadisticas_paises(opcion_estadisticas)
        elif opcion_menu.lower() == "fin":
            print("Gracias por utilizar el sistema de búsqueda de países")
            break

    except ValueError:
        print("Por favor, ingresa un comando válido")
        
