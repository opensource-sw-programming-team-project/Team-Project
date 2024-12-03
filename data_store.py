# 타임존 정보
time_zones = {
    "한국": "Asia/Seoul",
    "일본": "Asia/Tokyo",
    "중국": "Asia/Shanghai",
    "인도": "Asia/Kolkata",
    "인도네시아": "Asia/Jakarta",
    "아랍에미리트": "Asia/Dubai",
    "호주": "Australia/Sydney",
    "러시아": "Europe/Moscow",
    "영국": "Europe/London",
    "독일": "Europe/Berlin",
    "프랑스": "Europe/Paris",
    "네덜란드": "Europe/Amsterdam",
    "이탈리아": "Europe/Rome",
    "남아프리카 공화국": "Africa/Johannesburg",
    "이집트": "Africa/Cairo",
    "브라질": "America/Sao_Paulo",
    "미국": "America/New_York",
    "미국": "America/Los_Angeles",
    "캐나다": "America/Toronto",
    "멕시코": "America/Mexico_City",
    "아르헨티나": "America/Argentina/Buenos_Aires",
} #여러 국가의 타임존을 미리 저장후 불러오기

#국가 코드 정보(박재우)
country_code = {
    "아랍에미리트" : "AED",
    "호주" : "AUD",
    "바레인" : "BHD",
    "브루나이" : "BND",
    "캐나다" : "CAD",
    "스위스" : "CHF",
    "중국" : "CNH",
    "덴마크" : "DKK",
    "유로연합" : "EUR",
    "영국" : "GBP",
    "홍콩" : "HKD",
    "인도네시아" : "IDR(100)",
    "일본" : "JPY(100)",
    "한국" : "KRW",
    "쿠웨이트" : "KWD",
    "말레이시아" : "MYR",
    "노르웨이" : "NOK",
    "뉴질랜드" : "NZD",
    "사우디아라비아" : "SAR",
    "스웨덴" : "SEK",
    "싱가포르" : "SGD",
    "태국" : "THB",
    "미국" : "USD",
    "인도" : "IDR(100)"
} #국가와 국가코드를 매칭

