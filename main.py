"""
SkyRoute - Sistema de Gestión de Pasajes Aéreos
Versión prototipo (Evidencia 2 - TSCDeIA 2025)
Autores: [Juan Martin Rosello dal molin
         Erica Melisa Paredes 
         Pablo Francisco Elías 
         Florencia Belén Dussman 
         Lisi Daniela Gonzalez]
"""
from datetime import datetime
clientes = []
destinos = []
ventas = []
id_cliente = 1
id_destino = 1
id_venta = 1

def mostrar_menu():
    print("\nBienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Botón de Arrepentimiento")
    print("6. Ver Reporte General")
    print("7. Acerca del Sistema")
    print("8. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            print("\n-- GESTIONAR CLIENTES --")
            print("1. Ver Clientes")
            print("2. Agregar Cliente")
            print("3. Modificar Cliente")
            print("4. Eliminar Cliente")
            print("5. Volver al Menú Principal")
            subop = input("Seleccione una opción: ")

            if subop == "1":
                for c in clientes:
                    print(c)
            elif subop == "2":
                razon = input("Razón social: ")
                cuit = input("CUIT: ")
                correo = input("Correo: ")
                clientes.append({"id": id_cliente, "razon": razon, "cuit": cuit, "correo": correo})
                print(f"Cliente agregado con ID {id_cliente}")
                id_cliente += 1
            elif subop == "3":
                cid = int(input("ID del cliente a modificar: "))
                for c in clientes:
                    if c["id"] == cid:
                        c["razon"] = input("Nueva razón social: ")
                        c["cuit"] = input("Nuevo CUIT: ")
                        c["correo"] = input("Nuevo correo: ")
                        print("Cliente modificado.")
            elif subop == "4":
                cid = int(input("ID del cliente a eliminar: "))
                clientes = [c for c in clientes if c["id"] != cid]
                print("Cliente eliminado.")
            elif subop == "5":
                break

    elif opcion == "2":
        while True:
            print("\n-- GESTIONAR DESTINOS --")
            print("1. Ver Destinos")
            print("2. Agregar Destino")
            print("3. Modificar Destino")
            print("4. Eliminar Destino")
            print("5. Volver al Menú Principal")
            subop = input("Seleccione una opción: ")

            if subop == "1":
                for d in destinos:
                    print(d)
            elif subop == "2":
                ciudad = input("Ciudad: ")
                pais = input("País: ")
                costo = float(input("Costo base: "))
                destinos.append({"id": id_destino, "ciudad": ciudad, "pais": pais, "costo": costo})
                print(f"Destino agregado con ID {id_destino}")
                id_destino += 1
            elif subop == "3":
                did = int(input("ID del destino a modificar: "))
                for d in destinos:
                    if d["id"] == did:
                        d["ciudad"] = input("Nueva ciudad: ")
                        d["pais"] = input("Nuevo país: ")
                        d["costo"] = float(input("Nuevo costo: "))
                        print("Destino modificado.")
            elif subop == "4":
                did = int(input("ID del destino a eliminar: "))
                destinos = [d for d in destinos if d["id"] != did]
                print("Destino eliminado.")
            elif subop == "5":
                break

    elif opcion == "3":
        print("\n-- REGISTRAR VENTA --")
        cid = int(input("ID del cliente: "))
        did = int(input("ID del destino: "))
        fecha = datetime.now().strftime("%Y-%m-%d")
        estado = "Activa"
        ventas.append({"id": id_venta, "cliente": cid, "destino": did, "fecha": fecha, "estado": estado})
        print(f"Venta registrada con ID {id_venta}")
        id_venta += 1

    elif opcion == "4":
        print("\n-- CONSULTAR VENTAS --")
        print("1. Todas las ventas")
        print("2. Ventas por cliente")
        print("3. Ventas por destino")
        print("4. Ventas por estado")
        print("5. Ventas anuladas")
        subop = input("Seleccione una opción: ")
        if subop == "1":
            for v in ventas:
                print(v)
        elif subop == "2":
            cid = int(input("ID cliente: "))
            for v in ventas:
                if v["cliente"] == cid:
                    print(v)
        elif subop == "3":
            did = int(input("ID destino: "))
            for v in ventas:
                if v["destino"] == did:
                    print(v)
        elif subop == "4":
            estado = input("Estado (Activa/Anulada): ")
            for v in ventas:
                if v["estado"] == estado:
                    print(v)
        elif subop == "5":
            for v in ventas:
                if v["estado"] == "Anulada":
                    print(v)

    elif opcion == "5":
        print("\n-- BOTÓN DE ARREPENTIMIENTO --")
        vid = int(input("ID de la venta a anular: "))
        for v in ventas:
            if v["id"] == vid:
                fecha_venta = datetime.strptime(v["fecha"], "%Y-%m-%d")
                dias_habiles = (datetime.now() - fecha_venta).days
                if dias_habiles <= 60:
                    v["estado"] = "Anulada"
                    print("Venta anulada exitosamente.")
                else:
                    print("El plazo de 60 días hábiles ha expirado.")
                break

    elif opcion == "6":
        print("\n-- REPORTE GENERAL --")
        print(f"Clientes: {len(clientes)}, Destinos: {len(destinos)}, Ventas: {len(ventas)}")

    elif opcion == "7":
        print("Sistema de Gestión de Pasajes - SkyRoute S.R.L. - Prototipo académico.")

    elif opcion == "8":
        print("Saliendo del sistema. Gracias por usar SkyRoute.")
        break
    else:
        print("Opción inválida.")
