from dotenv import load_dotenv, find_dotenv
import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
from langchain_groq import ChatGroq

_ = load_dotenv(find_dotenv())

st.set_page_config(page_title="LangChain: Chat with SQL DB", page_icon="⛁")
st.title("🛢Chat with SQL Databases") 


LOCAL_DB = "USE_LOCAL_DB"
MYSQL = "USE_MYSQL"
POSTGRES = "USE_POSTGRES"

db_opts = ["Coursework.db (SQLite)", "MySQL Database", 'PostgresSQL']

selected_opt = st.sidebar.radio(label="Choose the DB to chat with", options=db_opts)

# MYSQL DB connection
if db_opts.index(selected_opt)==1:
    db_uri = MYSQL
    db_host = st.sidebar.text_input("Provide MySQL Host")
    db_user = st.sidebar.text_input("MYSQL User")
    db_password = st.sidebar.text_input("MYSQL password",type="password")
    db_name = st.sidebar.text_input("MySQL database")

# PostgresSQL DB connection
elif db_opts.index(selected_opt)==2:
    db_uri = POSTGRES
    db_user = st.sidebar.text_input("Postgres User")
    db_password = st.sidebar.text_input("Postgres Password", type="password")
    db_name = st.sidebar.text_input("Postgres Database Name")
    db_port = st.sidebar.text_input("Postgres Port", value="5432")
    db_host = st.sidebar.text_input("Postgres Host")

# Local SQLite3 DB connection
else:
    db_uri=LOCAL_DB

@st.cache_resource(ttl="2h")
def configure_db(db_uri, db_host=None, db_user=None, db_password=None, db_name=None, db_port=None):
    if db_uri == LOCAL_DB:
        db_filepath = (Path(__file__).parent / "coursework.db").absolute()
        print(db_filepath)
        # Correct SQLite connection string for SQLAlchemy
        engine = create_engine(f"sqlite:///{db_filepath}", connect_args={"check_same_thread": False})
        return SQLDatabase(engine)
    elif db_uri == MYSQL:
        if not (db_host and db_user and db_password and db_name):
            st.error("Please provide all MySQL connection details.")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}"))
    elif db_uri == POSTGRES:
        if not (db_host and db_user and db_password and db_name):
            st.error("Please provide all Postgres connection details.")
            st.stop()
        return SQLDatabase.from_uri(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Groq API key
api_key = st.sidebar.text_input(label="Groq API Key", type="password")
if api_key:
    llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-8b-instant", streaming=True)

    
    if db_uri == MYSQL:
        db = configure_db(db_uri, db_host, db_user, db_password, db_name)
    elif db_uri == POSTGRES:
        db = configure_db(db_uri, db_host, db_user, db_password, db_name, db_port)
    else:
        db = configure_db(db_uri)

    ## toolkit
    # toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    agent_executor = create_sql_agent(
        llm = llm,
        db = db,
        agent_type= 'tool-calling',     
        verbose = True
    )

    if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_query = st.chat_input(placeholder="Ask anything from the database")

    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        st.chat_message("user").write(user_query)

        with st.chat_message("assistant"):
            streamlit_callback = StreamlitCallbackHandler(st.container())
            response = agent_executor.run(user_query, callbacks=[streamlit_callback])
            st.session_state.messages.append({"role":"assistant","content":response})
            st.write(response)

else:
    st.info("Please enter the groq api key")

        