# 국가명과 수도의 좌표 매핑(Chat GPT 사용)
capital_mapping = {
    '가나': {'latitude': 5.6037, 'longitude': -0.1870},
    '가봉' : {'latitude': 0.4162, 'longitude': 9.4673},
    '가이아나': {'latitude': 6.8013, 'longitude': -58.1551},
    '과테말라': {'latitude': 14.6349, 'longitude': -90.5069},
    '그리스': {'latitude': 37.9838, 'longitude': 23.7275},
    '기니' : {'latitude': 9.6412, 'longitude': -13.5784},
    '나미비아' : {'latitude': -22.5609, 'longitude': 17.0658},
    '나이지리아': {'latitude': 9.0765, 'longitude': 7.3986},
    '남수단' : {'latitude': 4.8594, 'longitude': 31.5713},
    '남수단공화국' : {'latitude': 4.8594, 'longitude': 31.5713},
    '남아프리카공화국': {'latitude': -25.7479, 'longitude': 28.2293},
    '네덜란드': {'latitude': 52.3676, 'longitude': 4.9041},
    '네팔': {'latitude': 27.7172, 'longitude': 85.3240},
    '노르웨이': {'latitude': 59.9139, 'longitude': 10.7522},
    '뉴질랜드': {'latitude': -41.2865, 'longitude': 174.7762},
    '니제르' : {'latitude': 13.5116, 'longitude': 2.1254},
    '대만': {'latitude': 25.0330, 'longitude': 121.5654},
    '대한민국': {'latitude': 37.5665, 'longitude': 126.9780},
    '덴마크': {'latitude': 55.6761, 'longitude': 12.5683},
    '독일': {'latitude': 52.5200, 'longitude': 13.4050},
    '라오스': {'latitude': 17.9757, 'longitude': 102.6331},
    '라트비아': {'latitude': 56.9496, 'longitude': 24.1052},
    '러시아': {'latitude': 55.7558, 'longitude': 37.6176},
    '루마니아': {'latitude': 44.4268, 'longitude': 26.1025},
    '르완다' : {'latitude': -1.9579, 'longitude': 30.1127},
    '리비아' : {'latitude': 32.8872, 'longitude': 13.1913},
    '리투아니아': {'latitude': 54.6872, 'longitude': 25.2797},
    '마다가스카르': {'latitude': -18.8792, 'longitude': 47.5079},
    '말레이시아': {'latitude': 3.1390, 'longitude': 101.6869},
    '말리' : {'latitude': 12.6392, 'longitude': -8.0029},
    '멕시코': {'latitude': 19.4326, 'longitude': -99.1332},
    '모로코' : {'latitude': 34.0207, 'longitude': -6.8416},
    '모리타니' : {'latitude': 18.0735, 'longitude': -15.9582},
    '모잠비크' : {'latitude': -25.9653, 'longitude': 32.5892},
    '몽골': {'latitude': 47.8864, 'longitude': 106.9057},
    '미국': {'latitude': 38.9072, 'longitude': -77.0369},
    '미얀마': {'latitude': 19.7633, 'longitude': 96.0785},
    '바누아투' : {'latitude': -17.7333, 'longitude': 168.3273},
    '방글라데시': {'latitude': 23.8103, 'longitude': 90.4125},
    '베네수엘라': {'latitude': 10.4806, 'longitude': -66.9036},
    '베트남': {'latitude': 21.0285, 'longitude': 105.8542},
    '벨기에': {'latitude': 50.8503, 'longitude': 4.3517},
    '벨라루스': {'latitude': 53.9006, 'longitude': 27.5590},
    '보츠와나' : {'latitude': -24.6282, 'longitude': 25.9231},
    '볼리비아': {'latitude': -16.5000, 'longitude': -68.1500},
    '부르키나파소' : {'latitude': 12.3714, 'longitude': -1.5197},
    '북마케도니아': {'latitude': 41.9981, 'longitude': 21.4254},
    '불가리아' : {'latitude': 42.6977, 'longitude': 23.3219},
    '브라질': {'latitude': -15.8267, 'longitude': -47.9218},
    '사우디아라비아': {'latitude': 24.7136, 'longitude': 46.6753},
    '세네갈' : {'latitude': 14.6928, 'longitude': -17.4467},
    '세르비아': {'latitude': 44.7866, 'longitude': 20.4489},
    '소말리아' : {'latitude': 2.0469, 'longitude': 45.3182},
    '솔로몬제도': {'latitude': -9.4289, 'longitude': 159.9602},
    '수단' : {'latitude': 15.5007, 'longitude': 32.5599},
    '수리남': {'latitude': 5.8520, 'longitude': -55.2038},
    '스리랑카' : {'latitude': 6.9271, 'longitude': 79.8612},
    '스웨덴': {'latitude': 59.3293, 'longitude': 18.0686},
    '스위스': {'latitude': 46.9480, 'longitude': 7.4474},
    '스페인': {'latitude': 40.4168, 'longitude': -3.7038},
    '슬로바키아': {'latitude': 48.1486, 'longitude': 17.1077},
    '시리아': {'latitude': 33.5138, 'longitude': 36.2765},
    '아랍에미리트': {'latitude': 24.4539, 'longitude': 54.3773},
    '아르헨티나': {'latitude': -34.6037, 'longitude': -58.3816},
    '아이슬란드': {'latitude': 64.1355, 'longitude': -21.8954},
    '아일랜드' : {'latitude': 53.3498, 'longitude': -6.2603},
    '아제르바이잔': {'latitude': 40.4093, 'longitude': 49.8671},
    '아프가니스탄': {'latitude': 34.5553, 'longitude': 69.2075},
    '알바니아': {'latitude': 41.3275, 'longitude': 19.8187},
    '알제리' : {'latitude': 36.7372, 'longitude': 3.0865},
    '앙골라' : {'latitude': -8.8390, 'longitude': 13.2894},
    '에리트레아' : {'latitude': 15.3229, 'longitude': 38.9251},
    '에콰도르': {'latitude': -0.1807, 'longitude': -78.4678},
    '에티오피아': {'latitude': 9.1450, 'longitude': 40.4897},
    '영국': {'latitude': 51.5074, 'longitude': -0.1278},
    '예멘' : {'latitude': 15.3694, 'longitude': 44.1910},
    '오만' : {'latitude': 23.5859, 'longitude': 58.4059},
    '오스트레일리아': {'latitude': -35.2809, 'longitude': 149.1300},
    '오스트리아': {'latitude': 48.2082, 'longitude': 16.3738},
    '온두라스': {'latitude': 14.0723, 'longitude': -87.1921},
    '우간다' : {'latitude': 0.3476, 'longitude': 32.5825},
    '우루과이': {'latitude': -34.9011, 'longitude': -56.1645},
    '우즈베키스탄': {'latitude': 41.2995, 'longitude': 69.2401},
    '우크라이나': {'latitude': 50.4501, 'longitude': 30.5234},
    '이라크': {'latitude': 33.3152, 'longitude': 44.3661},
    '이란': {'latitude': 35.6892, 'longitude': 51.3890},
    '이스라엘': {'latitude': 31.7683, 'longitude': 35.2137},
    '이집트': {'latitude': 30.0444, 'longitude': 31.2357},
    '이탈리아': {'latitude': 41.9028, 'longitude': 12.4964},
    '인도': {'latitude': 28.6139, 'longitude': 77.2090},
    '인도네시아': {'latitude': -6.2088, 'longitude': 106.8456},
    '일본': {'latitude': 35.6895, 'longitude': 139.6917},
    '자메이카': {'latitude': 18.0179, 'longitude': -76.8099},
    '잠비아' : {'latitude': -15.3875, 'longitude': 28.3228},
    '적도기니' : {'latitude': 3.7500, 'longitude': 8.7833},
    '중국': {'latitude': 39.9042, 'longitude': 116.4074},
    '중앙아프리카공화국' : {'latitude': 4.3947, 'longitude': 18.5582},
    '짐바브웨' : {'latitude': -17.8252, 'longitude': 31.0335},
    '차드' : {'latitude': 12.6348, 'longitude': 15.0744},
    '체코': {'latitude': 50.0755, 'longitude': 14.4378},
    '칠레': {'latitude': -33.4489, 'longitude': -70.6693},
    '카메룬' : {'latitude': 3.8480, 'longitude': 11.5021},
    '카보베르데' : {'latitude': 14.9330, 'longitude': -23.5133},
    '카자흐스탄': {'latitude': 51.1694, 'longitude': 71.4491},
    '캐나다': {'latitude': 45.4215, 'longitude': -75.6972},
    '케냐': {'latitude': -1.2864, 'longitude': 36.8172},
    '콜롬비아': {'latitude': 4.7110, 'longitude': -74.0721},
    '콩고': {'latitude': -4.2634, 'longitude': 15.2429},
    '콩고공화국' : {'latitude': -4.2634, 'longitude': 15.2429},
    '콩고민주공화국' : {'latitude': -4.4419, 'longitude': 15.2663},
    '쿠바': {'latitude': 23.1136, 'longitude': -82.3666},
    '크로아티아': {'latitude': 45.8130, 'longitude': 15.9775},
    '키르기스스탄' : {'latitude': 42.8746, 'longitude': 74.6121},
    '타이': {'latitude': 13.7563, 'longitude': 100.5018},
    '타지키스탄' : {'latitude': 38.5598, 'longitude': 68.7870},
    '탄자니아' : {'latitude': -6.7924, 'longitude': 39.2083},
    '태국': {'latitude': 13.7563, 'longitude': 100.5018},
    '통가' : {'latitude': -21.1394, 'longitude': -175.2012},
    '투르크메니스탄' : {'latitude': 37.9601, 'longitude': 58.3797},
    '튀니지' : {'latitude': 36.8065, 'longitude': 10.1815},
    '튀르키예': {'latitude': 39.9334, 'longitude': 32.8597},
    '파나마' : {'latitude': 8.9833, 'longitude': -79.5167},
    '파라과이': {'latitude': -25.2637, 'longitude': -57.5759},
    '파키스탄': {'latitude': 33.6844, 'longitude': 73.0479},
    '파푸아뉴기니': {'latitude': -9.4438, 'longitude': 147.1803},
    '페루': {'latitude': -12.0464, 'longitude': -77.0428},
    '포르투갈': {'latitude': 38.7169, 'longitude': -9.1399},
    '폴란드': {'latitude': 52.2297, 'longitude': 21.0122},
    '프랑스': {'latitude': 48.8566, 'longitude': 2.3522},
    '핀란드': {'latitude': 60.1695, 'longitude': 24.9355},
    '필리핀': {'latitude': 14.5995, 'longitude': 120.9842},
    '한국': {'latitude': 37.5665, 'longitude': 126.9780},
    '헝가리': {'latitude': 47.4979, 'longitude': 19.0402},
    '호주': {'latitude': -35.2809, 'longitude': 149.1300}
    # 다른 국가 추가 가능
}

