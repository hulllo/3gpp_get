import pandas as pd
url ='http://www.3gpp.org/specifications/specification-numbering'
data =pd.read_html(url)[0]
print(data)
