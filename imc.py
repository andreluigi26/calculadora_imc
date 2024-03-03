import PySimpleGUI as sg

def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        return imc
    except ZeroDivisionError:
        return None
    except Exception as e:
        raise e
    
def classificar_imc(imc):
    if imc is None:
        return "Erro"
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
layout = [
    [sg.Text("Peso (kg):"), (sg.InputText(key="peso"))],
    [sg.Text("Altura (m):"), (sg.InputText(key="altura"))],
    [sg.Button("Calcular")],
    [sg.Text(size=(30,1), key="resultado")],
    [sg.Text(size=(30,1), key="classificacao")]
]

window = sg.Window("Calculadora de IMC", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Calcular":
        try:
            peso = float (values["peso"])
            altura = float (values["altura"])

            imc = calcular_imc(peso,altura)
            window["resultado"].update(f"Seu IMC é: {imc:.2f}")
            window["classificacao"].update(f"Classificação: {classificar_imc(imc)}")
        except ValueError:
            window["resultado"].update("Erro: Insira números válidos para peso e altura.")



window.close()