# 불용어 제거를 위한 조사 리스트
stopwords = ['은', '는', '이', '가', '을', '를', '에', '의', '에서', '도', '으로', '하다']

# 키워드 정의 딕셔너리
intents = {
    "greeting": ["안녕", "하이", "안녕하세요", "ㅎㅇ"],
    "emotion_joy_request": ["행복하다", "행복해", "행복했어", "기쁘다", "기뻐", "기뻤어"],
    "emotion_sadness_request": ["슬프다", "슬퍼", "슬펐어", "속상하다", "속상해", "속상했어", "ㅜㅜ", "ㅠㅠ"],
    "emotion_anger_request": ["화난다", "화나", "화났어"],
    "emotion_boredom_request": ["지루하다", "지루해", "지루했어", "심심하다", "심심해", "심심했어"],
    "time_request": ["몇 시", "시간", "몇시"],
    "help_request": ["도와줘", "도움", "어떻게"],
    "exchange_rate_request": ["환율", "환율정보", "환전"], #환율 정보 API 키워드(박재우)
    "weather_request": ["날씨", "기온", "온도"],
    "air_pollution_request": ["대기오염", "공기", "미세먼지", "초미세먼지"],
    "menu_request" : ["메뉴추천", "메뉴", "저녁추천", "아침추천", "점심추천"],
    "menu_type" : ["국", "밥", "후식", "반찬"],
    "random_book_request" : ["책", "도서"],
    "random_fortune_telling_request" : ["운세"],
    "random_movie_request" : ["영화"],
    "random_music_request" : ["음악", "노래"]
}

