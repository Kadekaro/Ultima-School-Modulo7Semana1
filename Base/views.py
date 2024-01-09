from django.shortcuts import render
from Base.forms import contatoForms, reservaForms


# Create your views here.
def inicio(request):
    return render(request, "inicio.html")


def contato(request):
    sucesso = False
    form = contatoForms(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'telefone': '(99)9999-9999',
        'responsável': 'Maria da Silva Pereira',
        'form': form,
        'sucesso': sucesso,
    }

    return render(request, "contato.html", contexto)


def reserva(request):
    sucesso = False
    form = reservaForms(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    cont = {'form': form,
            'sucesso': sucesso}

    return render(request, "reserva.html", cont)
