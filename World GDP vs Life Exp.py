import plotly.express as px
gapminder = px.data.gapminder() # 导入需要使用的数据集

gapminder2002 = gapminder.query('year == 2002')
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp',
            color='continent', size='pop', size_max=60,
            hover_name="country",
            hover_data=["year","continent","gdpPercap","lifeExp"],
            animation_frame='year', animation_group='country',
            range_y=[30, 100], range_x=[-5000, 55000],
            labels={'gdpPercap': 'GDP', 'lifeExp': 'Life Expectancy'}
                 )

fig2 = px.scatter(gapminder2002, x='gdpPercap', y='lifeExp',
           color='continent', size='pop', size_max=60,
            hover_name="country",
            hover_data=["year","continent","gdpPercap","lifeExp"],
                 facet_col="continent"
                  )

fig3 = px.choropleth(gapminder,
                     #locations:这个是接受国家每个国家的ISO3代码的, 也就是China就是CHN
                     locations = "iso_alpha",
                     color='lifeExp',
                     animation_frame="year",
                     color_continuous_scale=px.colors.diverging.RdBu,
                     projection='natural earth' #这个是可以选择地图的类型
                     )

fig3.update_layout(title='World GDP v.s. LifeExp',
                  font=dict(family="Courier New, monospace",size=18,color="#7f7f7f")
                 )

fig4 = px.scatter_geo(gapminder2002, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     size_max = 30,
                     projection="natural earth")


fig.show()
fig2.show()
fig3.show()
fig4.show()