import streamlit as st

from config.settings import APP_NAME, APP_VERSION
from data.scenarios import get_scenario
from models.risk_model import calculate_transaction_risk


# ==================================================
# Page Configuration
# ==================================================

st.set_page_config(
    page_title="AI BANK",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ==================================================
# Custom CSS
# ==================================================

st.markdown(
    """
<style>
.stApp {
    background-color: #f5f6f8;
}

.block-container {
    max-width: 480px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.bank-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.bank-name {
    font-size: 1.5rem;
    font-weight: 700;
}

.notification {
    font-size: 1.3rem;
}

.greeting {
    font-size: 1rem;
    color: #555;
    margin-bottom: 0.3rem;
}

.username {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
}

.balance-card {
    background-color: white;
    border-radius: 18px;
    padding: 1.5rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
}

.balance-label {
    font-size: 0.9rem;
    color: #777;
    margin-bottom: 0.5rem;
}

.balance {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.account-number {
    font-size: 0.85rem;
    color: #888;
}

.transaction-card {
    background-color: white;
    border-radius: 18px;
    padding: 1.3rem;
    margin-top: 1rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
}

.transaction-title {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.transaction-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.8rem 0;
    border-bottom: 1px solid #eeeeee;
}

.transaction-row:last-child {
    border-bottom: none;
}

.transaction-name {
    font-size: 0.95rem;
}

.transaction-date {
    font-size: 0.75rem;
    color: #999;
    margin-top: 0.2rem;
}

.transaction-amount {
    font-weight: 600;
}

.positive {
    color: #1a8f4d;
}

.negative {
    color: #333;
}

.transfer-card {
    background-color: white;
    border-radius: 18px;
    padding: 1.5rem;
    margin-top: 1rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
}

.transfer-title {
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
}

.transfer-description {
    color: #777;
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
}

.transfer-summary {
    background-color: #f7f8fa;
    border-radius: 12px;
    padding: 1rem;
    margin-top: 1rem;
}

.summary-label {
    color: #777;
    font-size: 0.8rem;
}

.summary-value {
    font-size: 1rem;
    font-weight: 600;
    margin-top: 0.2rem;
}

.risk-card {
    background-color: white;
    border-radius: 18px;
    padding: 1.5rem;
    margin-top: 1rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
}

</style>
""",
    unsafe_allow_html=True,
)


# ==================================================
# Session State
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "transaction" not in st.session_state:
    st.session_state.transaction = None

if "risk_result" not in st.session_state:
    st.session_state.risk_result = None


# ==================================================
# Helper Functions
# ==================================================

def go_home():
    st.session_state.page = "home"


def go_transfer():
    st.session_state.page = "transfer"


# ==================================================
# Home Page
# ==================================================

def show_home():

    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    st.markdown(
        """
<div class="bank-header">
    <div class="bank-name">🏦 AI BANK</div>
    <div class="notification">🔔</div>
</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Greeting
    # --------------------------------------------------

    st.markdown(
        """
<div class="greeting">안녕하세요</div>
<div class="username">사용자님 👋</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Balance Card
    # --------------------------------------------------

    st.markdown(
        """
<div class="balance-card"><div class="balance-label">총 보유 잔액</div><div class="balance">₩12,580,000</div><div class="account-number">AI BANK · 123-456-789012</div></div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Quick Actions
    # --------------------------------------------------

    st.subheader("빠른 메뉴")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "💸 송금하기",
            use_container_width=True,
        ):
            go_transfer()
            st.rerun()

    with col2:
        if st.button(
            "📋 거래내역",
            use_container_width=True,
        ):
            st.info("거래내역 기능은 다음 단계에서 구현합니다.")

    # --------------------------------------------------
    # Recent Transactions
    # --------------------------------------------------

    st.markdown(
        """
<div class="transaction-card"><div class="transaction-title">최근 거래</div><div class="transaction-row"><div><div class="transaction-name">급여</div><div class="transaction-date">08.25</div></div><div class="transaction-amount positive">+₩2,500,000</div></div><div class="transaction-row"><div><div class="transaction-name">편의점</div><div class="transaction-date">08.28</div></div><div class="transaction-amount negative">-₩8,500</div></div><div class="transaction-row"><div><div class="transaction-name">카페</div><div class="transaction-date">08.28</div></div><div class="transaction-amount negative">-₩6,000</div></div><div class="transaction-row"><div><div class="transaction-name">온라인 쇼핑</div><div class="transaction-date">08.29</div></div><div class="transaction-amount negative">-₩42,000</div></div></div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    st.divider()

    st.caption(f"{APP_NAME} MVP {APP_VERSION}")
    st.caption("Demo Environment · No Real Financial Data")


# ==================================================
# Transfer Page
# ==================================================

def show_transfer():

    # --------------------------------------------------
    # Back Button
    # --------------------------------------------------

    if st.button("← 홈으로"):
        go_home()
        st.rerun()

    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    st.markdown(
        """
<div class="transfer-card">
    <div class="transfer-title">송금하기</div>
    <div class="transfer-description">송금할 정보를 입력해주세요.</div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    # --------------------------------------------------
    # Transfer Form
    # --------------------------------------------------

    with st.form("transfer_form"):

        scenario_options = {
            "기관 사칭 보이스피싱": "institution_impersonation",
            "투자 사기": "investment_fraud",
            "가족·지인 사칭": "family_impersonation",
        }

        scenario_name = st.selectbox(
            "데모 시나리오",
            list(scenario_options.keys()),
        )

        scenario_id = scenario_options[scenario_name]

        recipient = st.selectbox(
            "수취인",
            [
                "김민수 · 123-456-789012",
                "박서연 · 234-567-890123",
                "이준호 · 345-678-901234",
            ],
        )

        amount = st.number_input(
            "송금 금액",
            min_value=0,
            max_value=12_580_000,
            value=0,
            step=10_000,
            format="%d",
        )

        purpose = st.selectbox(
            "송금 목적",
            [
                "생활비",
                "물품 구매",
                "가족·지인 송금",
                "투자",
                "대출 관련",
                "기타",
            ],
        )

        submitted = st.form_submit_button(
            "다음",
            use_container_width=True,
        )

    # --------------------------------------------------
    # Form Validation
    # --------------------------------------------------

    if submitted:

        if amount <= 0:

            st.error("송금 금액을 입력해주세요.")

        elif amount > 12_580_000:

            st.error("잔액보다 많은 금액을 송금할 수 없습니다.")

        else:

            recipient_name = recipient.split(" · ")[0]
            recipient_account = recipient.split(" · ")[1]

            scenario_data = get_scenario(scenario_id)

            # ------------------------------------------
            # Transaction Data
            # ------------------------------------------

            st.session_state.transaction = {
                "scenario_id": scenario_id,
                "scenario_name": scenario_name,

                "recipient_name": recipient_name,
                "recipient_account": recipient_account,

                "amount": int(amount),
                "purpose": purpose,

                # --------------------------------------
                # FDS-like Data
                # --------------------------------------

                "avg_transaction_amount": scenario_data[
                    "avg_transaction_amount"
                ],

                "is_new_recipient": scenario_data[
                    "is_new_recipient"
                ],

                "recent_loan": scenario_data[
                    "recent_loan"
                ],

                "transaction_count_24h": scenario_data[
                    "transaction_count_24h"
                ],

                "transaction_time": scenario_data[
                    "transaction_time"
                ],

                "device_change": scenario_data[
                    "device_change"
                ],

                "previous_transaction_count": scenario_data[
                    "previous_transaction_count"
                ],
            }

            st.session_state.page = "confirm"

            st.rerun()

    # --------------------------------------------------
    # Account Information
    # --------------------------------------------------

    st.markdown(
        """
<div class="transfer-summary"><div class="summary-label">출금 계좌</div><div class="summary-value">AI BANK · 123-456-789012</div></div>
""",
        unsafe_allow_html=True,
    )


# ==================================================
# Confirm Page
# ==================================================

def show_confirm():

    transaction = st.session_state.transaction

    # --------------------------------------------------
    # Safety Check
    # --------------------------------------------------

    if transaction is None:

        st.session_state.page = "home"
        st.rerun()

    # --------------------------------------------------
    # Back Button
    # --------------------------------------------------

    if st.button("← 송금 정보 수정"):

        st.session_state.page = "transfer"
        st.rerun()

    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    st.markdown(
        """
<div class="transfer-card">
    <div class="transfer-title">송금 정보 확인</div>
    <div class="transfer-description">입력하신 송금 정보를 확인해주세요.</div>
</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Recipient
    # --------------------------------------------------

    st.markdown(
        f"""
<div class="transfer-summary"><div class="summary-label">수취인</div><div class="summary-value">{transaction["recipient_name"]}</div><div class="summary-label">{transaction["recipient_account"]}</div></div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Amount
    # --------------------------------------------------

    st.markdown(
        f"""
<div class="transfer-summary"><div class="summary-label">송금 금액</div><div class="summary-value">₩{transaction["amount"]:,}</div></div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Purpose
    # --------------------------------------------------

    st.markdown(
        f"""
<div class="transfer-summary"><div class="summary-label">송금 목적</div><div class="summary-value">{transaction["purpose"]}</div></div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Scenario
    # --------------------------------------------------

    st.markdown(
        f"""
<div class="transfer-summary"><div class="summary-label">데모 시나리오</div><div class="summary-value">{transaction["scenario_name"]}</div></div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    # --------------------------------------------------
    # Continue
    # --------------------------------------------------

    if st.button(
        "송금 진행",
        use_container_width=True,
        type="primary",
    ):

        st.session_state.page = "risk_check"
        st.rerun()


# ==================================================
# Risk Check Page
# ==================================================

def show_risk_check():

    transaction = st.session_state.transaction

    # --------------------------------------------------
    # Safety Check
    # --------------------------------------------------

    if transaction is None:

        st.session_state.page = "home"
        st.rerun()

    # --------------------------------------------------
    # Calculate Risk
    # --------------------------------------------------

    risk_result = calculate_transaction_risk(
        transaction
    )

    st.session_state.risk_result = risk_result

    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    st.markdown(
        """
<div class="risk-card">
    <div class="transfer-title">거래 위험 분석</div>
    <div class="transfer-description">
        AI BANK의 거래 위험 분석 시스템이 송금 정보를 확인하고 있습니다.
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Transaction Summary
    # --------------------------------------------------

    st.markdown(
        f"""
<div class="transfer-summary"><div class="summary-label">송금 대상</div><div class="summary-value">{transaction["recipient_name"]}</div><div class="summary-label">{transaction["recipient_account"]}</div></div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="transfer-summary"><div class="summary-label">송금 금액</div><div class="summary-value">₩{transaction["amount"]:,}</div></div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Risk Score
    # --------------------------------------------------

    st.subheader("Transaction Risk Score")

    st.metric(
        label="거래 위험 점수",
        value=f'{risk_result["score"]} / 100',
    )

    # --------------------------------------------------
    # Risk Level
    # --------------------------------------------------

    level = risk_result["level"]

    if level == "CRITICAL":

        st.error("🔴 CRITICAL · 매우 높은 위험")

    elif level == "HIGH":

        st.warning("🟠 HIGH · 높은 위험")

    elif level == "MODERATE":

        st.warning("🟡 MODERATE · 주의 필요")

    else:

        st.success(
            "🟢 LOW · 현재 탐지된 위험이 낮습니다."
        )

    # --------------------------------------------------
    # Risk Signals
    # --------------------------------------------------

    st.subheader("탐지된 위험 신호")

    if risk_result["signals"]:

        for signal in risk_result["signals"]:

            st.write(
                f'**{signal["name"]}** '
                f'+{signal["score"]}점'
            )

            st.caption(
                signal["description"]
            )

    else:

        st.write(
            "현재 탐지된 주요 위험 신호가 없습니다."
        )

    # --------------------------------------------------
    # Temporary Message
    # --------------------------------------------------

    st.divider()

    st.info(
        "다음 단계에서 위험 거래가 탐지되면 "
        "AI CRACKER가 사용자에게 개입합니다."
    )

    # --------------------------------------------------
    # Back Home
    # --------------------------------------------------

    if st.button(
        "← 홈으로 돌아가기",
        use_container_width=True,
    ):

        go_home()
        st.rerun()


# ==================================================
# Page Router
# ==================================================

if st.session_state.page == "home":

    show_home()

elif st.session_state.page == "transfer":

    show_transfer()

elif st.session_state.page == "confirm":

    show_confirm()

elif st.session_state.page == "risk_check":

    show_risk_check()