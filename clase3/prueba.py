import pandas as pd
data=pd.read_excel('./RecursoDatos.xlsx')

import plotly.express as px


banco_popular = data[data["BANCO"]=="BANCO POPULAR"]
##        banco_popular para este caso = data_set
## px.bar(data_set , x='X', y='Y')

fig = px.bar(banco_popular, x='fecha_reporte', y='CLIENTES')
fig.show()
