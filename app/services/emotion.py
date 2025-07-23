def analyze_emotion(text: str) -> tuple[str, str]:
    """텍스트를 기반으로 감정을 분석하고 이미지 경로를 반환"""
    keywords = {
        "불안": ["불안", "초조", "걱정"],
        "기쁨": ["기쁘", "좋았", "행복", "즐거"],
        "슬픔": ["슬프", "속상", "우울"],
        "화남": ["화가", "짜증", "분노"]
    }

    for emotion, word_list in keywords.items():
        for word in word_list:
            if word in text:
                return emotion, f"/static/images/{emotion}.png"
    
    # 기본값
    return "중립", "/static/images/neutral.png"