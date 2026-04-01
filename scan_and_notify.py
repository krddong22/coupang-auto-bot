import os
import time
import requests
from datetime import datetime

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID   = os.environ["TELEGRAM_CHAT_ID"]

PROXIES = [
    "https://api.allorigins.win/raw?url={}",
    "https://corsproxy.io/?{}",
    "https://api.codetabs.com/v1/proxy?quest={}",
]

KOSPI200_LIST = [
    {"code": "005930.KS", "name": "삼성전자"},
    {"code": "000660.KS", "name": "SK하이닉스"},
    {"code": "005380.KS", "name": "현대차"},
    {"code": "373220.KS", "name": "LG에너지솔루션"},
    {"code": "402340.KS", "name": "SK스퀘어"},
    {"code": "207940.KS", "name": "삼성바이오로직스"},
    {"code": "000270.KS", "name": "기아"},
    {"code": "034020.KS", "name": "두산에너빌리티"},
    {"code": "012450.KS", "name": "한화에어로스페이스"},
    {"code": "329180.KS", "name": "HD현대중공업"},
    {"code": "105560.KS", "name": "KB금융"},
    {"code": "028260.KS", "name": "삼성물산"},
    {"code": "068270.KS", "name": "셀트리온"},
    {"code": "055550.KS", "name": "신한지주"},
    {"code": "032830.KS", "name": "삼성생명"},
    {"code": "042660.KS", "name": "한화오션"},
    {"code": "012330.KS", "name": "현대모비스"},
    {"code": "015760.KS", "name": "한국전력"},
    {"code": "035420.KS", "name": "NAVER"},
    {"code": "010130.KS", "name": "고려아연"},
    {"code": "267260.KS", "name": "HD현대일렉트릭"},
    {"code": "006800.KS", "name": "미래에셋증권"},
    {"code": "086790.KS", "name": "하나금융지주"},
    {"code": "006400.KS", "name": "삼성SDI"},
    {"code": "009150.KS", "name": "삼성전기"},
    {"code": "005490.KS", "name": "POSCO홀딩스"},
    {"code": "009540.KS", "name": "HD한국조선해양"},
    {"code": "316140.KS", "name": "우리금융지주"},
    {"code": "034730.KS", "name": "SK"},
    {"code": "000810.KS", "name": "삼성화재"},
    {"code": "035720.KS", "name": "카카오"},
    {"code": "298040.KS", "name": "효성중공업"},
    {"code": "010140.KS", "name": "삼성중공업"},
    {"code": "051910.KS", "name": "LG화학"},
    {"code": "064350.KS", "name": "현대로템"},
    {"code": "138040.KS", "name": "메리츠금융지주"},
    {"code": "096770.KS", "name": "SK이노베이션"},
    {"code": "267250.KS", "name": "HD현대"},
    {"code": "010120.KS", "name": "LS ELECTRIC"},
    {"code": "066570.KS", "name": "LG전자"},
    {"code": "011200.KS", "name": "HMM"},
    {"code": "003670.KS", "name": "포스코퓨처엠"},
    {"code": "024110.KS", "name": "기업은행"},
    {"code": "272210.KS", "name": "한화시스템"},
    {"code": "086280.KS", "name": "현대글로비스"},
    {"code": "033780.KS", "name": "KT&G"},
    {"code": "042700.KS", "name": "한미반도체"},
    {"code": "047810.KS", "name": "한국항공우주"},
    {"code": "000150.KS", "name": "두산"},
    {"code": "017670.KS", "name": "SK텔레콤"},
    {"code": "352820.KS", "name": "하이브"},
    {"code": "030200.KS", "name": "KT"},
    {"code": "000720.KS", "name": "현대건설"},
    {"code": "003550.KS", "name": "LG"},
    {"code": "071050.KS", "name": "한국금융지주"},
    {"code": "323410.KS", "name": "카카오뱅크"},
    {"code": "018260.KS", "name": "삼성에스디에스"},
    {"code": "005830.KS", "name": "DB손해보험"},
    {"code": "005940.KS", "name": "NH투자증권"},
    {"code": "047050.KS", "name": "포스코인터내셔널"},
    {"code": "010950.KS", "name": "S-Oil"},
    {"code": "039490.KS", "name": "키움증권"},
    {"code": "259960.KS", "name": "크래프톤"},
    {"code": "307950.KS", "name": "현대오토에버"},
    {"code": "278470.KS", "name": "에이피알"},
    {"code": "079550.KS", "name": "LIG넥스원"},
    {"code": "180640.KS", "name": "한진칼"},
    {"code": "003490.KS", "name": "대한항공"},
    {"code": "000880.KS", "name": "한화"},
    {"code": "161390.KS", "name": "한국타이어앤테크놀로지"},
    {"code": "016360.KS", "name": "삼성증권"},
    {"code": "003230.KS", "name": "삼양식품"},
    {"code": "326030.KS", "name": "SK바이오팜"},
    {"code": "090430.KS", "name": "아모레퍼시픽"},
    {"code": "006260.KS", "name": "LS"},
    {"code": "000100.KS", "name": "유한양행"},
    {"code": "377300.KS", "name": "카카오페이"},
    {"code": "009830.KS", "name": "한화솔루션"},
    {"code": "128940.KS", "name": "한미약품"},
    {"code": "007660.KS", "name": "이수페타시스"},
    {"code": "443060.KS", "name": "HD현대마린솔루션"},
    {"code": "032640.KS", "name": "LG유플러스"},
    {"code": "028050.KS", "name": "삼성E&A"},
    {"code": "034220.KS", "name": "LG디스플레이"},
    {"code": "029780.KS", "name": "삼성카드"},
    {"code": "064400.KS", "name": "LG씨엔에스"},
    {"code": "078930.KS", "name": "GS"},
    {"code": "011070.KS", "name": "LG이노텍"},
    {"code": "454910.KS", "name": "두산로보틱스"},
    {"code": "138930.KS", "name": "BNK금융지주"},
    {"code": "052690.KS", "name": "한전기술"},
    {"code": "175330.KS", "name": "JB금융지주"},
    {"code": "021240.KS", "name": "코웨이"},
    {"code": "001040.KS", "name": "CJ"},
    {"code": "001440.KS", "name": "대한전선"},
    {"code": "241560.KS", "name": "두산밥캣"},
    {"code": "022100.KS", "name": "포스코DX"},
    {"code": "062040.KS", "name": "산일전기"},
    {"code": "002380.KS", "name": "KCC"},
    {"code": "271560.KS", "name": "오리온"},
    {"code": "066970.KS", "name": "엘앤에프"},
    {"code": "251270.KS", "name": "넷마블"},
    {"code": "036570.KS", "name": "엔씨소프트"},
    {"code": "004020.KS", "name": "현대제철"},
    {"code": "450080.KS", "name": "에코프로머티"},
    {"code": "082740.KS", "name": "한화엔진"},
    {"code": "018880.KS", "name": "한온시스템"},
    {"code": "017800.KS", "name": "현대엘리베이터"},
    {"code": "088350.KS", "name": "한화생명"},
    {"code": "051900.KS", "name": "LG생활건강"},
    {"code": "111770.KS", "name": "영원무역"},
    {"code": "302440.KS", "name": "SK바이오사이언스"},
    {"code": "004990.KS", "name": "롯데지주"},
    {"code": "036460.KS", "name": "한국가스공사"},
    {"code": "011780.KS", "name": "금호석유화학"},
    {"code": "011790.KS", "name": "SKC"},
    {"code": "035250.KS", "name": "강원랜드"},
    {"code": "011170.KS", "name": "롯데케미칼"},
    {"code": "004170.KS", "name": "신세계"},
    {"code": "014680.KS", "name": "한솔케미칼"},
    {"code": "012750.KS", "name": "에스원"},
    {"code": "008930.KS", "name": "한미사이언스"},
    {"code": "000120.KS", "name": "CJ대한통운"},
    {"code": "000240.KS", "name": "한국앤컴퍼니"},
    {"code": "001450.KS", "name": "현대해상"},
    {"code": "009420.KS", "name": "한올바이오파마"},
    {"code": "009970.KS", "name": "영원무역홀딩스"},
    {"code": "023530.KS", "name": "롯데쇼핑"},
    {"code": "047040.KS", "name": "대우건설"},
    {"code": "071970.KS", "name": "HD현대마린엔진"},
    {"code": "097950.KS", "name": "CJ제일제당"},
    {"code": "103140.KS", "name": "풍산"},
    {"code": "139130.KS", "name": "iM금융지주"},
    {"code": "139480.KS", "name": "이마트"},
    {"code": "457190.KS", "name": "이수스페셜티케미컬"},
    {"code": "026960.KS", "name": "동서"},
    {"code": "004370.KS", "name": "농심"},
    {"code": "005850.KS", "name": "에스엘"},
    {"code": "028670.KS", "name": "팬오션"},
    {"code": "030000.KS", "name": "제일기획"},
    {"code": "001430.KS", "name": "세아베스틸지주"},
    {"code": "204320.KS", "name": "HL만도"},
    {"code": "051600.KS", "name": "한전KPS"},
    {"code": "002790.KS", "name": "아모레퍼시픽홀딩스"},
    {"code": "010060.KS", "name": "OCI홀딩스"},
    {"code": "383220.KS", "name": "F&F"},
    {"code": "006280.KS", "name": "녹십자"},
    {"code": "112610.KS", "name": "씨에스윈드"},
    {"code": "282330.KS", "name": "BGF리테일"},
    {"code": "069960.KS", "name": "현대백화점"},
    {"code": "073240.KS", "name": "금호타이어"},
    {"code": "192820.KS", "name": "코스맥스"},
    {"code": "011210.KS", "name": "현대위아"},
    {"code": "069620.KS", "name": "대웅제약"},
    {"code": "008770.KS", "name": "호텔신라"},
    {"code": "375500.KS", "name": "DL이앤씨"},
    {"code": "007310.KS", "name": "오뚜기"},
    {"code": "006360.KS", "name": "GS건설"},
    {"code": "006040.KS", "name": "동원산업"},
    {"code": "120110.KS", "name": "코오롱인더"},
    {"code": "161890.KS", "name": "한국콜마"},
    {"code": "298020.KS", "name": "효성티앤씨"},
    {"code": "007070.KS", "name": "GS리테일"},
    {"code": "003090.KS", "name": "대웅"},
    {"code": "034230.KS", "name": "파라다이스"},
    {"code": "005300.KS", "name": "롯데칠성"},
    {"code": "137310.KS", "name": "에스디바이오센서"},
    {"code": "000080.KS", "name": "하이트진로"},
    {"code": "185750.KS", "name": "종근당"},
    {"code": "009240.KS", "name": "한샘"},
    {"code": "004000.KS", "name": "롯데정밀화학"},
    {"code": "280360.KS", "name": "롯데웰푸드"},
    {"code": "006650.KS", "name": "대한유화"},
    {"code": "192080.KS", "name": "더블유게임즈"},
    {"code": "285130.KS", "name": "SK케미칼"},
    {"code": "114090.KS", "name": "GKL"},
    {"code": "093370.KS", "name": "후성"},
    {"code": "071320.KS", "name": "지역난방공사"},
    {"code": "014820.KS", "name": "동원시스템즈"},
    {"code": "005420.KS", "name": "코스모화학"},
    {"code": "005250.KS", "name": "녹십자홀딩스"},
    {"code": "004490.KS", "name": "세방전지"},
    {"code": "001680.KS", "name": "대상"},
    {"code": "000210.KS", "name": "DL"},
    {"code": "002030.KS", "name": "아세아"},
    {"code": "003030.KS", "name": "세아제강지주"},
]

