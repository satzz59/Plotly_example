import plotly.express as px
import pandas as pd

organic_teas = pd.read_excel('./Organic_Teas_db.xlsx')
summary_rating = organic_teas.groupby(['product_name','rating'])['rating'].size().to_frame('count_rating').reset_index()
print(summary_rating.head())

fig = px.bar(summary_rating,x='product_name',y='count_rating',color='rating')
fig.show()
