import streamlit as st
import importlib
import config
import time

# Optional: auto-refresh
from streamlit_autorefresh import st_autorefresh

# Auto-refresh every 3 seconds
st_autorefresh(interval=3000, key="refresh")

# Reload config.py each time
importlib.reload(config)

# Read values from config.py
summary = config.summary
score = config.score

# Page layout
st.set_page_config(layout="wide", page_title="Twitch + Sentiment Dashboard")
st.title("📺 Twitch + Sentiment Dashboard")
st.markdown("---")

left, right = st.columns([2, 1])

with left:
    twitch_embed = """
    <iframe
        src="https://player.twitch.tv/?channel=KaiCenat&parent=localhost"
        height="400"
        width="100%"
        frameborder="0"
        allowfullscreen="true">
    </iframe>
    """
    st.components.v1.html(twitch_embed, height=400)

with right:
    st.subheader("🎯 Sentiment Score")
    st.metric("Score (1–5)", f"{score:.1f}")

    st.subheader("📝 Live Chat Summary")
    st.markdown(summary)

