# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime. Strptime('DATA' , 'FORMATO' )
# datetime.now()

from datetime import datetime
from pytz import timezone


data=datetime(2022, 4, 20, 7, 49, 23)
print(data)


data_str_data = '20-04-2022 07:49:23'
data_str_fmt ='%d-%m-%Y %H:%M:%S'

data2 = datetime.strptime(data_str_data, data_str_fmt)
print(data2)
print(datetime.now(timezone('Asia/Tokyo')))
print(data.timestamp())
print(datetime.fromtimestamp(datetime.now().timestamp()))