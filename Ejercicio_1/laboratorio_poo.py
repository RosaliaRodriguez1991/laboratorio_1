'''
Desafío 1: Sistema de Gestión de Productos
Objetivo: Desarrollar un sistema para manejar productos en un inventario.

Requisitos:

Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
Implementar operaciones CRUD para gestionar productos del inventario.
Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
Persistir los datos en archivo JSON.
'''

import json

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.__codigo = self.validar_codigo(codigo)
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad
 
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre.capitalize()
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def precio(self):
        return self.__cantidad

    def validar_codigo(self,codigo):
        try:
            codigo_num = float(codigo)
            if codigo_num <= 0:
                raise ValueError("El código debe ser numérico positivo.")
            return codigo_num
        except ValueError:
            raise ValueError("El código debe ser un número válido.")

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }



    def __str__(self):
        return f"Código:{self.codigo}, Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class ProductoElectronico(Producto):
    def __init__(self, codigo, nombre, precio, cantidad, garantia):
        super().__init__(codigo, nombre, precio, cantidad)
        self.garantia = garantia

    @property
    def garantia(self):
        return self.__garantia
    
    def to_dict(self):
        data = super().to_dict()
        data["garantia"] = self.garantia
        return data

    def __str__(self):
        return f"Código: {self.codigo}, Producto Electrónico: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Garantía: {self.garantia} años"


class ProductoAlimenticio(Producto):
    def __init__(self, codigo, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(codigo, nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

   
    
    @property
    def fecha_expiracion(self):
        return self.__fecha_expiracion
    
    def to_dict(self):
        data = super().to_dict()
        data["fecha_expiracion"] = self.fecha_expiracion
        return data
    
    def __str__(self):
        return f" Código: {self.codigo}, Producto Alimenticio: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Fecha de Expiración: {self.fecha_expiracion}"
    

class Inventario:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return datos    

    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')   

    def agregar_producto(self, producto):
        try:
            datos = self.agregar_producto()
            codigo = producto.codigo
            if not str(codigo) in datos.keys():
                datos[codigo] = producto.to_dict()
                self.guardar_datos(datos)
                print(f'Producto{producto.codigo} {producto.nombre} agregado correctamente')
            else:
                print(f"Ya existe producto con ese Código '{codigo}'.")
        except Exception as error:
            print(f'Error inesperadoal crear producto: {error}')

    def actualizar_producto(self, codigo, nombre, nuevo_producto):
        try:
            datos = self.leer_datos()
            if str(codigo) in datos.keys():
                datos[codigo]['nuevo_producto'] = nuevo_producto
                self.guardar_datos(datos)
                print(f'Producto actualizado Código:{codigo}')
            else:
                print(f'No se encontró producto con ese código:{codigo}')
        except Exception as e:
            print(f'Error al actualizar el producto: {e}')

    def eliminar_producto(self, nombre):
        self.productos = [p for p in self.productos if p.nombre != nombre]
        self.guardar_datos()

    def actualizar_producto(self, nombre, nuevo_producto):
        for idx, producto in enumerate(self.productos):
            if producto.nombre == nombre:
                self.productos[idx] = nuevo_producto
                self.guardar_datos()
                return
        print("Producto no encontrado.")

    