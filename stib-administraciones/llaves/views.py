from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TipoLlavesForm
from .models import Llaves
from ..edificios.models import Edificios
from ..core.views import permisos_a_edificios


@login_required(redirect_field_name='accounts/login/')
@permisos_a_edificios
def set_llaves(request, edificio):
    """
    Vista para asignar llaves a los edificios
    """
    # -- obtengo las laves del edificio
    llaves_edificios = Llaves.objects.filter(edificio=edificio).all()

    ctx = {
        'form': TipoLlavesForm(prefix='llaves', initial={str(llave.tipo_llave_id):1 for llave in llaves_edificios}),
        'edificio': Edificios.objects.get(pk=edificio)
    }

    if request.method == "POST":
        # -- obtengo en una lista todos los tipos de llaves selccionados
        tipo_llaves = request.POST.getlist("llaves-tipo_llaves")
        # -- limpio las llaves del edifico
        Llaves.objects.filter(edificio=edificio).delete()
        # -- asigno una x una las llaves seleccionadas
        for tipo in tipo_llaves:
            llaves = Llaves()
            llaves.tipo_llave_id = tipo
            llaves.edificio_id = edificio
            llaves.save()

        messages.success(request, 'Se han asignado las llaves correctamente.')
        return redirect('edificios:administraciones', edificio)

    return render(request, 'llaves/llaves_form.html', ctx)
