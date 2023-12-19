from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from easteregg.includes.GeneradorBaseDeDatos import crearBaseDeDatos
from easteregg.includes.AñadirValores import stock
from easteregg.includes.BorrarTablas import drop
from easteregg.includes.AñadirValores import insertarDetallePedido, insertarPedido

# Create your views here.
def index(request):
    return render(request, 'index2.html')

def procesarFormulario(request):
    if request.method == "POST":
        connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
        )
        connection.autocommit = False

        try:
            codCliente = request.POST.get("codCliente", "")
            fechaPed = request.POST.get("fechaPed", "")
            codProd = request.POST.get("codProd", "")
            codPed = request.POST.get("codPed", "")
            cantidad = request.POST.get("cantidad", "")
            contexto = {
                "miTexto" : "Se ha añadido el pedido:",
                "fechaPed" : f"\tfecha pedido: {fechaPed}",
                "codCliente" : f"\tCódigo cliente: {codCliente}",
                "codProd" : f"\tCódigo producto: {codProd}",
                "codPed" : f"\tCódigo pedido: {codPed}",
                "cantidad" : f"\tCantidad: {cantidad}",
            }
            cursor = connection.cursor()
            insertarPedido(cursor, codPed, codCliente, fechaPed)
            insertarDetallePedido(cursor, codPed, codProd, cantidad)
            connection.commit()
        except:
            contexto = {
                "miTexto" : "La inserción ha fallado",
                "fechaPed" : "",
                "codCliente" : "",
                "codProd" : "",
                "codPed" : "",
                "cantidad" : "",
            }
        cursor.close()
        connection.close()
        return render(request, 'index2.html', contexto)

def generarBaseDeDatos(request):

    connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
    )
    connection.autocommit = False

    drop(connection)

    crearBaseDeDatos(connection)

    stock(connection)

    connection.close()

    contexto = {
        "miTexto" : "Base de datos actualizada",
    }

    return render(request, 'index2.html', contexto)
