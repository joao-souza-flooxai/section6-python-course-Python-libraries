from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
PASTA_ORIGINAIS = PASTA_NOVA / 'pdfs_originais'

IA =PASTA_ORIGINAIS / 'short_paper_machine_learning.pdf'

PASTA_NOVA.mkdir(exist_ok=True)
PASTA_ORIGINAIS.mkdir(exist_ok=True)


reader =PdfReader(IA)

# print(len(reader.pages))
# for page in reader.pages :

page0 = reader. pages[0]

print(page0.extract_text())

writer = PdfWriter()

with open(PASTA_NOVA /'NOVO_PDF.pdf', 'wb') as arquivo:
    for page in reader. pages :
        writer.add_page(page0)
        writer.write(arquivo)


for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo) 


files = [
    PASTA_NOVA / 'page0.pdf',
    PASTA_NOVA / 'page1.pdf' ,
]

merger = PdfMerger()
for file in files:
    merger.append(file) 

merger.write(PASTA_NOVA /'MERGED.pdf') #type: ignore
merger.close()