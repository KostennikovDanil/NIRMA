from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

PTV = 0
RES_1 = 0
RES_2 = True
RES_3 = True


def get_main(request, status):
    global PTV, RES_1, RES_2, RES_3
    if request.method == 'POST':
        if status == 1:
            form = FirstState(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                result = cd.get('yes_or_no')
                if result == False:
                    PTV = cd.get('ptv')
                    response = redirect('/main/2')
                    return response
                else:
                    return render(request, 'exit.html', context={
                        'message': "У пациента противопоказания, заканчиваем исследование"})

        if status == 2:
            form = SecondState(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                RES_1 = cd.get('res')
                response = redirect('/main/3')
                return response

        if status == 3:
            form = ThirdState(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                RES_2 = cd.get('yes_or_no')
                if RES_2 == False or RES_1 == 0:
                    return render(request, 'exit.html', context={
                        'message': "Диспансерское лечение"})

                else:
                    response = redirect('/main/4')
                    return response

        if status == 4:
            form = FourthState(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                RES_3 = cd.get('yes_or_no')
                if PTV > 15 and RES_3 == False:
                    return render(request, 'exit.html', context={
                        'message': "Персональное лечение"})
                elif PTV > 15 and RES_1 == 2:
                    return render(request, 'exit.html', context={
                        'message': "Лечение ИБС"})
                elif RES_3 == True:
                    return render(request, 'exit.html', context={
                        'message': "Использовать визуализирующие методы. Далее лечение ИБС"})
                else:
                    return render(request, 'exit.html', context={
                        'message': "При наличаие ишемических измененией лечение ИБС. В противном случае диспансерное наблюдение"})

    if status == 1:
        statusText = "Проведено холтеровское мониторирование, ЭКГ, сбор анамнеза, физикальное обследование"
        fdata_value = "Нет"
        form = FirstState(request.POST)
        instruction = "Нажмите если есть"

        return render(request, 'main.html', context={
            'status': statusText, "fdata_value": fdata_value, 'form': form, 'instruction': instruction})

    if status == 2:
        statusText = "ТТ первый день"
        form = SecondState(request.POST)
        instruction = "0 - ЖА исчезались или сохранялись с тенденцией к уменьшению\n 1 - ЖА появлялись или прогрессировали\n 2 - ЖА возникли на фоне депрессии сегмента ST ишемического характера"
        return render(request, 'main.html', context={
            'instruction': instruction, 'status': statusText, 'form': form})

    if status == 3:
        statusText = "ТТ второй день проверка на воспроизводимость"
        form = ThirdState(request.POST)
        instruction = "Нажмите если результаты воспроизводимы"

        return render(request, 'main.html', context={
            'status': statusText, 'form': form, 'instruction': instruction})

    if status == 4:
        statusText = "ТТ на фоне Hg"
        form = FourthState(request.POST)
        instruction = "Проба считается положительной, если на фоне принятогосублингвально Ng значимо (в  ≥2 раз)"

        return render(request, 'main.html', context={
            'status': statusText, 'form': form, 'instruction': instruction})
