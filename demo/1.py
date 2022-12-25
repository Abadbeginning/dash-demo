import dash
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入我们的主角fac框架

app = dash.Dash(__name__)

app.layout = html.Div(
    # fac网格系统示例
    fac.AntdRow(
        [
            fac.AntdCol(
                html.Div(
                    fac.AntdStatistic(
                        title=f'指标{i}',
                        value=99999
                    ),
                    style={
                        'textAlign': 'center'  # 用于使Div内元素水平居中
                    }
                ),
                span=6
            )
            for i in range(1, 5)
        ],
        style={
            'marginTop': '100px'  # 用于在AntdRow()上方添加100像素留白
        }
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)