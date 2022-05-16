import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots

organic_teas = pd.read_csv(
    'https://github.com/satzz59/Plotly_example/raw/main/Organic_Teas_db.csv')

# Graph 1
# Herbal/Organic Tea ratings:
# The below chart shows count of each rating (1 - 5) for different Herbal tea products.

summary_rating = organic_teas.groupby(['product_name', 'rating'])[
    'rating'].size().to_frame('count_rating').reset_index()

fig = px.bar(summary_rating, x='product_name', y='count_rating', color='rating', barmode='group',
             title="Organic/Herbal tea ratings", labels={'product_name': 'Product Name', 'count_rating': 'Count of Ratings'})
fig.show()

# Graph 2
# Total count of order of Herbal/Oraganic tea
# The below chart shows count of each order based on the ratings provided.

summary_total = organic_teas.groupby(
    ['product_name']).size().to_frame('count').reset_index()
fig = px.bar(summary_total, x='product_name', y='count', color='product_name',
             title="Organic/Herbal tea orders", labels={'product_name': 'Product Name', 'count': 'Count of Orders'})
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.show()

# Graph 3
# Product orders over the years
# The below graph shows the number of orders for each product over the years.

organic_teas['date'] = pd.to_datetime(organic_teas['date'])
organic_teas['Year'] = organic_teas['date'].dt.year
summary_year = organic_teas.groupby(
    ['product_name', 'Year']).size().to_frame('count_Year').reset_index()
figure = make_subplots(rows=3, cols=2, subplot_titles=('Organic India Tulsi Tea', 'Rishi Turmeric Tea', 'Yogi Antioxidant Tea',
                       'Pukka Ginger Turmeric Tea', 'Cellestial Seasonings Bengal Spice Tea', 'Twining America Herbal Peppermint Tea'))
fig1 = px.bar(summary_year[summary_year.product_name ==
              'organic-india-tulsi-tea'], x='Year', y='count_Year')
fig2 = px.bar(summary_year[summary_year.product_name ==
              'rishi-tea-turmeric'], x='Year', y='count_Year')
fig3 = px.bar(summary_year[summary_year.product_name ==
              'yogi-tea-antioxidant-reduce-radicals'], x='Year', y='count_Year')
fig4 = px.bar(summary_year[summary_year.product_name ==
              'pukka-ginger-turmeric-tea'], x='Year', y='count_Year')
fig5 = px.bar(summary_year[summary_year.product_name ==
              'cellestial-seasonings-bengal-spice-tea'], x='Year', y='count_Year')
fig6 = px.bar(summary_year[summary_year.product_name ==
              'twining-america-herbal-peppermint-tea'], x='Year', y='count_Year')

figure.add_trace(fig1['data'][0], row=1, col=1)
figure.add_trace(fig2['data'][0], row=1, col=2)
figure.add_trace(fig3['data'][0], row=2, col=1)
figure.add_trace(fig4['data'][0], row=2, col=2)
figure.add_trace(fig5['data'][0], row=3, col=1)
figure.add_trace(fig6['data'][0], row=3, col=2)

figure.show()

# Graph 4
# Products with highest negative ratings
# The below graph shows the products which has highest negative ratings (3 or below) against the total orders.

summary_join = summary_rating.merge(
    summary_total, on='product_name', how='left')
summary_join['negative_percent'] = (
    summary_join['count_rating']/summary_join['count'])*100
summary_neg = summary_join[(summary_join['rating'] < 4)]
summary_neg_3 = summary_neg.groupby(['product_name'])[
    'negative_percent'].sum().to_frame('count_neg').reset_index()
summary_neg_3['count_neg_char'] = summary_neg_3['count_neg'].round(
    2).astype(str)+' %'

summary_neg_3.head()
fig = px.bar(summary_neg_3, x='product_name', y='count_neg', color='product_name', title="Products with highest negative ratings",
             labels={'product_name': 'Product Name', 'count_neg': 'Percent of ratings 3 or below'})
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.show()

# Graph 5
# Number of non purchase review
# The below graph shows the number of reviews where the customer has not purchased the product but yet reviewed it. This can influence on the overall ratings of the product.
summary_bot = organic_teas.groupby(
    ['product_name', 'meta_data/verified_purchase']).size().to_frame('count_Bot').reset_index()
fig = px.bar(summary_bot, x='product_name', y='count_Bot', color='meta_data/verified_purchase', barmode='group', title="Number of non purchase review",
             labels={'product_name': 'Product Name', 'count_Bot': 'Count of Non-purchase review', 'meta_data/verified_purchase': 'Purchase Y/N'})
fig.show()