menu_type_DB = {
    "밥" : "밥",
    "국" : "국",
    "후식" : "후식" ,
    "반찬" : "반찬"
}
# 책 리스트
book_list = [
    {'제목': '햄릿', '저자': '윌리엄 셰익스피어'},
    {'제목': '리어왕', '저자': '윌리엄 셰익스피어'},
    {'제목': '오셀로', '저자': '윌리엄 셰익스피어'},
    {'제목': '멕베스', '저자': '윌리엄 셰익스피어'},
    {'제목': '노인과 바다', '저자': '어니스트 헤밍웨이'},
    {'제목': '오만과 편견', '저자': '제인 오스틴'},
    {'제목': '노트르담의 꼽추', '저자': '빅토르 위고'},
    {'제목': '변신', '저자': '프란츠 카프카'},
    {'제목': '1984', '저자': '조지 오웰'},
    {'제목': '젊은 베르테르의 슬픔', '저자': '요한 볼프강 폰 괴테'},

    {'제목': '채식주의자', '저자': '한강'},
    {'제목': '소년이 온다', '저자': '한강'},
    {'제목': '가면산장 살인사건', '저자': '히가시노 게이고'},
    {'제목': '데미안', '저자': '헤르만 헤세'},
    {'제목': '인간 실격', '저자': '다자이 오사무'},
    {'제목': '이방인', '저자': '알베르 카뮈'},
    {'제목': '호밀밭의 파수꾼', '저자': '제롬 데이비드 샐린저'},
    {'제목': '돈키호테', '저자': '미겔 데 세르반테스 사아베드라'},
    {'제목': '폭풍의 언덕', '저자': '에밀리 제인 브론테'},
    {'제목': '구운몽', '저자': '김만중'},

    {'제목': '리버보이', '저자': '팀 보울러'},
    {'제목': '연을 쫓는 아이', '저자': '할레드 호세이니'},
    {'제목': '돌이킬 수 있는', '저자': '문목하'},
    {'제목': '1차원이 되고 싶어', '저자': '박상영'},
    {'제목': '나미야 잡화점의 기적', '저자': '히가시노 게이고'},
    {'제목': '지구에서 한아뿐', '저자': '정세랑'},
    {'제목': '세이노의 가르침', '저자': '세이노'},
    {'제목': '세상의 마지막 기차역', '저자': '무라세 다케시'},
    {'제목': '어느 날, 내 죽음에 네가 들어왔다', '저자': '세이카 료겐'},
    {'제목': '오늘 밤, 세계에서 이 사랑이 사라진다 해도', '저자': '이치조 미사키'},

    {'제목': '요리코를 위해', '저자': '노리즈키 린타로'},
    {'제목': '우리는 여기에 없었다', '저자': '안드레아 바츠'},
    {'제목': '파친코', '저자': '이민진'},
    {'제목': '열린 어둠', '저자': '렌조 미키히코'},
    {'제목': '지위 게임', '저자': '윌 스토'},
    {'제목': '우리가 빛의 속도로 갈 수 없다면', '저자': '김초엽'},
    {'제목': '나와 너의 365일', '저자': '유이하'},
    {'제목': '잊혀진 계절', '저자': '김도형'},
    {'제목': '내일을 준 너에게, 마지막 러브레터를', '저자': '고자쿠라 스즈'},
    {'제목': '멘탈을 바꿔야 인생이 바뀐다', '저자': '박세니'},

    {'제목': '당신은 결국 무엇이든 해내는 사람', '저자': '김상현'},
    {'제목': '하우스 메이드', '저자': '프리다 맥파든'},
    {'제목': '앵무새 죽이기', '저자': '하퍼 리'},
    {'제목': '소문', '저자': '오기와라 히로시'},
    {'제목': '바다가 들리는 편의점', '저자': '미치다 소노코'},
    {'제목': '불편한 편의점', '저자': '김호연'},
    {'제목': '좁은 문', '저자': '앙드레 지드'},
    {'제목': '주홍글씨', '저자': '너대니얼 호손'},
    {'제목': '안네의 일기', '저자': '안네 프랑크'},
    {'제목': '긴긴밤', '저자': '루리'},

    {'제목': '코스모스', '저자': '칼 세이건'},
    {'제목': '총 균 쇠', '저자': '재레드 다이아몬드'},
    {'제목': '용의자 X의 헌신', '저자': '히가시노 게이고'},
    {'제목': '악의', '저자': '히가시노 게이고'},
    {'제목': '백야행', '저자': '히가시노 게이고'},
    {'제목': '꿈꾸는 다락방', '저자': '이지성'},
    {'제목': '2억 빚을 진 내게 우주님이 가르쳐준 운이 풀리는 말버릇', '저자': '고이케 히로시'},
    {'제목': '죄와 벌', '저자': '도스토예프스키'},
    {'제목': '아몬드', '저자': '손원평'},
    {'제목': '위대한 개츠비', '저자': '스콧 피츠제럴드'},

    {'제목': '동물농장', '저자': '조지 오웰'},
    {'제목': '작별하지 않는다', '저자': '한강'},
    {'제목': '흰', '저자': '한강'},
    {'제목': '너도 하늘말나리야', '저자': '이금이'},
    {'제목': '수레바퀴 아래서', '저자': '헤르만 헤세'},
    {'제목': '완득이', '저자': '김려령'},
    {'제목': '몽실언니', '저자': '권정생'},
    {'제목': '이 지랄맞음이 쌓여 축제가 되겠지', '저자': '조승리'},
    {'제목': '날씨가 좋으면 찾아가겠어요', '저자': '이도우'},
    {'제목': '나는 왜 남들보다 쉽게 지칠까', '저자': '최재훈'},

    {'제목': '서랍에 저녁을 넣어 두었다', '저자': '한강'},
    {'제목': '대도시의 사랑법', '저자': '박상영'},
    {'제목': '즐거운 어른', '저자': '이옥선'},
    {'제목': '베를린에는 육개장이 없어서', '저자': '전성진'},
    {'제목': '급류', '저자': '정대건'},
    {'제목': '한 스푼의 시간', '저자': '구병모'},
    {'제목': '넥서스', '저자': '유발 하라리'},
    {'제목': '인생의 의미', '저자': '토마스 힐란드 에릭센'},
    {'제목': '아주 작은 습관의 힘', '저자': '제임스 클리어'},
    {'제목': '내면소통', '저자': '김주환'},

    {'제목': '사피엔스', '저자': '유발 하라리'},
    {'제목': '불변의 법칙', '저자': '모건 하우절'},
    {'제목': '전제의 법칙', '저자': '네빌 고다드'},
    {'제목': '이처럼 사소한 것들', '저자': '클레어 키건'},
    {'제목': '위저드 베이커리', '저자': '구병모'},
    {'제목': '기분이 태도가 되지 말자', '저자': '김수현'},
    {'제목': '이기적 유전자', '저자': '리처드 도킨스'},
    {'제목': '이토록 평범한 미래', '저자': '김연수'},
    {'제목': '그대들 어떻게 살 것인가', '저자': '요시노 겐자부로'},
    {'제목': '내가 틀릴 수도 있습니다', '저자': '비욘 나티코 린데블라드'},

    {'제목': '걸리버 여행기', '저자': '조나단 스위프트'},
    {'제목': '불안의 서', '저자': '페르난두 페소아'},
    {'제목': '어른의 중력', '저자': '사타 도일 바이옥'},
    {'제목': '셜록 홈즈', '저자': '아서 코난 도일'},
    {'제목': '말의 트렌드', '저자': '정유라'},
    {'제목': '왜 일하는가', '저자': '이나모리 가즈오'},
    {'제목': '정의란 무엇인가', '저자': '마이클 샌델'},
    {'제목': '쓰게 될 것', '저자': '최진영'},
    {'제목': '두 사람의 인터내셔널', '저자': '김진영'},
    {'제목': '홍학의 자리', '저자': '정해연'},

]

