import streamlit as st
import importlib.util
import os
st.title("我的应用")
file_names = [
    "个人简历生成器",
    "南宁美食数据仪表",
    "视频网站",
    "相册",
    "项目部署",
    "音乐播放器"]

tabs = st.tabs(file_names)

for i, tab in enumerate(tabs):
    with tab:
        file_name = file_names[i]
        file_path = os.path.join("pages", f"{file_name}.py")

    
        spec = importlib.util.spec_from_file_location(file_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
       
