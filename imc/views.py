from django.shortcuts import render

# Create your views here.


def pagina_imc(request):

    if request.method == 'POST':
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')

        # Converte o dados recebido para o tipo numérico, par apoder fazer o cáculo
        peso = float(peso)
        altura = float(altura)

        imc = peso / (altura * altura)

        estado_imc = ''

        cor_estado_imc = 'black'

        if imc < 18.5:
            estado_imc = 'Abaixo do peso'
            cor_estado_imc = 'yellow'

        elif imc <= 18.5 and imc <= 24.9:
            estado_imc = 'peso nomal'
            cor_estado_imc = 'green'

        elif imc >= 25 and imc <= 29.9:
            estado_imc = 'Sobrepeso'
            cor_estado_imc = 'red'   

        elif imc >= 30 and imc <= 34.9:
            estado_imc = 'Obesidade I'
            cor_estado_imc = 'red'

        elif imc >= 35 and imc <= 39.9:
            estado_imc = 'Obesidade II'
            cor_estado_imc = 'red'

        else:
            estado_imc = 'Obesidade III'
            cor_estado_imc = 'red'

      

        contexto = {
            'imc': imc,
            'estado_imc': estado_imc,
            'cor_estado_imc': cor_estado_imc
        }

        return render(request, 'imc.html', contexto)

    return render(request, 'imc.html')