# 영화 리스트
movie_list = [
    {'제목': '기생충', '감독': '봉준호'},
    {'제목': '택시운전사', '감독': '장훈'},
    {'제목': '어바웃 타임', '감독': '리차드 커티스'},
    {'제목': '명량', '감독': '김한민'},
    {'제목': '극한직업', '감독': '이병헌'},
    {'제목': '국제시장', '감독': '윤제균'},
    {'제목': '아바타', '감독': '제임스 카메론'},
    {'제목': '서울의 봄', '감독': '김성수'},
    {'제목': '7번방의 선물', '감독': '이환경'},
    {'제목': '파묘', '감독': '장재현'},

    {'제목': '부산행', '감독': '연상호'},
    {'제목': '변호인', '감독': '양우석'},
    {'제목': '해운대', '감독': '윤제균'},
    {'제목': '괴물', '감독': '봉준호'},
    {'제목': '모가디슈', '감독': '류승완'},
    {'제목': '소년시절의 너', '감독': '증국상'},
    {'제목': '파일럿', '감독': '김한결'},
    {'제목': '탈주', '감독': '이종필'},
    {'제목': '청년경찰', '감독': '김주환'},
    {'제목': '너의 이름은.', '감독': '신카이 마코토'},

    {'제목': '날씨의 아이', '감독': '신카이 마코토'},
    {'제목': '센과 치히로의 행방불명', '감독': '미야자키 하야오'},
    {'제목': '갓파 쿠와 여름방학을', '감독': '하라 케이이치'},
    {'제목': '마음이 외치고 싶어해', '감독': '쿠마자와 나오토'},
    {'제목': '목소리의 형태', '감독': '야마다 나오코'},
    {'제목': '추억의 마니', '감독': '요네바야시 히로마사'},
    {'제목': '비긴 어게인', '감독': '존 카니'},
    {'제목': '인터스텔라', '감독': '크리스토퍼 놀란'},
    {'제목': '미스 페레그린과 이상한 아이들의 집', '감독': '팀 버튼'},
    {'제목': '거울나라의 앨리스', '감독': '팀 버튼'},

    {'제목': '타이타닉', '감독': '제임스 카메론'},
    {'제목': '인사이드 아웃', '감독': '켈시 맨'},
    {'제목': '룩백', '감독': '오시야마 키요타카'},
    {'제목': '시간을 달리는 소녀', '감독': '호소다 마모루'},
    {'제목': '라푼젤', '감독': '네이슨 그레노'},
    {'제목': '엘리멘탈', '감독': '피터 손'},
    {'제목': '코코', '감독': '리 언크리치'},
    {'제목': '주토피아', '감독': '바이론 하워드'},
    {'제목': '업', '감독': '피트 닥터'},
    {'제목': '빅 피쉬', '감독': '팀 버튼'},

    {'제목': '노트북', '감독': '닉 카사베츠'},
    {'제목': '라라랜드', '감독': '데이미언 셔젤'},
    {'제목': '위대한 쇼맨', '감독': '마이클 그레이시'},
    {'제목': '박물관이 살아있다', '감독': '숀 레비'},
    {'제목': '레미제라블', '감독': '톰 후퍼'},
    {'제목': '인생은 아름다워', '감독': '최국희'},
    {'제목': '아이 캔 스피크', '감독': '김현석'},
    {'제목': '써니', '감독': '강형철'},
    {'제목': '수상한 그녀', '감독': '황동혁'},
    {'제목': '국가대표', '감독': '김용화'},

    {'제목': '세 얼간이', '감독': '라지쿠마르 히라니'},
    {'제목': '탑건', '감독': '조셉 코신스키'},
    {'제목': '인셉션', '감독': '크리스토퍼 놀란'},
    {'제목': '설국열차', '감독': '봉준호'},
    {'제목': '어스', '감독': '조던 필'},
    {'제목': '겟 아웃', '감독': '조던 필'},
    {'제목': '곡성', '감독': '나홍진'},
    {'제목': '화이트 칙스', '감독': '키넨 아이보리 웨이언스'},
    {'제목': '미드소마', '감독': '아리 에스터'},
    {'제목': '베테랑', '감독': '류승완'},

    {'제목': '헌트', '감독': '이정재'},
    {'제목': '관상', '감독': '한재림'},
    {'제목': '다만 악에서 구하소서', '감독': '홍원찬'},
    {'제목': '밀수', '감독': '류승완'},
    {'제목': '비공식작전', '감독': '김성훈'},
    {'제목': '쥬만지', '감독': '조 존스톤'},
    {'제목': '사운드 오브 뮤직', '감독': '로버트 와이즈'},
    {'제목': '왕의 남자', '감독': '이준익'},
    {'제목': '그랜드 부다페스트 호텔', '감독': '웨스 앤더슨'},
    {'제목': '화양연화', '감독': '왕가위'},

    {'제목': '올드보이', '감독': '박찬욱'},
    {'제목': '라따뚜이', '감독': '브래드 버드'},
    {'제목': '조디악', '감독': '데이비드 핀처'},
    {'제목': '그것', '감독': '안드레스 무시에티'},
    {'제목': '도둑들', '감독': '최동훈'},
    {'제목': '실미도', '감독': '강우석'},
    {'제목': '태극기 휘날리며', '감독': '강제규'},
    {'제목': '알포인트', '감독': '공수창'},
    {'제목': '잠', '감독': '유재선'},
    {'제목': '콘스탄틴', '감독': '프란시스 로렌스'},

    {'제목': '트루먼 쇼', '감독': '피터 위어'},
    {'제목': '미 비포 유', '감독': '테아 샤록'},
    {'제목': '하모니', '감독': '강대규'},
    {'제목': '히말라야', '감독': '이석훈'},
    {'제목': '월-E', '감독': '앤드류 스탠튼'},
    {'제목': '마가렛', '감독': '케네스 로너건'},
    {'제목': '타인의 삶', '감독': '플로리안 헨켈 폰 도너스마르크'},
    {'제목': '악마는 프다라를 입는다', '감독': '데이빗 프랭클'},
    {'제목': '메멘토', '감독': '크리스토퍼 놀란'},
    {'제목': '로마의 휴일', '감독': '이덕희'},

    {'제목': '굿 윌 헌팅', '감독': '구스 반 산트'},
    {'제목': '타짜', '감독': '최동훈'},
    {'제목': '이프 온리', '감독': '길 정거'},
    {'제목': '캐스트 어웨이', '감독': '로버트 저메키스'},
    {'제목': '러브레터', '감독': '이와이 슌지'},
    {'제목': '노팅 힐', '감독': '로저 미첼'},
    {'제목': '로미오와 줄리엣', '감독': '바즈 루어만'},
    {'제목': '말모이', '감독': '엄유나'},
    {'제목': '1987', '감독': '장준환'},
    {'제목': '늑대소년', '감독': '조성희'},

]

