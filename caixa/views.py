from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import datetime
from .models import movimentos
from .forms import MovimentoForm


def dashboard(request):
    if request.method == 'GET':
        form = MovimentoForm()
        ano_atual = datetime.now().year
        mes_atual = datetime.now().month

        selected_ano = int(request.GET.get('ano', ano_atual))  # Converta para inteiro
        selected_mes = int(request.GET.get('mes', mes_atual))  # Converta para inteiro

        movimentos_list = movimentos.objects.filter(data__year=selected_ano, data__month=selected_mes)

        entradas_do_mes = movimentos.objects.filter(data__year=selected_ano, data__month=selected_mes, in_out=True).aggregate(Sum('valor'))['valor__sum'] or 0
        saidas_do_mes = movimentos.objects.filter(data__year=selected_ano, data__month=selected_mes, in_out=False).aggregate(Sum('valor'))['valor__sum'] or 0
        total_do_mes = entradas_do_mes - saidas_do_mes
        

        return render(request, 'dashboard.html', {
                                                'movimentos_list': movimentos_list, 
                                                'entradas_do_mes': entradas_do_mes, 
                                                'saidas_do_mes': saidas_do_mes, 
                                                'total_do_mes': total_do_mes,
                                                'ano_atual': selected_ano,  # Use o ano selecionado
                                                'mes_atual': selected_mes, 
                                                'form': form,
                                                'meses': [(i, datetime(2022, i, 1).strftime('%B')) for i in range(1, 13)],
                                                'anos': range(ano_atual, ano_atual - 5, -1), 
                                                })

    else:
        form = MovimentoForm(request.POST)
        print(movimentos)
        if form.is_valid():
            form.save()
            return redirect('dashboard') 
        else:
            return render(request, 'dashboard.html', {'form': form})
