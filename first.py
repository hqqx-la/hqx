import streamlit as st

st.title("学生 小古-数字档案")
st.header("🍉基础信息")
st.subheader("学生ID：:green[23031310129]")
st.subheader('注册时间: :yellow[2025-10-20]  |精神状态: :yellow[微疯]')
st.subheader('当前教室: :blue[实训楼204]  |安全等级: :blue[危险]')

st.markdown('# 展示美食')
st.image("https://th.bing.com/th/id/OIP.s6dpfSeTuglKhh1UbDEZDQHaE8?w=265&h=180&c=7&r=0&o=7&cb=12&pid=1.7&rm=3")

st.subheader('🏖️能力展示')
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="吃饭时间", value="10%", delta="2%")
c2.metric(label="追剧时间", value="30%", delta="4%")
c3.metric(label="睡觉时间", value="70%", delta="10%")



import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它

# 定义数据,以便创建数据框
data = {
    '任务':['吃早餐', '吃午餐', '吃晚餐'],
    '状态':['完成😁', '未完成😅', '未完成😅'],
    '难度':['困难', '简单', '简单'],
}
# 定义数据框所用的索引
index = pd.Series(['1', '2', '3', ], name='序号')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

import streamlit as st
import time
st.header("streamlit课程进度")
progress_text_1 = "streamlit课程进度"
my_bar = st.progress(0, text=progress_text_1)
time.sleep(0.5)


st.subheader('😀任务日志')
st.table(df)


st.markdown("## 🤣最新代码展示")
str='''
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={j*i},end='\t')
    print()
'''
st.code(str,language='python',line_numbers=True)
st.caption('这是一段python代码')