# 음악 리스트
music_list = [
    {'제목': 'Whiplash', '가수': '에스파'},
    {'제목': 'APT.', '가수': '로제'},
    {'제목': 'Mantra', '가수': '제니'},
    {'제목': 'How Sweet', '가수': '뉴진스'},
    {'제목': '첫 눈', '가수': 'EXO'},
    {'제목': 'HAPPY', '가수': '데이식스'},
    {'제목': 'Love wins all', '가수': '아이유'},
    {'제목': 'Darling', '가수': '걸스데이'},
    {'제목': '광화문에서', '가수': '규현'},
    {'제목': 'TMI', '가수': '그레이'},

    {'제목': '예쁘잖아', '가수': '기리보이'},
    {'제목': '재워', '가수': '데이먼스 이어'},
    {'제목': '괜찮아도 괜찮아', '가수': '도경수'},
    {'제목': '운명의 히로인', '가수': '디핵'},
    {'제목': 'Cosmic', '가수': '레드벨벳'},
    {'제목': '두 번째 고백', '가수': '비투비'},
    {'제목': '아니 근데 진짜', '가수': '루시'},
    {'제목': 'Yesterday', '가수': '박재범'},
    {'제목': '야생화', '가수': '박효신'},
    {'제목': '첫사랑', '가수': '백아'},

    {'제목': '백야', '가수': '짙은'},
    {'제목': '산책', '가수': '백예린'},
    {'제목': '솔직히 말해서', '가수': '버나드 박'},
    {'제목': '나만, 봄', '가수': '볼빨간 사춘기'},
    {'제목': '풍경', '가수': '뷔'},
    {'제목': '비누', '가수': '비비'},
    {'제목': '고맙다', '가수': '세븐틴'},
    {'제목': '라비앙로즈', '가수': '아이즈원'},
    {'제목': '저녁 하늘', '가수': '에일리'},
    {'제목': '혜성', '가수': '윤하'},

    {'제목': '한숨', '가수': '이하이'},
    {'제목': '나무', '가수': '카더가든'},
    {'제목': '너를 그리는 시간', '가수': '태연'},
    {'제목': 'EVERYDAY', '가수': '위너'},
    {'제목': '사람', '가수': '지코'},
    {'제목': '양화대교', '가수': '자이언티'},
    {'제목': 'Touch Love', '가수': '윤미래'},
    {'제목': '오르골', '가수': 'NCT DREAM'},
    {'제목': '맨정신', '가수': '빅뱅'},
    {'제목': '고민중독', '가수': 'QWER'},

    {'제목': 'Blank Space', '가수': 'Taylor Swift'},
    {'제목': 'LA on a Saturday Night', '가수': 'Heart & Colors'},
    {'제목': 'One Last Chance', '가수': 'Daughtry'},
    {'제목': 'get him back!', '가수': 'Olivia Rodrigo'},
    {'제목': 'Birthday', '가수': 'Anne-Marie'},
    {'제목': 'Let Her go', '가수': 'Passenger'},
    {'제목': 'Six Feet Under', '가수': 'Billie Eilish'},
    {'제목': 'Older', '가수': 'Sasha Sloan'},
    {'제목': 'Sorry', '가수': 'Justin Bieber'},
    {'제목': 'Superman', '가수': 'Reiley'},

    {'제목': 'Make It ti Christmas', '가수': 'Alessia Cara'},
    {'제목': 'Santa Tell Me', '가수': 'Ariana Grande'},
    {'제목': 'Copines', '가수': 'Aya Nakamura'},
    {'제목': 'Dangerously', '가수': 'Charlie Puth'},
    {'제목': 'A Thousand Years', '가수': 'Christina Perri'},
    {'제목': 'All I Want for Christmas Is You', '가수': 'Mariah Carey'},
    {'제목': 'Espresso', '가수': 'Sabrina Carpenter'},
    {'제목': 'Eine Kleine', '가수': '요네즈 켄시'},
    {'제목': 'Sukidakara', '가수': '유이카'},
    {'제목': 'Marigold', '가수': '아이묭'},

    {'제목': 'Dramaturgy', '가수': 'Eve'},
    {'제목': 'koi', '가수': '호시노 겐'},
    {'제목': 'Inferno', '가수': 'Mrs.Green Apple'},
    {'제목': 'Beautiful Fin', '가수': 'Spitz'},
    {'제목': 'PUPPET SHOW', '가수': 'XG'},
    {'제목': 'NEW LOOK', '가수': 'MISAMO'},
    {'제목': 'number one girl', '가수': '로제'},
    {'제목': 'Drowning', '가수': 'WOODZ'},
    {'제목': 'Igloo', '가수': 'KISS OF LIFE'},
    {'제목': '너와의 모든 지금', '가수': '재쓰비'},

    {'제목': '녹아내려요', '가수': '데이식스'},
    {'제목': 'Wishful Winter', '가수': 'NCT WISH'},
    {'제목': '어떻게 이별까지 사랑하겠어, 널 사랑하는 거지', '가수': '악뮤'},
    {'제목': 'MEOW', '가수': 'MEOVV'},
    {'제목': '네모네모', '가수': '최예나'},
    {'제목': 'Love 119', '가수': '라이즈'},
    {'제목': '소나기', '가수': '이클립스'},
    {'제목': 'Snowman', '가수': 'Sia'},
    {'제목': 'Supersonic', '가수': '프로미스나인'},
    {'제목': 'Magnetic', '가수': '아일릿'},

    {'제목': 'Gee', '가수': '소녀시대'},
    {'제목': '그때 헤어지면 돼', '가수': '로이킴'},
    {'제목': '빛나리', '가수': '펜타곤'},
    {'제목': '켜줘', '가수': '워너원'},
    {'제목': '별이 빛나는 밤', '가수': '마마무'},
    {'제목': 'Way Back Home', '가수': '숀'},
    {'제목': '애상', '가수': '쿨'},
    {'제목': '순정', '가수': '코요태'},
    {'제목': '실연', '가수': '코요태'},
    {'제목': '아틀란티스 소녀', '가수': '보아'},

    {'제목': 'YOU AND I', '가수': '박봄'},
    {'제목': '우아하게', '가수': '트와이스'},
    {'제목': 'LUV', '가수': '에이핑크'},
    {'제목': 'Bad Girl, Good Girl', '가수': '미쓰에이'},
    {'제목': '적당히', '가수': 'clo'},
    {'제목': '그래서 난 뭔데', '가수': '태리'},
    {'제목': 'LAST GIRL (feat. D-HACK)', '가수': '제이씨 유카'},
    {'제목': '김철수 씨 이야기', '가수': '허회경'},
    {'제목': '파도', '가수': '찬민'},
    {'제목': '거북이', '가수': '다비치'},

]

