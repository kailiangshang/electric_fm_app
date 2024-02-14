import streamlit as st


# 初始化app页面的配置
st.set_page_config(
    page_title='Electric Fast Modeling',
    page_icon=':volcano:',
)

# 设置页面的标题
st.title(':volcano: EleFM/:blue[_Electric_ Fast Modeling]', 
         help='This is a software that can quickly :red['
         '_visualize_] and :red[_model_] electric data, '
         'author : kailiangs')

# 显示软件的功能解释信息
st.info(
    body="#####  ``为了能够帮助电力相关的用户使用几乎无代码的方式进行电力数据的建模, "
    "电力大数据实验室推出了这个项目, 我们把它叫做``  EleFM 电力快速建模, "
    " `` 包括 `` 风速预测， 谐波建模， 负荷分类辨识 ``等方面， 囊括了`` 时序预测， 回归，分类，深度学习"
    " ``等方面， 并将`` AutoML 自动化机器学习 ``嵌入到其中, 使用者无需自己手动进行超参数调优即可进行模型构建`` ",
    icon="😎"
)

# 介绍特性
st.info(
    body="##### ````",
    icon="😉"
)

st.subheader(
    body=':one: Start',
    divider='violet'
)