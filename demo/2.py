import dash
import random
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入我们的主角fac框架

app = dash.Dash(__name__)

# 模拟数据
company2percent = {
    'A': 80,
    'B': 65,
    'C': 100,
    'D': 45
}

# 构建Dash应用网页内容的过程即为对layout属性赋值的过程
app.layout = html.Div(
    [
        fac.AntdTitle(
            '2022年第一季度各部门业务目标完成情况：',
            level=3
        ),
        fac.AntdText('示例中均为随机生成数据'),
        fac.AntdRow(
            [
                fac.AntdCol(
                    [
                        fac.AntdCard(
                            fac.AntdProgress(
                                percent=company2percent[apartment],
                                type='circle'
                            ),
                            title=f'部门{apartment}',
                            hoverable=True,
                            bodyStyle={
                                'display': 'flex',
                                'justifyContent': 'center'
                            }
                        ),
                        fac.AntdCard(
                            [
                                fac.AntdRow(
                                    [
                                        fac.AntdCol(
                                            fac.AntdText(
                                                f'员工{apartment}{i}：',
                                                strong=True
                                            ),
                                            flex='none'
                                        ),
                                        fac.AntdCol(
                                            fac.AntdProgress(
                                                percent=round(
                                                    random.uniform(20, 100), 1),
                                                strokeColor={
                                                    'from': '#00F5A0',
                                                    'to': '#00D9F5'
                                                }
                                            ),
                                            flex='auto'
                                        )
                                    ],
                                    style={
                                        'marginBottom': '10px',
                                        'width': '100%'
                                    }
                                )
                                for i in range(1, 10)
                            ],
                            title='各员工业绩目标完成情况',
                            hoverable=True,
                            style={
                                'textAlign': 'center',
                                'marginTop': '20px'
                            }
                        )
                    ],
                    span=6
                )
                for apartment in list('ABCD')
            ],
            gutter=20
        )
    ],
    style={
        'padding': '100px 200px'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)