KOSDAQ150_LIST = [
    {"code": "086520.KQ", "name": "에코프로"},
    {"code": "196170.KQ", "name": "알테오젠"},
    {"code": "247540.KQ", "name": "에코프로비엠"},
    {"code": "000250.KQ", "name": "삼천당제약"},
    {"code": "277810.KQ", "name": "레인보우로보틱스"},
    {"code": "298380.KQ", "name": "에이비엘바이오"},
    {"code": "058470.KQ", "name": "리노공업"},
    {"code": "214370.KQ", "name": "케어젠"},
    {"code": "028300.KQ", "name": "HLB"},
    {"code": "141080.KQ", "name": "리가켐바이오"},
    {"code": "087010.KQ", "name": "펩트론"},
    {"code": "240810.KQ", "name": "원익IPS"},
    {"code": "310210.KQ", "name": "보로노이"},
    {"code": "039030.KQ", "name": "이오테크닉스"},
    {"code": "214150.KQ", "name": "클래시스"},
    {"code": "108490.KQ", "name": "로보티즈"},
    {"code": "140410.KQ", "name": "메지온"},
    {"code": "095340.KQ", "name": "ISC"},
    {"code": "214450.KQ", "name": "파마리서치"},
    {"code": "403870.KQ", "name": "HPSP"},
    {"code": "068760.KQ", "name": "셀트리온제약"},
    {"code": "145020.KQ", "name": "휴젤"},
    {"code": "263750.KQ", "name": "펄어비스"},
    {"code": "357780.KQ", "name": "솔브레인"},
    {"code": "237690.KQ", "name": "에스티팜"},
    {"code": "084370.KQ", "name": "유진테크"},
    {"code": "005290.KQ", "name": "동진쎄미켐"},
    {"code": "257720.KQ", "name": "실리콘투"},
    {"code": "041510.KQ", "name": "에스엠"},
    {"code": "036930.KQ", "name": "주성엔지니어링"},
    {"code": "035900.KQ", "name": "JYP Ent."},
    {"code": "064760.KQ", "name": "티씨케이"},
    {"code": "067310.KQ", "name": "하나마이크론"},
    {"code": "098460.KQ", "name": "고영"},
    {"code": "178320.KQ", "name": "서진시스템"},
    {"code": "039200.KQ", "name": "오스코텍"},
    {"code": "065350.KQ", "name": "신성델타테크"},
    {"code": "222800.KQ", "name": "심텍"},
    {"code": "085660.KQ", "name": "차바이오텍"},
    {"code": "101490.KQ", "name": "에스앤에스텍"},
    {"code": "048410.KQ", "name": "현대바이오"},
    {"code": "140860.KQ", "name": "파크시스템스"},
    {"code": "319660.KQ", "name": "피에스케이"},
    {"code": "089030.KQ", "name": "테크윙"},
    {"code": "195940.KQ", "name": "HK이노엔"},
    {"code": "035760.KQ", "name": "CJ ENM"},
    {"code": "096530.KQ", "name": "씨젠"},
    {"code": "095610.KQ", "name": "테스"},
    {"code": "122870.KQ", "name": "와이지엔터테인먼트"},
    {"code": "253450.KQ", "name": "스튜디오드래곤"},
    {"code": "293490.KQ", "name": "카카오게임즈"},
    {"code": "137400.KQ", "name": "피엔티"},
    {"code": "131970.KQ", "name": "두산테스나"},
    {"code": "328130.KQ", "name": "루닛"},
    {"code": "166090.KQ", "name": "하나머티리얼즈"},
    {"code": "056190.KQ", "name": "에스에프에이"},
    {"code": "183300.KQ", "name": "코미코"},
    {"code": "189300.KQ", "name": "인텔리안테크"},
    {"code": "213420.KQ", "name": "덕산네오룩스"},
    {"code": "131290.KQ", "name": "티에스이"},
    {"code": "086450.KQ", "name": "동국제약"},
    {"code": "086900.KQ", "name": "메디톡스"},
    {"code": "033500.KQ", "name": "동성화인텍"},
    {"code": "112040.KQ", "name": "위메이드"},
    {"code": "033100.KQ", "name": "제룡전기"},
    {"code": "241710.KQ", "name": "코스메카코리아"},
    {"code": "121600.KQ", "name": "나노신소재"},
    {"code": "046890.KQ", "name": "서울반도체"},
    {"code": "079370.KQ", "name": "제우스"},
    {"code": "095660.KQ", "name": "네오위즈"},
    {"code": "025900.KQ", "name": "동화기업"},
    {"code": "215200.KQ", "name": "메가스터디교육"},
    {"code": "050890.KQ", "name": "쏠리드"},
    {"code": "053030.KQ", "name": "바이넥스"},
    {"code": "069080.KQ", "name": "웹젠"},
    {"code": "200130.KQ", "name": "콜마비앤에이치"},
    {"code": "352480.KQ", "name": "씨앤씨인터내셔널"},
    {"code": "078340.KQ", "name": "컴투스"},
    {"code": "215000.KQ", "name": "골프존"},
    {"code": "108860.KQ", "name": "셀바스AI"},
]


