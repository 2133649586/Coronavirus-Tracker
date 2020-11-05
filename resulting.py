import ssl
# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd
from bokeh.core.properties import value
from bokeh.layouts import column, row
from bokeh.models import CustomJS, DatePicker, Div, ColumnDataSource, TableColumn, DataTable, HoverTool
from bokeh.plotting import figure, curdoc



total_path = "https://raw.githubusercontent.com/datadesk/california-coronavirus-data/master/cdph-state-totals.csv"
race_path = "https://raw.githubusercontent.com/datadesk/california-coronavirus-data/master/cdph-race-ethnicity.csv"

total_data = pd.read_csv(total_path)
race_data = pd.read_csv(race_path)
last_update_date = total_data["date"][0]

# to represent the source of data
introduce_of_data = Div(text = """all of the data we used in this visualization project is published by the California \
Department of Public Health, and we get the dataset with url from github repository : https://github.com/datadesk/california-coronavirus-data.
<b>Last update date: {}<b>""".format(last_update_date), width = 700, height= 80 )


# design date select options
date_picker = DatePicker(title='Select date', value="2020-08-11", min_date="2020-06-25", max_date=last_update_date)
selected_date = date_picker.value



# question a
increase_case = {"date":[selected_date],"confirm case":[]}
for i in range(len(total_data["date"])-1):
    if total_data["date"][i] == selected_date:
        increase_case["confirm case"].append(total_data["confirmed_cases"][i] - total_data["confirmed_cases"][i+1])

source_q1 = ColumnDataSource(increase_case)
columns1 = [TableColumn(field="date", title="Date"),TableColumn(field="confirm case", title="Increase confirm case")]
data_table1 = DataTable(source = source_q1, columns=columns1, width=400, height=120)



#question b,c
description = Div(text = """we can get answer of second and third question here, 2.For a particular day, what is the %percent cases by race compared to their representation in the 
general population? 3.For a particular day, what is the %percent deaths by race compared to their representation in the 
general population? And when you move mouse to certain area, the detail of parameter will displayed in right box. <b>Attention: if there is no any data in table or figure
, that means the search date is not exist in our data<b>""")

some = race_data[(race_data["age"]=="all") & (race_data["date"]==selected_date)]
particular_column = ["date","race","confirmed_cases_percent","deaths_percent","population_percent"]
particular_data = some[particular_column]
source_q23 = ColumnDataSource(data = particular_data)

columns23 = [TableColumn(field="date", title="Date"),TableColumn(field="race", title="Race"),
    TableColumn(field="confirmed_cases_percent", title="Confirmed cases percent")
    ,TableColumn(field="deaths_percent", title="Deaths percent"),TableColumn(field="population_percent", title="Population percent")]

data_table23 = DataTable(source = source_q23, columns=columns23, width=800, height=280)


# 创建数据
colors = ["#c9d9d3", "#718dbf", "#e84d60"]
para_column = ["confirmed_cases_percent","deaths_percent","population_percent"]
p = figure(x_range=particular_data["race"], plot_height=350, title="",tools="")
renderers = p.vbar_stack(para_column, #可以用years代替，就是上边设置的变量 # 设置堆叠值，这里source中包含了不同年份的值，years变量用于识别不同堆叠层
                         x='race',     # 设置x坐标
                         source=source_q23, #包含了2015/2016/2017的数据的；  主要设置的就是这3个参数
                         width=0.9, color=colors,
                         legend=[value(x) for x in para_column], name=para_column) #对整个数据做一个分组集合变成一个列表
# 绘制堆叠图
# 注意第一个参数需要放years
h = HoverTool(
    tooltips=[('confirmed cases percent %', '@confirmed_cases_percent'), ('deaths cases percent %', '@deaths_percent'), ('population percent %', '@population_percent')])
p.add_tools(h)
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
# 设置其他参数



def call_back(attr, old, new):
    # question a
    increase_case = {"date": [selected_date], "confirm case": []}
    for i in range(len(total_data["date"]) - 1):
        if total_data["date"][i] == selected_date:
            increase_case["confirm case"].append(
                total_data["confirmed_cases"][i] - total_data["confirmed_cases"][i + 1])

    source_q1 = ColumnDataSource(increase_case)


    # question b,c
    some = race_data[(race_data["age"] == "all") & (race_data["date"] == selected_date)]
    particular_column = ["date", "race", "confirmed_cases_percent", "deaths_percent", "population_percent"]
    particular_data = some[particular_column]
    source_q23 = ColumnDataSource(data=particular_data)

date_picker.on_change("value", call_back)
q1 = column(introduce_of_data,date_picker,data_table1)
q23 = column(description,p)
#show(column(q1,q23))
curdoc().add_root(column(q1,column(data_table23,q23)))






