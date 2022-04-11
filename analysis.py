import pyecharts.options as opts
from pyecharts.charts import Line, Page
import csv
import calendar

# data start in 1951
tavg: list[list[int]] = [[] for i in range(12)]
tmin: list[list[int]] = [[] for i in range(12)]
tmax: list[list[int]] = [[] for i in range(12)]

with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)
    cnt = 0
    for index, row in enumerate(reader):
        cnt += 1
        tavg[index % 12].append(row["TAVG"])
        tmin[index % 12].append(row["TMIN"])
        tmax[index % 12].append(row["TMAX"])
    assert cnt % 12 == 0


def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)

    for index, month_name in enumerate(list(calendar.month_name)[1:]):
        line = (
            Line()
            .add_xaxis(xaxis_data=[str(i) for i in range(1951, 2012)])
            .set_global_opts(
                title_opts=opts.TitleOpts(title=month_name),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            )
        )

        line.add_yaxis(
            series_name="TMAX",
            y_axis=tmax[index],
            label_opts=opts.LabelOpts(is_show=False),
            is_connect_nones=True,
        )
        line.add_yaxis(
            series_name="TAVG",
            y_axis=tavg[index],
            label_opts=opts.LabelOpts(is_show=False),
            is_connect_nones=True,
        )
        line.add_yaxis(
            series_name="TMIN",
            y_axis=tmin[index],
            label_opts=opts.LabelOpts(is_show=False),
            is_connect_nones=True,
        )
        page.add(line)

    page.render("result.html")


if __name__ == "__main__":
    page_simple_layout()