def fetch_yahoo(code, interval, range_):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{code}?interval={interval}&range={range_}"
    for proxy_tpl in PROXIES:
        try:
            proxy_url = proxy_tpl.format(requests.utils.quote(url, safe=''))
            res = requests.get(proxy_url, timeout=15)
            if not res.ok:
                continue
            data = res.json()
            if data.get("chart", {}).get("result"):
                return data
        except Exception:
            continue
    return None


def check_v2(stock, months=6, min_ago=1, max_ago=3, ma_period=10, min_gap=5.0, max_gap=100.0):
    daily_data = fetch_yahoo(stock["code"], "1d", "2y")
    if not daily_data:
        return False

    month_data = fetch_yahoo(stock["code"], "1mo", "15y")
    if not month_data:
        return False

    chart = daily_data["chart"]["result"][0]
    timestamps = chart.get("timestamp", [])
    quotes = chart["indicators"]["quote"][0]
    if not quotes.get("volume") or not quotes.get("close"):
        return False

    from datetime import datetime, timezone
    now = datetime.now()
    this_year = now.year
    this_month = now.month - 1  # Python month is 0-indexed like JS

    # cutoff
    import calendar
    cutoff_month = this_month - months
    cutoff_year = this_year
    while cutoff_month < 0:
        cutoff_month += 12
        cutoff_year -= 1
    cutoff_ts = datetime(cutoff_year, cutoff_month + 1, 1).timestamp()

    # validKeys
    valid_keys = set()
    for ago in range(min_ago, max_ago + 1):
        m = this_month - ago
        y = this_year
        while m < 0:
            m += 12
            y -= 1
        valid_keys.add(f"{y}-{m}")

    # monthly volume
    monthly_vol = {}
    for i, ts in enumerate(timestamps):
        if ts < cutoff_ts:
            continue
        d = datetime.fromtimestamp(ts)
        yr, mo = d.year, d.month - 1
        if yr == this_year and mo == this_month:
            continue
        key = f"{yr}-{mo}"
        monthly_vol[key] = monthly_vol.get(key, 0) + (quotes["volume"][i] or 0)

    if len(monthly_vol) < 2:
        return False

    max_vol = max(monthly_vol.values())
    top_key = next(k for k, v in monthly_vol.items() if v == max_vol)
    if top_key not in valid_keys:
        return False

    # 양봉 조건
    top_yr, top_mo = int(top_key.split("-")[0]), int(top_key.split("-")[1])
    opens = quotes.get("open", [])
    closes = quotes.get("close", [])
    top_opens, top_closes = [], []
    for i, ts in enumerate(timestamps):
        d = datetime.fromtimestamp(ts)
        if d.year == top_yr and d.month - 1 == top_mo:
            if opens[i] is not None:
                top_opens.append(opens[i])
            if closes[i] is not None:
                top_closes.append(closes[i])
    if not top_opens or not top_closes:
        return False
    if top_closes[-1] <= top_opens[0]:
        return False

    # MA 괴리율 조건
    m_chart = month_data["chart"]["result"][0]
    m_quotes = m_chart["indicators"]["quote"][0]
    month_closes = [v for v in (m_quotes.get("close") or []) if v is not None]
    if len(month_closes) < ma_period:
        return False

    ma = sum(month_closes[-ma_period:]) / ma_period
    current = month_closes[-1]
    gap = (current - ma) / ma * 100
    if gap < min_gap or gap > max_gap:
        return False

    return True


