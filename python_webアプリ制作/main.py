import streamlit as st
from PIL import Image
import time
st.title("Streamlit 超入門")#タイトル追加

#st.write("DataFrame")#テキストデータ記入

st.write("プログレスバー")
#st.write(df) データフレームの表示
latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.01)

"""Done!!"""

left_column,right_column = st.columns(2)
button = left_column.button("右カラムに表示")
if button:
    right_column.write("ここは右カラムです")

expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")
expander.write("問い合わせ内容を書く")
expander.write("問い合わせ内容を書く")
expander.write("問い合わせ内容を書く")
#st.map(df)#折れ線グラフの記入
option = st.text_input("あなたの趣味を教えてください")
condition = st.slider("あなたの今の調子は",0,100,100)


"あなたの趣味は:",option
"あなたの調子は:",condition
# if st.checkbox("Show Image"):
#   img = Image.open('sample.png')
#    st.image(img,caption = "ニューラルネットワーク",use_column_width=True)