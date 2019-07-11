class Cliente:
    def __init__ (self, nombre, correo, dinero):
        self.nombre = nombre
        self.correo = correo
        self.dinero = dinero
    
    def printCliente(self):
        print("DATOS CLIENTE: ")
        print(f'Nombre: {self.nombre}')
        print(f'Correo: {self.correo}')
        print(f'Dinero: {self.dinero}')


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def printProducto(self):
        print(f'Nombre Producto: {self.nombre}')
        print(f'Precio Producto: {self.precio}')

class Tienda:
    def __init__(self, prod1, prod2, prod3):
         self.prod1 = prod1
         self.prod2 = prod2
         self.prod3 = prod3
         self.productos = [prod1,prod2,prod3]
    
    def printTienda(self):
         for producto in self.productos:
             producto.printProducto()

    def compra(self, comprador, opcion):
        opt = int(opcion)
        if opt == 1:
            if comprador.dinero >= prod1.precio:
                print(f'Gracias por la compra de {self.prod1.nombre}')
            else :
                print(f'No te alcanza para comprar {self.prod1.nombre}')

        # elif opcion == 2:
        #     if comprador.dinero >= prod2.precio:
        #         print(f'Gracias por la compra de {prod1.nombre}')
        #     else 
        #         print(f'No te alcanza para comprar {prod1.nombre}')
                

#Productos
prod1 = Producto('Papitas', 15)
prod2 = Producto('Refresco', 12)
prod3 = Producto('Gomitas', 10)

#Cliente
cliente1 = Cliente("Daniel Garnica ", "thedaniel115@gmail.com", 20)
cliente1.printCliente()

#Tiendita
tiendita = Tienda(prod1, prod2, prod3)

print('PRODUCTOS DEL SENIOR DE LA TIENDA')

for producto in tiendita.productos:
    print('------------------------')
    producto.printProducto()

opcion = input("Ingresa el nombre del producto: ")

tiendita.compra(cliente1,opcion)

