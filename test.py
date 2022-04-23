from datetime import datetime
import datetime

lsp = datetime.now()

lsp = str(lsp)

date = lsp.split()[0]
dates = date.split('-')
print(type(dates))

k = datetime.strptime('24052010', "%d%m%Y").date()
print(k)
print(type(k))