# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
#- Crie a data do empréstimo
#- Crie a data do final do empréstimo
#- Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y'
data_inicio = datetime.strptime('20/12/2020', fmt)
data_final = datetime.strptime('20/12/2025', fmt)
valor_parcelas_mensal = ((1 * (10**6)) / 5)/12
delta = relativedelta(data_final, data_inicio)
meses_totais = delta.years * 12 + delta.months + 1
data_parcela = data_inicio
for i in range(meses_totais):
    print(f"Parcela {i+1:02d} - Vencimento: {data_parcela.strftime('%d/%m/%Y')} - Valor: R$ {valor_parcelas_mensal:,.2f}")
    data_parcela += relativedelta(months=1)