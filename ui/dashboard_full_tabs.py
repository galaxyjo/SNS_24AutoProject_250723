# -*- coding: utf-8 -*-
import sqlite3

import pandas as pd
import streamlit as st

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"

conn = sqlite3.connect(DB_PATH)
trace_df = pd.read_sql_query("SELECT * FROM log_trace ORDER BY inserted_at DESC", conn)
commit_df = pd.read_sql_query(
    "SELECT * FROM git_commits ORDER BY inserted_at DESC", conn
)
hook_df = pd.read_sql_query("SELECT * FROM hook_logs ORDER BY executed_at DESC", conn)
session_df = pd.read_sql_query(
    "SELECT * FROM session_results ORDER BY executed_at DESC", conn
)
conn.close()

st.set_page_config(page_title="LogTrace Full Dashboard", layout="wide")
st.title("?? LogTrace 통합 대시보드")

tab1, tab2, tab3, tab4 = st.tabs(
    ["?? 함수 로그", "?? Git 커밋", "?? Hook 로그", "?? 세션 결과"]
)

with tab1:
    st.subheader("?? 함수 메타 로그")
    st.dataframe(trace_df, use_container_width=True)

with tab2:
    st.subheader("?? Git 커밋 내역")
    st.dataframe(commit_df, use_container_width=True)

with tab3:
    st.subheader("?? Git Hook 로그")
    st.dataframe(hook_df, use_container_width=True)

with tab4:
    st.subheader("?? 실행 세션 기록")
    st.dataframe(session_df, use_container_width=True)
