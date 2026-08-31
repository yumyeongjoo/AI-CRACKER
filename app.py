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

</style>
""",
    unsafe_allow_html=True,
)


# ==================================================
# Session State
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


# ==================================================
# Header
# ==================================================

st.markdown(
    """
<div class="bank-header">
    <div class="bank-name">🏦 AI BANK</div>
    <div class="notification">🔔</div>
</div>
""",
    unsafe_allow_html=True,
)


# ==================================================
# Greeting
# ==================================================

st.markdown(
    """
<div class="greeting">안녕하세요</div>
<div class="username">사용자님 👋</div>
""",
    unsafe_allow_html=True,
)


# ==================================================
# Balance Card
# ==================================================

st.markdown(
    """
<div class="balance-card"><div class="balance-label">총 보유 잔액</div><div class="balance">₩12,580,000</div><div class="account-number">AI BANK · 123-456-789012</div></div>
""",
    unsafe_allow_html=True,
)


# ==================================================
# Quick Actions
# ==================================================

st.subheader("빠른 메뉴")

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "💸 송금하기",
        use_container_width=True,
    ):
        st.session_state.page = "transfer"

with col2:
    if st.button(
        "📋 거래내역",
        use_container_width=True,
    ):
        st.session_state.page = "history"


# ==================================================
# Recent Transactions
# ==================================================

st.markdown(
    """
<div class="transaction-card"><div class="transaction-title">최근 거래</div><div class="transaction-row"><div><div class="transaction-name">급여</div><div class="transaction-date">08.25</div></div><div class="transaction-amount positive">+₩2,500,000</div></div><div class="transaction-row"><div><div class="transaction-name">편의점</div><div class="transaction-date">08.28</div></div><div class="transaction-amount negative">-₩8,500</div></div><div class="transaction-row"><div><div class="transaction-name">카페</div><div class="transaction-date">08.28</div></div><div class="transaction-amount negative">-₩6,000</div></div><div class="transaction-row"><div><div class="transaction-name">온라인 쇼핑</div><div class="transaction-date">08.29</div></div><div class="transaction-amount negative">-₩42,000</div></div></div>
""",
    unsafe_allow_html=True,
)


# ==================================================
# Footer
# ==================================================

st.divider()

st.caption(f"{APP_NAME} MVP {APP_VERSION}")
st.caption("Demo Environment · No Real Financial Data")