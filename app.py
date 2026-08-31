import streamlit as st

from config.settings import APP_NAME, APP_VERSION


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

.back-button {
    margin-bottom: 1rem;
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

    if st.button(
        "← 홈으로",
        use_container_width=False,
    ):
        go_home()
        st.rerun()

    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    st.markdown(
        """
<div class="transfer-card">
    <div class="transfer-title">송금하기</div>
    <div class="transfer-description">
        송금할 정보를 입력해주세요.
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Transfer Form
    # --------------------------------------------------

    with st.form("transfer_form"):

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

            st.session_state.transaction = {
                "recipient_name": recipient_name,
                "recipient_account": recipient_account,
                "amount": int(amount),
                "purpose": purpose,
            }

            st.session_state.page = "confirm"

            st.rerun()

    # --------------------------------------------------
    # Account Information
    # --------------------------------------------------

    st.markdown(
        """
<div class="transfer-summary">
    <div class="summary-label">출금 계좌</div>
    <div class="summary-value">
        AI BANK · 123-456-789012
    </div>
</div>
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

    if st.button(
        "← 송금 정보 수정",
        use_container_width=False,
    ):
        st.session_state.page = "transfer"
        st.rerun()

    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    st.markdown(
        """
<div class="transfer-card">
    <div class="transfer-title">송금 정보 확인</div>
    <div class="transfer-description">
        입력하신 송금 정보를 확인해주세요.
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Recipient
    # --------------------------------------------------

    st.markdown(
        f"""
<div class="transfer-summary">
    <div class="summary-label">수취인</div>
    <div class="summary-value">
        {transaction["recipient_name"]}
    </div>
    <div class="summary-label">
        {transaction["recipient_account"]}
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Amount
    # --------------------------------------------------

    st.markdown(
        f"""
<div class="transfer-summary">
    <div class="summary-label">송금 금액</div>
    <div class="summary-value">
        ₩{transaction["amount"]:,}
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Purpose
    # --------------------------------------------------

    st.markdown(
        f"""
<div class="transfer-summary">
    <div class="summary-label">송금 목적</div>
    <div class="summary-value">
        {transaction["purpose"]}
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    # --------------------------------------------------
    # Next Step
    # --------------------------------------------------

    if st.button(
        "송금 진행",
        use_container_width=True,
        type="primary",
    ):
        st.session_state.page = "risk_check"
        st.rerun()


# ==================================================
# Placeholder: Risk Check
# ==================================================

def show_risk_check():

    st.title("거래 확인")

    st.info(
        "다음 단계에서 Transaction Risk Model이 "
        "이 위치에 연결됩니다."
    )

    st.write(
        "현재는 위험 분석을 구현하기 전 단계입니다."
    )

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