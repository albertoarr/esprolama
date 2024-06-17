from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from .forms import VolcadoForm
from .models import Estrategia, Principio, Descriptor, Volcado, Autoevaluacion


def autoevaluaciones(request):
    objetos_autoevaluacion = Autoevaluacion.objects.all()
    context = {
        'objetos_autoevaluacion': objetos_autoevaluacion
    }
    return render(request, 'elama/autoevaluaciones.html', context)


def estrategias(request, autoevaluacion_id):
    objetos_estrategia = Estrategia.objects.filter(autoevaluacion=autoevaluacion_id)
    context = {
        'objetos_estrategia': objetos_estrategia
    }
    return render(request, 'elama/estrategias.html', context)


def principios(request, estrategia_id):
    objetos_principio = Principio.objects.filter(estrategia=estrategia_id)
    context = {
        'objetos_principio': objetos_principio,
    }
    return render(request, 'elama/principios.html', context)


def descriptores(request, principio_id):
    objetos_descriptor = Descriptor.objects.filter(principio=principio_id)
    context = {
        'objetos_descriptor': objetos_descriptor,
    }
    return render(request, 'elama/descriptores.html', context)


def volcado(request, autoevaluacion_id, descriptor_id):
    autoevaluacion = Autoevaluacion.objects.get(pk=autoevaluacion_id)
    descriptor = Descriptor.objects.get(pk=descriptor_id)
    existe = True

    try:
        volcado = Volcado.objects.get(autoevaluacion=autoevaluacion, descriptor=descriptor)
    except ObjectDoesNotExist:
        existe = False

    if request.method != 'POST':

        if existe:
            form = VolcadoForm(instance=volcado)
        else:
            form = VolcadoForm()

    else:
        if existe:
            form = VolcadoForm(request.POST, instance=volcado)
            if form.is_valid():
                volcado.save()
        else:
            form = VolcadoForm(data=request.POST)
            if form.is_valid():
                v = form.save(commit=False)
                v.autoevaluacion = autoevaluacion
                v.descriptor = descriptor
                v.save()
        #return redirect('elama: individual', autoevaluacion_id=autoevaluacion.id)

    context = {
        'autoevaluacion': autoevaluacion,
        'descriptor': descriptor,
        'form': form
    }

    return render(request, 'elama/volcado.html', context)