# 운세 리스트
fortune_telling_list = [
    '사랑의 큐피드가 나타날 수 있어요. 인맥관계가 넓은 친구에게 소개를 부탁해 보세요. 이상형에 가까운 사람과 인연이 맺어질 수 있습니다.',
    '원하는 대로 행동하세요. 고민을 하면 기회를 놓칠 수 있습니다. 승부운도 좋으니 스포츠 경기에 도전해도 좋습니다.',
    '무난히 자기 자신의 자리에 충실하세요. 앞으로 나설 필요 없습니다. 너무 열심히 하면 오히려 겉돌 우려가 있습니다.',
    '이기적인 말투로 인해 분위기가 나빠질 수 있어요. 주위와의 관계도 불편해질 것 같습니다. 상대의 사정도 고려해서 발언합시다.',
    '마음에 드는 사람에게서 호의를 느낄 것 같아요. 자신 있게 대하면 괜찮습니다. 단둘이 만날 약속도 잡아보도록 합시다. 행복한 시간이 될 수 있어요.',
    '씀씀이에 주의가 필요합니다. 돈을 활용하는 방법에 대해 배워보는 것을 추천드립니다.',
    '한 가지에 집중하는 것이 좋습니다. 이것저것 하다 보면 처음 기세는 좋더라도 오래가지 않습니다. 작아도 실현 가능한 목표를 하나씩 설정하세요.',
    '급하면 될 일도 잘 안됩니다. 초조함을 버리는 것이 중요합니다. 친구가 느리더라도 재촉하지 마세요.',
    '동료의 기대감으로 인해 부담을 가질 수 있어요. 허풍을 떨지 말고 있는 그대로의 모습을 보여줍시다.',
    '의사소통이 부족해서 실수를 많이 할 것 같아요. 모르는 것은 계속 물어봐야 합니다. 기억력이 좋아도 반드시 메모를 합시다.',

    '절호의 타이밍에 원하는 것을 얻을 수 있을 것 같아요. 생각보다 근처에서 구할 수 있습니다.',
    '기회를 잘 포착해야 합니다. 오후부터 운의 기운이 좋아질 수 있어요. 소중한 사람에게 저녁 7시 이후에 연락을 해보세요.',
    '열정적으로 움직이나 주변에서 인정해 주지 않을 수 있어요. 되도록 독단 진행은 피하는 게 좋습니다. 시간과 에너지 낭비로 끝날 것 같습니다.',
    '감정의 균형이 깨지기 쉽습니다. 하고 싶은 말을 참으면 몸에 해로워요. 우선 마음을 안정시킨 뒤 할 이야기를 전합시다.',
    '뜻에 따르지 않아도 꾹 참읍시다. 폭발하면 불리한 입장에 몰릴 뿐입니다. 포커페이스로 그냥 넘어가도록 하세요.',
    '몸에 힘든 일을 맡게 될 수 있어요. 무리함으로 인해 몸에 이상을 느낄 수 있습니다. 힘들면 도움을 요청합시다.',
    '도움을 주는 역할로 활약할 수 있는 날. 당신의 태도가 좋은 인상을 줘서 호감도가 오를 수 있습니다. 그것을 기회로 비즈니스 파트너로 발전할 수 있습니다.',
    '귀찮은 일에 휘말릴 것 같아요. 애매한 언행을 취하고 있는 것이 원인입니다. 의사표시는 확실하게 하세요.',
    '문제가 발생해 우왕좌왕하기 쉽습니다. 조급하면 오판을 할 수 있어요. 천천히 심호흡을 하고 마음을 가라앉힌 후에 행동합시다.',
    '인간관계에 대해 재검토할 타이밍입니다. 메리트가 느껴지지 않는다면 망설이지 말고 관계를 끊으세요.',

    '감정적인 행동에 주의하세요. 표정에서 기분이 나타나기 때문에 주위에서 거리를 둘 수 있습니다. 좋아하는 음악을 듣고 기분전환을 해봅시다.',
    '좋은 정보를 얻을 수 있습니다. 사소한 대화도 놓치지 않도록 하세요. 궁금한 내용은 메모로 남겨 둡시다.',
    '자신의 의견을 강요하지 마세요. 반감을 살 뿐만 아니라 불필요한 적을 만들 수 있습니다. 무엇이든 받아들이는 자세가 중요합니다.',
    '장애물에 부딪히는 등 생각대로 일이 풀리지 않을 수 있습니다. 막히면 기분전환을 하세요. 머리가 맑아지고 해결책이 보일 수 있습니다.',
    '깊게 생각하지 말고 마음을 그대로 전달하는 것이 중요합니다. 싫은 일이나 짜증 나는 일이야말로 솔직하게 말하세요.',
    '지출이 증가할 수 있어요. 저렴한 가격에 이끌려 불필요한 물건을 사게 될 수 있습니다. 필요한 만큼만 구매합시다.',
    '일정 변경 등 복잡한 일이 생길 수 있어요. 잘되지 않아도 멘탈을 잘 챙기는 것이 좋습니다. 과감한 결단이 운의 흐름을 좋게 만들어 줄 것.',
    '몸 전체에 에너지가 충만함을 느낄 수 있어요. 발걸음도 가볍게 뛰어다닐 수 있습니다. 처음 방문하는 장소에서 좋은 일이 있을 것.',
    '너무 바빠서 마음의 여유가 없어질 수 있어요. 동료에게도 배려 없는 말을 하기 쉽습니다. 미안하면 바로 사과하세요.',
    '컨디션이 나쁠 수 있어요. 그냥 넘기면 더욱 문제가 커질 수 있습니다. 이상을 느끼면 빨리 치료를 받아야 합니다.',

]

