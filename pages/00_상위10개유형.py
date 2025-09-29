import streamlit as st
import pandas as pd
import altair as alt

# 제목
st.title("MBTI 유형별 평균 상위 10")

# 데이터 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# MBTI 유형별 평균 계산 (Country 제외)
mbti_means = df.drop(columns=["Country"]).mean().reset_index()
mbti_means.columns = ["MBTI", "Average"]

# 상위 10개 추출
top10 = mbti_means.sort_values("Average", ascending=False).head(10)

# Altair 막대 그래프
chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X("Average:Q", title="평균 비율"),
        y=alt.Y("MBTI:N", sort="-x", title="MBTI 유형"),
        tooltip=["MBTI", "Average"]
    )
)

# 그래프 출력
st.subheader("MBTI 유형별 평균 비율 Top 10")
st.altair_chart(chart, use_container_width=True)
