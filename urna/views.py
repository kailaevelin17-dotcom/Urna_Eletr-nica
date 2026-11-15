from django.shortcuts import render, redirect
from .models import Candidato, Votacao


def urna(request):

    candidatos = Candidato.objects.all().order_by('numero')

    if request.method == 'POST':

        # VOTO EM BRANCO
        if request.POST.get('branco'):

            votacao, created = Votacao.objects.get_or_create(id=1)

            votacao.votos_brancos += 1
            votacao.save()

            return redirect('resultado')

        # VOTO EM CANDIDATO
        numero = request.POST.get('numero')

        if numero:

            try:
                candidato = Candidato.objects.get(numero=int(numero))

                candidato.votos += 1
                candidato.save()

                return redirect('resultado')

            except (Candidato.DoesNotExist, ValueError):
                pass

    return render(
        request,
        'urna/urna.html',
        {'candidatos': candidatos}
    )


def resultado(request):

    candidatos = Candidato.objects.all().order_by('-votos')

    votacao, created = Votacao.objects.get_or_create(id=1)

    votos_candidatos = sum(
        candidato.votos
        for candidato in candidatos
    )

    total_votos = votos_candidatos + votacao.votos_brancos

    return render(
        request,
        'urna/resultado.html',
        {
            'candidatos': candidatos,
            'total_votos': total_votos,
            'votos_brancos': votacao.votos_brancos
        }
    )