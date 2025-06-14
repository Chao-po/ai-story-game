import streamlit as st
import openai

# 使用 Streamlit 的 secrets 儲存金鑰
api_key = st.secrets["openai_key"]

# ✅ 建立 OpenAI Client（關鍵修正點）
client = openai.OpenAI(api_key=api_key)

st.title("🎴 AI 神祇：事件劇情生成器")

prompt = st.text_area("請輸入事件敘述（例如：玩家A發動叛變攻擊B）")

if st.button("🎭 召喚神意"):
    if not prompt.strip():
        st.warning("請先輸入事件描述！")
    else:
        with st.spinner("神祇沉思中..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "你是桌遊中的神祇，負責生成古風劇情與遊戲效果指令"},
                    {"role": "user", "content": f"""
事件說明：
{prompt}
請用三行以內敘述故事，並附上三條具體遊戲效果指令，格式如下：

故事：
指令：
"""}
                ]
            )

            reply = response.choices[0].message.content
            st.success("神意降臨：")
            st.text_area("GPT 回應", reply, height=250)