def check_v3(stock, months=6, min_ago=1, max_ago=3, ma_period=10, min_gap=5.0, max_gap=100.0):
    daily_data = fetch_yahoo(stock["code"], "1d", "2y")
    if not daily_data:
        return False

    month_data = fetch_yahoo(stock["code"], "1mo", "15y")
    if not month_data:
        return False

    chart = daily_data["chart"]["result"][0]
    timestamps = chart.get("timestamp", [])
    quotes = chart["indicators"]["quote"][0]
    if not quotes.get("volume") or not quotes.get("close"):
        return False

    from datetime import datetime
    now = datetime.now()
    this_year = now.year
    this_month = now.month - 1

    cutoff_month = this_month - months
    cutoff_year = this_year
    while cutoff_month < 0:
        cutoff_month += 12
        cutoff_year -= 1
    cutoff_ts = datetime(cutoff_year, cutoff_month + 1, 1).timestamp()

    valid_keys = set()
    for ago in range(min_ago, max_ago + 1):
        m = this_month - ago
        y = this_year
        while m < 0:
            m += 12
            y -= 1
        valid_keys.add(f"{y}-{m}")

    monthly_vol = {}
    for i, ts in enumerate(timestamps):
        if ts < cutoff_ts:
            continue
        d = datetime.fromtimestamp(ts)
        yr, mo = d.year, d.month - 1
        if yr == this_year and mo == this_month:
            continue
        key = f"{yr}-{mo}"
        monthly_vol[key] = monthly_vol.get(key, 0) + (quotes["volume"][i] or 0)

    if len(monthly_vol) < 2:
        return False

    max_vol = max(monthly_vol.values())
    top_key = next(k for k, v in monthly_vol.items() if v == max_vol)
    if top_key not in valid_keys:
        return False

    top_yr, top_mo = int(top_key.split("-")[0]), int(top_key.split("-")[1])
    opens = quotes.get("open", [])
    closes_daily = quotes.get("close", [])
    highs = quotes.get("high", [])
    top_opens, top_closes, top_highs = [], [], []
    for i, ts in enumerate(timestamps):
        d = datetime.fromtimestamp(ts)
        if d.year == top_yr and d.month - 1 == top_mo:
            if opens[i] is not None:
                top_opens.append(opens[i])
            if closes_daily[i] is not None:
                top_closes.append(closes_daily[i])
            if highs[i] is not None:
                top_highs.append(highs[i])
    if not top_opens or not top_closes or not top_highs:
        return False

    # 양봉 조건
    if top_closes[-1] <= top_opens[0]:
        return False

    # 월봉 MA 계산
    m_chart = month_data["chart"]["result"][0]
    m_quotes = m_chart["indicators"]["quote"][0]
    month_closes = [v for v in (m_quotes.get("close") or []) if v is not None]

    if len(month_closes) < 120:
        return False

    ma60 = sum(month_closes[-60:]) / 60
    ma120 = sum(month_closes[-120:]) / 120

    # MA120 > MA60 조건
    if ma120 <= ma60:
        return False

    # 거래량 터진 달 고가가 MA60 아래인지 체크 (월봉 데이터 기준)
    m_timestamps = m_chart.get("timestamp", [])
    m_highs = m_quotes.get("high", [])
    top_month_high = None
    for i, ts in enumerate(m_timestamps):
        d = datetime.fromtimestamp(ts)
        if d.year == top_yr and d.month - 1 == top_mo:
            if m_highs[i] is not None:
                top_month_high = m_highs[i]
            break
    if top_month_high is None:
        return False
    if top_month_high >= ma60:
        return False

    # MA 괴리율 조건
    if len(month_closes) < ma_period:
        return False
    ma = sum(month_closes[-ma_period:]) / ma_period
    current = month_closes[-1]
    gap = (current - ma) / ma * 100
    if gap < min_gap or gap > max_gap:
        return False

    return True


