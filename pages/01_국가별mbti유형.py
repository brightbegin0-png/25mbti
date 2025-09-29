import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("🌍 나라별 MBTI 분포 시각화 📊🌈")

# 데이터 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 나라 선택 박스
country_list = df["Country"].tolist()
selected_country = st.selectbox("국가를 선택하세요 🌐", country_list)

# 선택한 나라의 데이터 추출
country_data = df[df["Country"] == selected_country].drop(columns=["Country"]).T
country_data.columns = ["비율"]
country_data = country_data.reset_index().rename(columns={"index": "MBTI"})

# Plotly rainbow 색상 팔레트
colors = px.colors.qualitative.Prism  # 화려한 색감
# 16개 맞춰주기 위해 반복
color_cycle = colors * (len(country_data) // len(colors) + 1)

# Plotly 그래프
fig = px.bar(
    country_data,
    x="MBTI",
    y="비율",
    color="MBTI",
    color_discrete_sequence=color_cycle,
    title=f"🇨🇭 {selected_country}의 MBTI 분포",
    text=country_data["비율"].map(lambda x: f"{x*100:.1f}%"),
)

fig.update_traces(textposition="outside")
fig.update_layout(
    yaxis=dict(title="비율", tickformat=".0%"),
    xaxis=dict(title="MBTI 유형"),
    showlegend=False,
    title_x=0.5,
    bargap=0.3,
)

# 출력
st.plotly_chart(fig, use_container_width=True)

# 데이터프레임도 함께 표시
st.subheader("📋 선택한 나라의 MBTI 분포 데이터")
st.dataframe(country_data.style.format({"비율": "{:.2%}"}))
