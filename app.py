import streamlit as st
from utils.connection import get_connection

st.set_page_config(
    page_title="Netflix Content Intelligence Platform",
    layout="wide"
)

st.title("Netflix Content Intelligence Platform")

try:
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM ANALYTICS.FACT_CONTENT
    """)

    count = cursor.fetchone()[0]

    st.success("Connected to Snowflake")

    st.metric(
        "Total Titles",
        count
    )

except Exception as e:
    st.error(e)

except Exception as e:
    st.error(e)