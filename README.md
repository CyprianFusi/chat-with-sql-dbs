<div align="center">
  <img src="https://raw.githubusercontent.com/CyprianFusi/chat-with-sql-dbs/main/assets/binati_logo.png" alt="BINATI AI Logo" width="75"/><strong></strong>

  # 🛢️ Chat with SQL Databases

  _By **BINATI AInalytics**_
</div>


A Streamlit web application that allows you to chat with SQL databases using natural language queries powered by LangChain and Groq's LLM API.

# Demo



## ✨ Features

- **Multi-Database Support**: Connect to SQLite, MySQL, or PostgreSQL databases
- **Natural Language Queries**: Ask questions about your data in plain English
- **Real-time Streaming**: Get responses as they're generated
- **Interactive Chat Interface**: Conversation-style interaction with your database
- **Secure Connections**: Password-protected database credentials
- **Local SQLite Support**: Includes a local `coursework.db` for quick testing

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository** (or download the files)
   ```bash
   git clone https://github.com/CyprianFusi/chat-with-sql-dbs.git
   cd chat-with-sql-dbs
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional)
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Prepare your database** (if using local SQLite)
   - Ensure `coursework.db` exists in the project directory
   - Or modify the code to point to your SQLite database

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 🔧 Configuration

### Database Options

The application supports three types of databases:

#### 1. **SQLite (Local)**
- **File**: `coursework.db` (must be in the same directory as `app.py`)
- **Use case**: Testing, small datasets, local development
- **Setup**: No additional configuration required

#### 2. **MySQL Database**
- **Required fields**:
  - Host (e.g., `localhost` or `your-mysql-host.com`)
  - Username
  - Password
  - Database name
- **Use case**: Production applications, shared databases

#### 3. **PostgreSQL Database**
- **Required fields**:
  - Host (e.g., `localhost` or `your-postgres-host.com`)
  - Username
  - Password
  - Database name
  - Port (default: 5432)
- **Use case**: Enterprise applications, complex queries

### API Configuration

1. **Get a Groq API key**:
   - Visit [Groq Cloud](https://console.groq.com)
   - Sign up for an account
   - Generate an API key

2. **Enter the API key**:
   - Use the sidebar input field in the application
   - Or add it to your `.env` file as `GROQ_API_KEY`

## 💡 Usage Examples

Once the application is running, you can ask natural language questions about your database:

- **Data Exploration**:
  - "Show me all tables in the database"
  - "What columns are in the users table?"
  - "How many records are in the orders table?"

- **Business Queries**:
  - "What are the top 5 customers by total purchase amount?"
  - "Show me sales trends for the last quarter"
  - "Which products have the highest ratings?"

- **Analytical Questions**:
  - "What's the average order value by customer segment?"
  - "Find customers who haven't made a purchase in the last 90 days"
  - "Compare revenue between different product categories"

## 🏗️ Project Structure

```
project-directory/
│
├── app.py              # Main Streamlit application
├── coursework.db       # Sample SQLite database (if using local option)
├── .env               # Environment variables (optional)
├── README.md          # This file
└── requirements.txt   # Python dependencies (optional)
```

## 📦 Dependencies

- **streamlit**: Web application framework
- **langchain-community**: LangChain community integrations
- **langchain-groq**: Groq LLM integration
- **python-dotenv**: Environment variable management
- **sqlalchemy**: Database toolkit
- **mysql-connector-python**: MySQL database connector
- **psycopg2-binary**: PostgreSQL adapter

## 🛠️ Technical Details

### Architecture

- **Frontend**: Streamlit for the web interface
- **LLM**: Groq's Llama-3.1-8b-instant model for natural language processing
- **Framework**: LangChain for SQL agent creation and database interaction
- **Database Layer**: SQLAlchemy for database connections and queries

### Key Components

- **SQL Agent**: Uses LangChain's `create_sql_agent` with tool-calling capabilities
- **Database Abstraction**: `SQLDatabase` wrapper for different database types
- **Streaming**: Real-time response streaming with `StreamlitCallbackHandler`
- **Caching**: Database connections cached for 2 hours for performance

## 🔒 Security Considerations

- API keys and database passwords are handled securely through Streamlit's input widgets
- Database connections use proper SQLAlchemy engines with appropriate drivers
- SQLite connections include thread safety configurations

## 🐛 Troubleshooting

### Common Issues

1. **"Please provide all connection details" error**
   - Ensure all required database fields are filled in the sidebar

2. **"Please enter the groq api key" message**
   - Add your Groq API key in the sidebar input field

3. **Database connection errors**
   - Verify your database credentials and network connectivity
   - For local SQLite, ensure `coursework.db` exists in the project directory

4. **Package import errors**
   - Install all required dependencies: `pip install -r requirements.txt`

### Performance Tips

- Use the "Clear message history" button to reset the conversation
- Database connections are cached, but may need refreshing after 2 hours
- For large databases, consider adding specific table/column filters

## 🤝 Contributing

Feel free to contribute by:
- Adding support for additional database types
- Improving the UI/UX
- Adding more sophisticated query capabilities
- Enhancing error handling and validation

## 📄 License

[Add your license information here]

## 🔗 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [LangChain Documentation](https://python.langchain.com)
- [Groq API Documentation](https://console.groq.com/docs)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org)
