# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 14:13
# @Author  : zhuhua
# @File    : fiancial_ana_graph.py
# @Software: PyCharm
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Grid, Scatter, WordCloud

import financial_ana_data


# today_df = financial_ana_data.stock_data_by_time('2022-5-5')
# named_df = financial_ana_data.stock_data_by_name("上海临港")
# print(today_df)


def stock_volume_slider_bar(df):
    if df is None:
        df = pd.DataFrame()
    df = df.dropna(subset=["成交量"])

    c = (
        Bar()
            .add_xaxis(df["股票名称"].values.tolist())
            .add_yaxis("股票成交量情况", df["成交量"].values.tolist())
            .set_global_opts(
            title_opts=opts.TitleOpts(title="成交量图表 - Volume chart（slider-水平）"),
            datazoom_opts=[opts.DataZoomOpts(),
                           opts.DataZoomOpts(type_="inside", )],

        )
            .render("..\\resources\\html\\" + "stock_volume_chart_slider.html")
    )


def stock_volume_vertical_bar(df):
    if df is None:
        df = pd.DataFrame()
    df = df.dropna(subset=["成交量"])
    c = (
        Bar()
            .add_xaxis(df["股票名称"].values.tolist())
            .add_yaxis("股票成交量情况", df["成交量"].values.tolist())
            .set_global_opts(
            title_opts=opts.TitleOpts(title="成交量图表 - Volume chart（slider-垂直）"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(orient="vertical"),
                           opts.DataZoomOpts(type_="inside")]
        )
            .render("..\\resources\\html\\" + "stock_volume_chart__slider_vertical.html")
    )


def stock_open_close_line(df):
    """
    绘制今开昨收折线图
    :param df: 只带一个数据的DataFrame
    :return:
    """
    if df is None:
        df = pd.DataFrame
    df = df.dropna(subset=["今开"])
    x = df["ISO时间"].values.tolist()
    y1 = df["今开"].values.tolist()
    y2 = df["昨收"].values.tolist()
    l1 = (
        Line()
            .add_xaxis(x)
            .add_yaxis(series_name="今开",
                       y_axis=y1,
                       # symbol_size=8,
                       is_hover_animation=False,
                       label_opts=opts.LabelOpts(is_show=False),
                       linestyle_opts=opts.LineStyleOpts(width=1.5),
                       # is_smooth=True,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='min')])

                       )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="今开昨收数据图", pos_left="center"
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            axispointer_opts=opts.AxisPointerOpts(
                is_show=True, link=[{"xAxisIndex": "all"}]
            ),
            datazoom_opts=[
                opts.DataZoomOpts(type_='inside'),
                opts.DataZoomOpts(
                    is_show=True,
                    is_realtime=True,
                    # start_value=30,
                    # end_value=70,
                    xaxis_index=[0, 1],
                )
            ],
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            ),
            yaxis_opts=opts.AxisOpts(name="今开"),
            legend_opts=opts.LegendOpts(pos_left="left"),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True,
                feature={
                    "dataZoom": {"yAxisIndex": "none"},
                    "restore": {},
                    "saveAsImage": {},
                },
            )
        )
    )
    l2 = (
        Line()
            .add_xaxis(x)
            .add_yaxis(
            series_name="昨收",
            y_axis=y2,
            # xaxis_index=1,
            # yaxis_index=1,
            # symbol_size=8,
            is_hover_animation=False,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=1.5),
            # is_smooth=True,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max')])
        )
            .set_global_opts(
            axispointer_opts=opts.AxisPointerOpts(
                is_show=True,
                link=[{"xAxisIndex": "all"}]
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            xaxis_opts=opts.AxisOpts(
                grid_index=1,
                type_="category",
                boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=True),
                # position="top",
            ),
            datazoom_opts=[
                opts.DataZoomOpts(type_='inside'),
                opts.DataZoomOpts(
                    is_realtime=True,
                    type_="inside",
                    # start_value=30,
                    # end_value=70,
                    xaxis_index=[0, 1],
                )
            ],
            yaxis_opts=opts.AxisOpts(name="昨收"),
            legend_opts=opts.LegendOpts(pos_left="7%"),
        )
    )
    (
        Grid(init_opts=opts.InitOpts(width="1024px", height="768px"))
            .add(
            chart=l1,
            grid_opts=opts.GridOpts(pos_left=50, pos_right=50, height="35%"))
            .add(
            chart=l2,
            grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="55%", height="35%"),
        )
            .render("..\\resources\\html\\" + "stock_open_close_line.html")
    )


def stock_close_volume_scatter(name):
    """
    绘制 股价和成交量散点图 ，分析其相关性
    :param name:
    :return:
    """
    df = financial_ana_data.stock_data_by_name(name)
    # df = df.dropna(subset=["昨收"])
    x = df["成交量"].values.tolist()
    y = df["昨收"].values.tolist()
    print(x)
    # print(y)
    c = (
        Scatter()
            .add_xaxis(x)
            .add_yaxis(name, y)
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(type_='value', name="成交量"),
            yaxis_opts=opts.AxisOpts(name="股价（RMB）"),
            title_opts=opts.TitleOpts(title=name + "Scatter-VisualMap(Size)"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=df["昨收"].max(), min_=df["昨收"].min()),
        )
            .render("..\\resources\\html\\" + "stock_close_volume_scatter_visualmap.html")
    )


def stock_close_worldcloud(time):
    df = financial_ana_data.stock_data_by_time(time)
    df = df.dropna(subset=["昨收"])
    df = df.sort_values(by="昨收", ascending=False)[["股票名称", "昨收"]]
    data = df.head(300).values.tolist()
    c = (
        WordCloud()
            .add(series_name="股价", data_pair=data, word_size_range=[20, 150])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="股价分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
            .render("..\\resources\\html\\" + "stock_close_wordcloud.html")
    )


stock_close_worldcloud("2022-5-6")
# stock_close_volume_scatter("上海临港")
# stock_volume_slider(today_df)
# stock_volume_vertical(financial_ana_data.stock_data_by_time('2022-5-5'))
# stock_open_close_line(financial_ana_data.stock_data_by_name("上海临港"))
