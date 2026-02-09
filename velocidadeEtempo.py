velocidadekm = float(input('Digite a velocidade média em km/h que você viajou: '))

velocidadem = velocidadekm / 3.6

tempoDecimal = 435 / velocidadekm

horas = int(tempoDecimal)
minutos = int((tempoDecimal - horas) * 60)

print(f'A viagem em {velocidadekm}km/h irá demorar {horas}H/{minutos}M\n{velocidadekm}km/h = {velocidadem}m/s')