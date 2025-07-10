import streamlit as st

st.set_page_config(page_title="MBTI 여행지 추천", page_icon="🌍", layout="centered")

st.title("🌟 MBTI 기반 여행지 추천기 🌟")
st.markdown("당신의 **MBTI**를 선택하면, 성격에 딱 맞는 여행지를 추천해드릴게요 ✈️")

mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_list)

travel_recommendations = {
    "ISTJ": [
        ("🇩🇪 베를린", "질서와 역사를 중시하는 ISTJ에게는 풍부한 역사와 정돈된 도시 구조를 지닌 베를린이 딱이에요."),
        ("🇯🇵 교토", "전통과 규칙을 존중하는 ISTJ는 고즈넉한 사찰과 정원이 있는 교토에서 힐링할 수 있어요."),
        ("🇨🇦 오타와", "조용하고 체계적인 환경을 선호하는 ISTJ에게 적합한 캐나다의 수도예요."),
    ],
    "ENFP": [
        ("🇹🇭 방콕", "에너지가 넘치는 ENFP에게 잘 맞는 곳! 밤 문화와 시장 탐방이 활발해요 🎉"),
        ("🇪🇸 바르셀로나", "예술과 열정이 넘치는 도시에서 자유로운 영혼을 펼칠 수 있어요 🎨"),
        ("🇲🇽 멕시코시티", "열정적이고 사람들과의 교류를 좋아하는 ENFP에게 최고의 놀이터예요 🌮"),
    ],
    "INTP": [
        ("🇸🇪 스톡홀름", "지적 자극을 중시하는 INTP는 북유럽 디자인과 기술에 빠져들 수 있어요 🧠"),
        ("🇺🇸 샌프란시스코", "기술 혁신의 중심지에서 창의력을 뽐내보세요 💻"),
        ("🇳🇱 암스테르담", "자전거로 자유롭게 다니며, 박물관 탐방을 즐길 수 있어요 🚲"),
    ],
    "ESFJ": [
        ("🇫🇷 파리", "사람들과 교류하며 감성을 나누는 것을 좋아하는 ESFJ에게는 파리가 제격이에요 💕"),
        ("🇰🇷 서울", "활기찬 도시에서 사람들과 교류하며 다양한 문화 체험 가능해요 🎎"),
        ("🇮🇹 로마", "전통과 낭만, 사람들과 함께하는 분위기를 만끽할 수 있어요 🍝"),
    ],
    # 여기에 다른 MBTI 유형들도 자유롭게 추가 가능
}

if selected_mbti:
    st.subheader(f"🎯 {selected_mbti} 유형에게 추천하는 여행지 TOP 3!")
    
    places = travel_recommendations.get(selected_mbti, None)
    
    if places:
        for place, reason in places:
            st.markdown(f"### {place}")
            st.markdown(f"👉 {reason}")
            st.markdown("---")
        st.success("즐거운 여행 되세요! 🎈")
        st.balloons()
    else:
        st.warning("앗! 아직 이 MBTI는 준비 중이에요. 곧 업데이트할게요! 🚧")
