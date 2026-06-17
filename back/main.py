from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RecommendRequest(BaseModel):
    genre: str
    mood: str
    situation: str

@app.get("/")
def read_root():
    return {"message": "K-Band Recommender API is running"}

@app.post("/recommend")
def recommend(request: RecommendRequest):
    genre = request.genre
    mood = request.mood
    situation = request.situation

    if genre == "록" and mood == "강렬한":
        band = "국카스텐"
        songs = ["거울", "붉은 밭"]
        similar_bands = ["쏜애플", "실리카겔"]
        reason = "폭발적인 보컬과 강한 밴드 사운드를 좋아하는 사용자에게 잘 어울립니다."
    elif genre == "록" and mood == "몽환적인":
        band = "쏜애플"
        songs = ["시퍼런 봄", "아지랑이"]
        similar_bands = ["국카스텐", "검정치마"]
        reason = "몽환적인 가사와 강렬한 기타 사운드를 함께 느낄 수 있는 밴드입니다."
    elif genre == "인디" and mood == "감성적인":
        band = "잔나비"
        songs = ["주저하는 연인들을 위해", "뜨거운 여름밤은 가고 남은 건 볼품없지만"]
        similar_bands = ["혁오", "검정치마"]
        reason = "따뜻하고 대중적인 인디 감성을 좋아하는 사용자에게 잘 어울립니다."
    elif genre == "인디" and mood == "잔잔한":
        band = "브로콜리너마저"
        songs = ["유자차", "앵콜요청금지"]
        similar_bands = ["옥상달빛", "92914"]
        reason = "담백하고 조용한 인디 음악을 듣고 싶을 때 어울리는 밴드입니다."
    elif genre == "펑크" and mood == "신나는":
        band = "크라잉넛"
        songs = ["말달리자", "밤이 깊었네"]
        similar_bands = ["노브레인", "레이지본"]
        reason = "빠르고 에너지 있는 펑크 록을 좋아하는 사용자에게 잘 어울립니다."
    elif genre == "펑크" and mood == "강렬한":
        band = "노브레인"
        songs = ["넌 내게 반했어", "미친 듯 놀자"]
        similar_bands = ["크라잉넛", "레이지본"]
        reason = "공연장에서 신나게 즐기기 좋은 강한 펑크 사운드를 가진 밴드입니다."
    elif genre == "모던록" and mood == "청량한":
        band = "데이브레이크"
        songs = ["좋다", "꽃길만 걷게 해줄게"]
        similar_bands = ["소란", "루시"]
        reason = "밝고 산뜻한 모던록 사운드를 좋아하는 사용자에게 잘 어울립니다."
    elif genre == "모던록" and mood == "감성적인":
        band = "루시"
        songs = ["개화", "조깅"]
        similar_bands = ["데이브레이크", "엔플라잉"]
        reason = "바이올린 사운드가 더해진 청량하고 감성적인 밴드 음악입니다."
    elif genre == "감성/발라드" and mood == "잔잔한":
        band = "넬"
        songs = ["기억을 걷는 시간", "Stay"]
        similar_bands = ["자우림", "못"]
        reason = "깊고 차분한 감성을 느끼고 싶을 때 잘 어울리는 밴드입니다."
    elif genre == "감성/발라드" and mood == "감성적인":
        band = "자우림"
        songs = ["스물다섯, 스물하나", "하하하쏭"]
        similar_bands = ["넬", "체리필터"]
        reason = "감정 표현이 뚜렷하고 오래 들어도 질리지 않는 밴드 음악입니다."
    elif genre == "시티팝/레트로" and mood == "청량한":
        band = "새소년"
        songs = ["긴 꿈", "난춘"]
        similar_bands = ["wave to earth", "실리카겔"]
        reason = "세련되고 감각적인 밴드 사운드를 좋아하는 사용자에게 잘 어울립니다."
    elif genre == "시티팝/레트로" and mood == "잔잔한":
        band = "wave to earth"
        songs = ["seasons", "bad"]
        similar_bands = ["92914", "새소년"]
        reason = "편안하고 분위기 있는 사운드를 듣고 싶을 때 좋은 밴드입니다."
    else:
        band = "루시"
        songs = ["개화", "조깅"]
        similar_bands = ["데이브레이크", "잔나비"]
        reason = "선택한 조건과 완전히 일치하는 규칙은 없지만, 대중적이고 청량한 밴드 사운드를 즐기기 좋습니다."

    if situation == "공부할 때":
        situation_tip = "집중을 방해하지 않으면서 분위기를 만들어주는 음악으로 듣기 좋습니다."
    elif situation == "산책할 때":
        situation_tip = "가볍게 걸으면서 기분을 정리할 때 잘 어울립니다."
    elif situation == "드라이브할 때":
        situation_tip = "이동 중에 분위기를 살려주고 지루함을 줄여주는 음악입니다."
    elif situation == "공연 준비할 때":
        situation_tip = "합주나 공연을 준비할 때 에너지를 끌어올리기 좋습니다."
    elif situation == "기분전환할 때":
        situation_tip = "답답한 기분을 바꾸고 싶을 때 듣기 좋습니다."
    elif situation == "새벽에 들을 때":
        situation_tip = "조용한 새벽 감성과 잘 어울리는 음악입니다."
    else:
        situation_tip = "선택한 상황에서 편하게 듣기 좋은 음악입니다."

    return {
        "band": band,
        "reason": reason,
        "songs": songs,
        "similar_bands": similar_bands,
        "situation_tip": situation_tip,
    }