# 화난 감정 리스트
emotion_anger_list = [
    '화날 만한 일이네요. 충분히 그렇게 느낄 수 있을 것 같아요.',
    '그런 일이 있다니 정말 속상하셨겠어요.',
    '그건 정말 화나는 상황이네요. 어떻게 도와드릴 수 있을까요?',
]

# 지루한 감정 리스트
emotion_boredom_list = [
    '뭔가 새로운 일이 생기면 좋겠죠? 함께 재미있는 걸 찾아볼까요?',
    '지루함을 달래는 방법을 같이 생각해 볼까요?',
    '새로운 도전이나 활동을 시작해 보면 어떨까요? 재미있을 거예요!',
]

# 기쁜 감정 리스트
emotion_joy_list = [
    '정말 멋진 소식이네요! 저도 기뻐요!',
    '축하드려요! 정말 기쁘셨겠어요!',
    '좋은 일이 있었군요! 계속 이런 기쁜 순간이 가득하길 바랄게요!',
]

# 슬픈 감정 리스트
emotion_sadness_list = [
    '정말 힘들겠어요. 제가 조금이라도 위로가 될 수 있으면 좋겠어요.',
    '그런 일이 있었다니 마음이 아프네요. 힘내세요.',
    '속상하시겠어요. 제가 도울 수 있는 게 있으면 말해주세요.',
]
