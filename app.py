import streamlit as st

from config.settings import APP_NAME, APP_VERSION


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🛡️",
    layout="centered",
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🛡️ AI CRACKER")

st.caption(
    "금융사기 예방을 위한 AI Intervention Layer"
)

st.divider()


# --------------------------------------------------
# Introduction
# --------------------------------------------------

st.subheader("송금 전, 한 번 더 확인하세요.")

st.write(
    """
AI CRACKER는 금융 거래의 위험 신호를 분석하고,
사용자가 왜 해당 거래를 신뢰하고 있는지 파악한 뒤
필요한 검증 행동을 안내하는 금융사기 예방 서비스입니다.
"""
)

st.info(
    """
현재 서비스는 실제 금융정보가 아닌
가상 거래 데이터를 이용한 MVP입니다.
"""
)


# --------------------------------------------------
# Start Button
# --------------------------------------------------

if st.button(
    "💸 가상 은행 앱 시작하기",
    use_container_width=True,
):

    st.session_state.started = True


# --------------------------------------------------
# Temporary Bank Screen
# --------------------------------------------------

if st.session_state.get("started", False):

    st.divider()

    st.subheader("🏦 AI BANK")

    st.write("가상 계좌")

    st.metric(
        label="사용 가능 잔액",
        value="₩12,580,000",
    )

    st.write("")

    st.button(
        "송금하기",
        use_container_width=True,
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(f"AI CRACKER MVP {APP_VERSION}")

st.caption(
    "Demo Environment · No Real Financial Data"
)