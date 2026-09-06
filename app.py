import asyncio
import streamlit as st

from Kisan_agent import agent
from agents import Runner


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Kisan Advisor",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main App */
    .stApp {
        background: linear-gradient(135deg, #f4f8f1 0%, #eef5ea 100%);
    }

    /* Main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Hero Header */
    .hero {
        background: linear-gradient(135deg, #1b5e20, #2e7d32);
        padding: 32px;
        border-radius: 22px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(46, 125, 50, 0.18);
    }

    .hero-title {
        color: white;
        font-size: 42px;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        color: #dcedc8;
        font-size: 17px;
        margin-top: 8px;
    }

    .status {
        display: inline-block;
        background: rgba(255, 255, 255, 0.15);
        color: white;
        padding: 7px 14px;
        border-radius: 20px;
        font-size: 13px;
        margin-top: 15px;
    }

    /* Information Cards */
    .info-card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #e2eadf;
        box-shadow: 0 5px 18px rgba(0, 0, 0, 0.05);
        min-height: 125px;
    }

    .info-icon {
        font-size: 28px;
    }

    .info-title {
        font-weight: 700;
        color: #1b5e20;
        font-size: 17px;
        margin-top: 8px;
    }

    .info-text {
        color: #666;
        font-size: 14px;
        margin-top: 5px;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #f8fbf6;
        border-right: 1px solid #dfe9db;
    }

    .sidebar-title {
        font-size: 24px;
        font-weight: 800;
        color: #1b5e20;
    }

    .sidebar-text {
        color: #666;
        font-size: 14px;
        line-height: 1.6;
    }

    /* Chat */
    [data-testid="stChatMessage"] {
        border-radius: 16px;
        margin-bottom: 12px;
    }

    /* Input */
    [data-testid="stChatInput"] {
        border-radius: 18px;
    }

    /* Buttons */
    .stButton button {
        border-radius: 10px;
        font-weight: 600;
    }

    /* Welcome Box */
    .welcome {
        background: white;
        border: 1px solid #e0e9dc;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 20px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.04);
    }

    .welcome-title {
        font-size: 24px;
        font-weight: 700;
        color: #1b5e20;
    }

    .welcome-text {
        color: #666;
        font-size: 15px;
        margin-top: 8px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #777;
        font-size: 12px;
        margin-top: 30px;
        padding: 15px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🌾 Kisan Advisor</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-text">
        A smart AI farming assistant designed to help Pakistani
        farmers with weather, crops and market-related decisions.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🛠️ Available Tools")

    st.markdown("""
    **🌤️ Weather**

    Live weather information using Open-Meteo.

    **🌱 Crop Information**

    Information about wheat, rice and maize.

    **💰 Market Price**

    Seasonal price ranges and selling advice.
    """)

    st.divider()

    st.markdown("### 💡 Try asking")

    st.markdown("""
    - Wheat ke liye weather advice?
    - Rice ke liye best season kya hai?
    - Maize ko kitna pani chahiye?
    - Wheat kab sell karni chahiye?
    - Faisalabad ka weather kaisa hai?
    """)

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# HERO HEADER
# ============================================================

st.markdown("""
<div class="hero">

    <div class="hero-title">
        🌾 Kisan Advisor
    </div>

    <div class="hero-subtitle">
        AI-powered farming assistant for Pakistani farmers
    </div>

    <div class="status">
        🟢 AI Agent Online
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INFORMATION CARDS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown("""
    <div class="info-card">

        <div class="info-icon">🌤️</div>

        <div class="info-title">
            Live Weather
        </div>

        <div class="info-text">
            Get weather information for your city.
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="info-card">

        <div class="info-icon">🌱</div>

        <div class="info-title">
            Crop Guidance
        </div>

        <div class="info-text">
            Learn about season, soil, water and crop risks.
        </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="info-card">

        <div class="info-icon">💰</div>

        <div class="info-title">
            Market Advice
        </div>

        <div class="info-text">
            Get seasonal market price and selling guidance.
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# WELCOME MESSAGE
# ============================================================

if len(st.session_state.messages) == 0:

    st.markdown("""
    <div class="welcome">

        <div class="welcome-title">
            👋 Welcome to Kisan Advisor
        </div>

        <div class="welcome-text">
            Ask me about crops, weather, farming conditions,
            or market prices.
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Ask Kisan Advisor about farming..."
)


# ============================================================
# AGENT EXECUTION
# ============================================================

if user_input:

    # --------------------------------------------------------
    # Save user message
    # --------------------------------------------------------

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })


    # --------------------------------------------------------
    # Display user message
    # --------------------------------------------------------

    with st.chat_message("user"):

        st.markdown(user_input)


    # --------------------------------------------------------
    # Generate agent response
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("🌾 Kisan Advisor is thinking..."):

            try:

                # IMPORTANT:
                # Use Runner.run(), NOT agent.run()

                result = asyncio.run(
                    Runner.run(
                        agent,
                        user_input
                    )
                )


                # ------------------------------------------------
                # Get final response
                # ------------------------------------------------

                response = result.final_output


                # ------------------------------------------------
                # Display response
                # ------------------------------------------------

                st.markdown(response)


                # ------------------------------------------------
                # Save assistant response
                # ------------------------------------------------

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })


            except Exception as e:

                error_message = (
                    "⚠️ Agent ko run karte waqt error aaya:\n\n"
                    f"`{str(e)}`"
                )

                st.error(error_message)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    🌾 Kisan Advisor • AI Farming Assistant
    • Built with Python & Streamlit

</div>
""", unsafe_allow_html=True)