def send_telegram(message):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    )


def run_scan(scan_func, label, stock_list, delay=1.5, **kwargs):
    kospi_pass, kosdaq_pass = [], []
    for stock in stock_list:
        try:
            result = scan_func(stock, **kwargs)
            if result:
                market = "KOSPI" if stock["code"].endswith(".KS") else "KOSDAQ"
                clean_code = stock["code"].replace(".KS", "").replace(".KQ", "")
                if market == "KOSPI":
                    kospi_pass.append(f"- {clean_code} {stock['name']}")
                else:
                    kosdaq_pass.append(f"- {clean_code} {stock['name']}")
        except Exception as e:
            print(f"[ERROR] {stock['name']}: {e}")
        time.sleep(delay)
    return kospi_pass, kosdaq_pass


def build_message(label, kospi_list, kosdaq_list, date_str):
    kospi_str = "\n".join(kospi_list) if kospi_list else "- 해당 종목 없음"
    kosdaq_str = "\n".join(kosdaq_list) if kosdaq_list else "- 해당 종목 없음"
    return (
        f"📊 <b>[{label}] {date_str} 스캔 결과</b>\n\n"
        f"🟢 <b>KOSPI200 ({len(kospi_list)}개)</b>\n{kospi_str}\n\n"
        f"🟡 <b>KOSDAQ150 ({len(kosdaq_list)}개)</b>\n{kosdaq_str}"
    )


if __name__ == "__main__":
    today = datetime.now().strftime("%Y년 %m월 %d일")
    all_stocks = KOSPI200_LIST + KOSDAQ150_LIST

    print("=== v2 스캔 시작 ===")
    v2_kospi, v2_kosdaq = run_scan(
        check_v2, "v2 범위설정형", all_stocks,
        months=6, min_ago=1, max_ago=3,
        ma_period=10, min_gap=5.0, max_gap=100.0
    )
    v2_msg = build_message("v2 범위설정형", v2_kospi, v2_kosdaq, today)
    send_telegram(v2_msg)
    print("v2 메시지 전송 완료")

    time.sleep(3)

    print("=== v3 스캔 시작 ===")
    v3_kospi, v3_kosdaq = run_scan(
        check_v3, "v3 MA추세 필터형", all_stocks,
        months=6, min_ago=1, max_ago=3,
        ma_period=10, min_gap=5.0, max_gap=100.0
    )
    v3_msg = build_message("v3 MA추세 필터형", v3_kospi, v3_kosdaq, today)
    send_telegram(v3_msg)
    print("v3 메시지 전송 완료")
