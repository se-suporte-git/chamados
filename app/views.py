from django.shortcuts import render
from .models import Anotacao
from .models import ChamadoAtendido
from django.http import HttpResponse

import csv

def minha_view(request):
    if request.method == 'POST':
        data_solicitacao = request.POST['data_solicitacao']
        numero_chamado = request.POST['numero_chamado']
        problema_relatado = request.POST['problema_relatado']
        resolucao = request.POST['resolucao']
        data_solucao = request.POST['data_solucao']
        tipo_atendimento = request.POST['tipo_atendimento']
        hora_inicio = request.POST['hora_inicio']
        hora_fim = request.POST['hora_fim']

        # Salvar os dados no banco de dados usando o modelo Anotacao
        anotacao = Anotacao(
            data_solicitacao=data_solicitacao,
            numero_chamado=numero_chamado,
            problema_relatado=problema_relatado,
            resolucao=resolucao,
            data_solucao=data_solucao,
            tipo_atendimento=tipo_atendimento,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim
        )
        print(anotacao)
        anotacao.save()

        chamado_atendido = ChamadoAtendido(
            numero_chamado=numero_chamado,
            problema_relatado=problema_relatado,
            resolucao=resolucao,
            data_solucao=data_solucao,
            tipo_atendimento=tipo_atendimento,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim
        )
        chamado_atendido.save()

        # Redirecionar para a página de sucesso
        return render(request, 'app/sucesso.html')

    return render(request, 'app/formulario_anotacao.html')

def chamados_atendidos(request):
    chamados = ChamadoAtendido.objects.all()
    print(chamados)
    return render(request, 'app/chamados_atendidos.html', {'chamados': chamados})



def exportar_chamados_csv(request):
    chamados = ChamadoAtendido.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="chamados_atendidos.csv"'

    writer = csv.writer(response)

    writer.writerow(['Número do Chamado', 'Problema Relatado', 'Resolução', 'Data da Solução', 'Tipo de Atendimento', 'Hora de Início', 'Hora de Fim'])

    for chamado in chamados:
        writer.writerow([chamado.numero_chamado, chamado.problema_relatado, chamado.resolucao, chamado.data_solucao, chamado.tipo_atendimento, chamado.hora_inicio, chamado.hora_fim])

    return response
