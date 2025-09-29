import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📖 나라별 문해력 지표 (MBTI 기반 가설)")

# 데이터 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 문해력이 높을 것 같은 MBTI 유형 (가설)
literacy_types = ["INTP", "INFJ", "INTJ", "INFP", "ENFP", "ENFJ"]

st.write("가설: 문해력이 높은 MBTI 유형 =", ", ".join(literacy_types))

# 나라별 문해력 지표 계산
df["문해력지표"] = df[literacy_types].sum(axis=1)

# 상위 10개국
top10 = df[["Country", "문해력지표"]].sort_values("문해력지표", ascending=False).head(10)

# Plotly 시각화
fig = px.bar(
    top10,
    x="문해력지표",
    y="Country",
    orientation="h",
    color="문해력지표",
    color_continuous_scale="Rainbow",
    text=top10["문해력지표"].map(lambda x: f"{x*100:.1f}%"),
    title="🌍 문해력 지표 Top 10 국가"
)

fig.update_traces(textposition="outside")
fig.update_layout(
    xaxis_title="문해력 지표 (%)",
    yaxis_title="국가",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# 선택한 나라 확인하기
country = st.selectbox("국가를 선택해보세요", df["Country"])
value = df.loc[df["Country"] == country, "문해력지표"].values[0]
st.write(f"📌 {country}의 문해력 지표는 **{value*100:.2f}%** 입니다!")
