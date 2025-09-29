import streamlit as st
import pandas as pd

# 제목
st.title("MBTI Countries Dataset Viewer")

# 데이터 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 데이터 기본 정보 출력
st.subheader("데이터 상위 5행 미리보기")
st.dataframe(df.head())
