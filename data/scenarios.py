"""
AI CRACKER
가상 금융 거래 시나리오 데이터

주의:
실제 고객 데이터가 아닌 MVP 데모용 가상 데이터만 사용한다.
"""


# ==================================================
# Scenario Data
# ==================================================

SCENARIOS = {
    "institution_impersonation": {
        "name": "기관 사칭 보이스피싱",
        "description": "검찰·금융기관 등을 사칭하여 송금을 유도하는 상황",

        "recipient_name": "안전계좌",
        "recipient_account": "900-123-456789",

        "amount": 3_500_000,
        "avg_transaction_amount": 650_000,

        "is_new_recipient": True,
        "recent_loan": True,
        "transaction_count_24h": 2,

        "transaction_time": "02:13",
        "device_change": True,

        "previous_transaction_count": 14,
    },

    "investment_fraud": {
        "name": "투자 사기",
        "description": "고수익 투자 등을 이유로 송금을 유도하는 상황",

        "recipient_name": "AI 투자센터",
        "recipient_account": "910-234-567890",

        "amount": 5_000_000,
        "avg_transaction_amount": 700_000,

        "is_new_recipient": True,
        "recent_loan": False,
        "transaction_count_24h": 1,

        "transaction_time": "21:35",
        "device_change": False,

        "previous_transaction_count": 8,
    },

    "family_impersonation": {
        "name": "가족·지인 사칭",
        "description": "가족이나 지인을 사칭하여 긴급 송금을 요구하는 상황",

        "recipient_name": "김민수",
        "recipient_account": "920-345-678901",

        "amount": 2_000_000,
        "avg_transaction_amount": 500_000,

        "is_new_recipient": True,
        "recent_loan": False,
        "transaction_count_24h": 4,

        "transaction_time": "23:48",
        "device_change": False,

        "previous_transaction_count": 20,
    },
}


# ==================================================
# Scenario Helper
# ==================================================

def get_scenario(scenario_id: str) -> dict:
    """
    시나리오 ID를 받아 가상 거래 데이터를 반환한다.
    """

    if scenario_id not in SCENARIOS:
        raise ValueError(f"존재하지 않는 시나리오입니다: {scenario_id}")

    # 원본 데이터가 수정되지 않도록 복사해서 반환
    return SCENARIOS[scenario_id].copy()


def get_all_scenarios() -> dict:
    """
    전체 시나리오를 반환한다.
    """

    return {
        scenario_id: scenario.copy()
        for scenario_id, scenario in SCENARIOS.items()
    }