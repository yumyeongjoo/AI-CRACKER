"""
AI CRACKER
Transaction Risk Model

규칙 기반 거래 위험 점수 모델.
실제 금융 데이터가 아닌 MVP용 가상 거래 데이터를 사용한다.
"""


# ==================================================
# Risk Rules
# ==================================================

RISK_RULES = {
    "new_recipient": 20,
    "high_amount": 25,
    "recent_loan": 20,
    "repeated_transaction": 15,
    "device_change": 10,
    "abnormal_time": 10,
}


# ==================================================
# Helper Functions
# ==================================================

def is_high_amount(
    amount: int,
    avg_transaction_amount: int,
) -> bool:
    """
    현재 송금액이 평소 거래액의 2배 이상인지 판단한다.
    """

    if avg_transaction_amount <= 0:
        return False

    return amount >= avg_transaction_amount * 2


def is_abnormal_time(transaction_time: str) -> bool:
    """
    거래 시간이 비정상 시간대인지 판단한다.

    MVP에서는 23:00 ~ 06:00을 비정상 시간대로 정의한다.
    """

    hour = int(transaction_time.split(":")[0])

    return hour >= 23 or hour < 6


def get_risk_level(score: int) -> str:
    """
    위험 점수를 위험 등급으로 변환한다.
    """

    if score >= 80:
        return "CRITICAL"

    if score >= 60:
        return "HIGH"

    if score >= 30:
        return "MODERATE"

    return "LOW"


# ==================================================
# Main Risk Calculation
# ==================================================

def calculate_transaction_risk(transaction: dict) -> dict:
    """
    거래 데이터를 받아 Transaction Risk Score를 계산한다.

    반환값:

    {
        "score": 75,
        "level": "HIGH",
        "signals": [
            {
                "name": "신규 수취인",
                "score": 20
            }
        ]
    }
    """

    score = 0
    signals = []

    # --------------------------------------------------
    # 1. 신규 수취인
    # --------------------------------------------------

    if transaction.get("is_new_recipient", False):

        points = RISK_RULES["new_recipient"]

        score += points

        signals.append(
            {
                "name": "신규 수취인",
                "score": points,
                "description": "최근 거래 이력이 없는 수취인입니다.",
            }
        )

    # --------------------------------------------------
    # 2. 평소보다 높은 금액
    # --------------------------------------------------

    if is_high_amount(
        transaction.get("amount", 0),
        transaction.get("avg_transaction_amount", 0),
    ):

        points = RISK_RULES["high_amount"]

        score += points

        signals.append(
            {
                "name": "평소보다 높은 송금액",
                "score": points,
                "description": "평소 거래 금액보다 크게 높은 금액입니다.",
            }
        )

    # --------------------------------------------------
    # 3. 최근 대출
    # --------------------------------------------------

    if transaction.get("recent_loan", False):

        points = RISK_RULES["recent_loan"]

        score += points

        signals.append(
            {
                "name": "최근 대출",
                "score": points,
                "description": "최근 대출 거래가 확인된 상태입니다.",
            }
        )

    # --------------------------------------------------
    # 4. 단시간 반복 거래
    # --------------------------------------------------

    if transaction.get("transaction_count_24h", 0) >= 3:

        points = RISK_RULES["repeated_transaction"]

        score += points

        signals.append(
            {
                "name": "단시간 반복 송금",
                "score": points,
                "description": "최근 24시간 동안 반복적인 거래가 발생했습니다.",
            }
        )

    # --------------------------------------------------
    # 5. 새로운 기기
    # --------------------------------------------------

    if transaction.get("device_change", False):

        points = RISK_RULES["device_change"]

        score += points

        signals.append(
            {
                "name": "새로운 기기",
                "score": points,
                "description": "평소와 다른 기기에서 거래가 발생했습니다.",
            }
        )

    # --------------------------------------------------
    # 6. 비정상 시간대
    # --------------------------------------------------

    if is_abnormal_time(
        transaction.get("transaction_time", "12:00")
    ):

        points = RISK_RULES["abnormal_time"]

        score += points

        signals.append(
            {
                "name": "비정상 시간대",
                "score": points,
                "description": "일반적인 거래 시간대를 벗어난 거래입니다.",
            }
        )

    # --------------------------------------------------
    # Score Normalization
    # --------------------------------------------------

    score = min(score, 100)

    level = get_risk_level(score)

    return {
        "score": score,
        "level": level,
        "signals": signals,
    }