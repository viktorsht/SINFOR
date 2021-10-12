from datetime import datetime as dt

def calcula_idade(nasc):

    agora = dt.today()
    data = dt.strptime(nasc, '%d/%m/%Y')
    if agora.month <= data.month and agora.day <= data.day:
        return (agora.year - data.year) -1
    else:
        return (agora.year - data.year)

def conta_dias(data):
    today = dt.today()
    data = dt.strptime(data,'%d/%m/%Y')
    data = data.strftime('%d/%m/%Y')
    end = dt.strptime(data,'%d/%m/%Y')
    diff = abs((end - today).days)
    return diff


