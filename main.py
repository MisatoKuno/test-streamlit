import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit 超入門")

st.write("interactive widgets")

#レイアウト
left_column,right_column=st.columns(2)
button=left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

exp=st.expander("問合せ")
exp.write("問い合わせ内容を書く")

"## プログレスバーの表示"
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

#マップ表示
# df=pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=["lat","lon"]
# )
# st.map(df)

#画像表示
# img=Image.open("スクリーンショット 2023-04-19 110824.png")
# st.image(img,caption="画像",use_column_width=True)

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# #静的な表を表示
# st.table(df.style.highlight_max(axis=0))

# #動的な表を表示
# st.dataframe(df,width=120,height=200)


#ウィジェット
if st.checkbox("Show Image"):
    img=Image.open("スクリーンショット 2023-04-19 110824.png")
    st.image(img,caption="画像",use_column_width=True)

option=st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)
"あなたの好きな数字は",option,"です"

text=st.sidebar.text_input("あなたの趣味を教えてください")
"あなたの趣味：",text

condi=st.sidebar.slider("あなたの今の調子は？",0,100,50)
"コンディション：",condi