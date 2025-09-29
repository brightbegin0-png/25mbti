import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📚 나라별 '책을 많이 읽는 MBTI' 지표 시각화")

# 데이터 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# '책을 많이 읽는 MBTI' 가설 유형군 (비공식/수업용)
reading_types = ["INFJ", "INFP", "INTP", "INTJ", "ENFP"]

st.write("가설: 책을 많이 읽는 MBTI 유형 =", ", ".join(reading_types))

# 나라별 독서 지표 계산 (해당 MBTI 비율 합산)
df["독서지표"] = df[reading_types].sum(axis=1)

# 상위 10개국
top10 = df[["Country", "독서지표"]].sort_values("독서지표", ascending=False).head(10)

# Plotly 시각화
fig = px.bar(
    top10,
    x="독서지표",
    y="Country",
    orientation="h",
    color="독서지표",
    color_continuous_scale="Rainbow",
    text=top10["독서지표"].map(lambda x: f"{x*100:.1f}%"),
    title="🌍 책을 많이 읽는 MBTI 지표 Top 10 국가"
)

fig.update_traces(textposition="outside")
fig.update_layout(
    xaxis_title="독서 지표 (%)",
    yaxis_title="국가",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# 개별 나라 선택
country = st.selectbox("국가를 선택해보세요 🌐", df["Country"])
score = df.loc[df["Country"] == country, "독서지표"].values[0]
st.write(f"📌 {country}의 '책을 많이 읽는 MBTI' 지표는 **{score*100:.2f}%** 입니다!")
