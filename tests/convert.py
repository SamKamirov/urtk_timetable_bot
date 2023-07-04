import tabula
import pandas as pd
pdf_in = '1.pdf'
PDF = tabula.read_pdf(pdf_in, pages='all', multiple_tables=True)
PDF = pd.DataFrame(PDF)
PDF.to_excel('from_pdf.xls', index=False)
print('Done')
