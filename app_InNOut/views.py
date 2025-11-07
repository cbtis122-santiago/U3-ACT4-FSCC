from django.shortcuts import render, redirect, get_object_or_404
from .models import Sucursal

# Página de inicio del sistema
def inicio_in_n_out(request):
    total_sucursales = Sucursal.objects.count()
    sucursales = Sucursal.objects.all().order_by('-fecha_apertura')[:5]
    return render(request, 'inicio.html', {'total_sucursales': total_sucursales, 'sucursales': sucursales})

# Mostrar formulario para agregar sucursal
def agregar_sucursal(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_tienda')
        direccion = request.POST.get('direccion')
        ciudad = request.POST.get('ciudad')
        codigo_postal = request.POST.get('codigo_postal')
        telefono = request.POST.get('telefono_tienda')
        fecha = request.POST.get('fecha_apertura')
        es_drive_thru = True if request.POST.get('es_drive_thru') == 'on' else False

        Sucursal.objects.create(
            nombre_tienda=nombre,
            direccion=direccion,
            ciudad=ciudad,
            codigo_postal=codigo_postal,
            telefono_tienda=telefono,
            fecha_apertura=fecha,
            es_drive_thru=es_drive_thru
        )
        return redirect('ver_sucursales')

    return render(request, 'sucursal/agregar_sucursal.html')

# Ver todas las sucursales
def ver_sucursales(request):
    sucursales = Sucursal.objects.all().order_by('nombre_tienda')
    return render(request, 'sucursal/ver_sucursales.html', {'sucursales': sucursales})

# Mostrar formulario con datos para actualizar
def actualizar_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, id=sucursal_id)
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal})

# Procesar la actualización (POST)
def realizar_actualizacion_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, id=sucursal_id)
    if request.method == 'POST':
        sucursal.nombre_tienda = request.POST.get('nombre_tienda')
        sucursal.direccion = request.POST.get('direccion')
        sucursal.ciudad = request.POST.get('ciudad')
        sucursal.codigo_postal = request.POST.get('codigo_postal')
        sucursal.telefono_tienda = request.POST.get('telefono_tienda')
        sucursal.fecha_apertura = request.POST.get('fecha_apertura')
        sucursal.es_drive_thru = True if request.POST.get('es_drive_thru') == 'on' else False
        sucursal.save()
        return redirect('ver_sucursales')
    return redirect('ver_sucursales')

# Confirmación y borrado
def borrar_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, id=sucursal_id)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('ver_sucursales')
    return render(request, 'sucursal/borrar_sucursal.html', {'sucursal': sucursal})

# ===============================
# CRUD TRABAJADOR
# ===============================
from .models import Trabajador, Sucursal

def agregar_trabajador(request):
    sucursales = Sucursal.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        puesto = request.POST.get('puesto')
        fecha_contratacion = request.POST.get('fecha_contratacion')
        email = request.POST.get('email')
        telefono_personal = request.POST.get('telefono_personal')
        sucursal_id = request.POST.get('sucursal')
        sucursal = Sucursal.objects.get(id=sucursal_id)
        Trabajador.objects.create(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            fecha_contratacion=fecha_contratacion,
            email=email,
            telefono_personal=telefono_personal,
            sucursal=sucursal
        )
        return redirect('ver_trabajadores')
    return render(request, 'trabajador/agregar_trabajador.html', {'sucursales': sucursales})

def ver_trabajadores(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'trabajador/ver_trabajadores.html', {'trabajadores': trabajadores})

def actualizar_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    sucursales = Sucursal.objects.all()
    return render(request, 'trabajador/actualizar_trabajador.html', {'trabajador': trabajador, 'sucursales': sucursales})

def realizar_actualizacion_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    if request.method == 'POST':
        trabajador.nombre = request.POST.get('nombre')
        trabajador.apellido = request.POST.get('apellido')
        trabajador.puesto = request.POST.get('puesto')
        trabajador.fecha_contratacion = request.POST.get('fecha_contratacion')
        trabajador.email = request.POST.get('email')
        trabajador.telefono_personal = request.POST.get('telefono_personal')
        sucursal_id = request.POST.get('sucursal')
        trabajador.sucursal = Sucursal.objects.get(id=sucursal_id)
        trabajador.save()
        return redirect('ver_trabajadores')
    return redirect('ver_trabajadores')

def borrar_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('ver_trabajadores')
    return render(request, 'trabajador/borrar_trabajador.html', {'trabajador': trabajador})
