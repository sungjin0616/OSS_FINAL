import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://backend:8000/recommend")

st.title("K-Band Recommender")
st.write("취향을 선택하면 어울리는 한국 밴드를 추천해드립니다.")

st.sidebar.header("앱 정보")
st.sidebar.write("- Streamlit 프론트엔드")
st.sidebar.write("- FastAPI 백엔드")
st.sidebar.write("- Docker 기반 실행")
st.sidebar.write("- 한국 밴드 rule-based 추천 앱")

genre = st.selectbox("선호 장르", ["록", "인디", "펑크", "모던록", "감성/발라드", "시티팝/레트로"])
mood = st.selectbox("원하는 분위기", ["신나는", "감성적인", "강렬한", "몽환적인", "청량한", "잔잔한"])
situation = st.selectbox("듣는 상황", ["공부할 때", "산책할 때", "드라이브할 때", "공연 준비할 때", "기분전환할 때", "새벽에 들을 때"])

if st.button("추천 받기"):
    payload = {
        "genre": genre,
        "mood": mood,
        "situation": situation,
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
    except requests.exceptions.RequestException:
        st.error("백엔드 서버에 연결할 수 없습니다. FastAPI 서버가 실행 중인지 확인해주세요.")
    else:
        if response.status_code != 200:
            st.error("추천 결과를 가져오는 중 문제가 발생했습니다.")
        else:
            data = response.json()
            st.divider()
            st.subheader(f"추천 밴드: {data.get('band', '결과 없음')}")
            st.write(data.get("reason", "추천 이유를 가져올 수 없습니다."))

            songs = data.get("songs", [])
            if songs:
                st.write("**추천 입문곡**")
                for song in songs:
                    st.write(f"- {song}")

            similar_bands = data.get("similar_bands", [])
            if similar_bands:
                st.write("**함께 들어볼 만한 밴드**")
                st.write(", ".join(similar_bands))

            situation_tip = data.get("situation_tip")
            if situation_tip:
                st.write("**추천 상황 설명**")
                st.write(situation_tip)
