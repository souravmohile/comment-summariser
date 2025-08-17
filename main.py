import streamlit as st
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

st.set_page_config(layout="wide",)

st.title("Livestream Comments Analysis")
st.divider()

col1, col2 = st.columns([3, 1])
with col1: 
    st.video("https://www.youtube.com/watch?v=sYv9D8CIDJQ&list=PLoW1SIeAWaWb1IDY_WuLKvZygiJudUBSd")
    with st.container(border=True):
        st.header("Johnny Depp v. Amber Heard Defamation Trial - Plaintiff Opening Statement - Benjamin Chew")

    with st.container(border=True):
        text = """
        Johnny Depp's attorney Benjamin Chew presents opening states in the defamation trial. 
        Actor Johnny Depp is suing ex-wife Amber Heard for \$50 million for defamation in connection with Heard’s 2018 Washington Post op-ed, in which she spoke out about being the victim of domestic violence. 
        Heard’s article did not specifically name Depp as her alleged abuser, but according to Depp’s lawsuit, it relied “on the central premise that Ms. Heard was a domestic abuse victim and that Mr. Depp perpetrated domestic violence against her.” 
        Amber Heard is counter-suing Depp for $100 million. The defamation trial began Monday in Fairfax County Circuit Court in Virginia, with jury selection completing on the same day. There is a possibility of celebrity witnesses testifying, including James Franco and Elon Musk. 
        Tune in to the Law&Crime Network for daily coverage of this high-profile trial. 

        #JohnnyDepp #AmberHeard
        """

        st.write(text)
with col2:
    with st.container(border=True):
        st.subheader("Comments Summary")
        st.write("The comments are saying that amber herd is not a good person.")

    with st.container(border=True):
        st.subheader("Viewer Sentiment")
        df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

        st.line_chart(df)

    with st.container(border=True):
        st.subheader("Comments")
        st.write("comment 1")
        st.write("comment 2")
        st.write("comment 3")
        st.write("comment 4")
        st.write("comment 5")
        st.write("comment 6")
        st.write("comment 7")


# Make sure that you store the summary and history so that you can update the metrics as the person scrolls through the video
