import streamlit as st

st.set_page_config(page_title='猫咖',page_icon='🐇')

images = [
     {'ur1': "https://doc-fd.zol-img.com.cn/t_s2000x2000/g7/M00/0D/01/ChMkK2acwHiINQfYAABZbwXg56gAAg0-QJi9sIAAFmH232.png",
      'parm': "hello kitty"
      },
     {'ur1': "https://p5.qhimg.com/d/dy_99a97e29c27cb6a57af441479b3e3875.jpg",
       'parm': 'hello kitty1'
      },
     {'ur1': "https://www.pixartprinting.co.uk/blog/wp-content/uploads/2024/06/Hello_Kitty.jpg",
      'parm':'hello kitty2'
      },
     {'ur1':"https://rhslegend.com/wp-content/uploads/2023/03/Hello-Kitty.png",
      'parm':'hello kitty3'
      }
]


if 'ind' not in st.session_state:
    st.session_state['ind']=0
    
def lastImg():
    st.session_state['ind']= (st.session_state['ind']-1) % len(images)
st.image(images[st.session_state['ind']]['ur1'],caption=images[st.session_state['ind']]['parm'])

def nextImg():
    st.session_state['ind']= (st.session_state['ind']+1) % len(images)

c1,c2 = st.columns(2)
with c1:
    st.button('上一张',on_click=nextImg,use_container_width=True)
with c2:
    st.button('下一张',on_click=nextImg,use_container_width=True)

