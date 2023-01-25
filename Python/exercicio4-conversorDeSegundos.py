segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = segundos//86400
diasInt = int(dias) 
horas = ((segundos/86400)-diasInt)*24
horasInt = int(horas)
minutos = (((segundos/86400-diasInt)*24)-horasInt)*60
minutosInt = int(minutos)
segundos = (((((segundos/86400-diasInt)*24)-horasInt)*60)-minutosInt)*60



print(diasInt, 'dias,', horasInt, 'horas,', minutosInt, 'minutos e', int(segundos), 'segundos.')