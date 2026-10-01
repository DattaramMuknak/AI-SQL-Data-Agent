# 🤖 AI SQL Data Agent

An intelligent **AI-powered SQL and ETL data agent** built with **LangGraph, Groq, PostgreSQL, LangChain, and Pandas**.

The system accepts natural-language instructions and intelligently routes them to specialized agents. It can generate and execute safe SQL queries against PostgreSQL databases or perform ETL operations such as extracting data from APIs, transforming datasets, and saving results in multiple formats.

---

## 🚀 Features

### 🧠 Intelligent Query Routing

The main Data Agent analyzes the user's natural-language request and automatically routes it to the appropriate specialized agent:

* **SQL Analyst Agent** → Database queries and analysis
* **ETL Analyst Agent** → API extraction and data transformation

### 🗄️ SQL Agent

The SQL Analyst Agent can:

* Convert natural-language questions into SQL
* Understand PostgreSQL database schemas
* Generate SQL queries using an LLM
* Validate SQL queries before execution
* Prevent destructive SQL operations
* Execute safe queries
* Generate human-readable answers from query results

### 🔄 ETL Agent

The ETL Analyst Agent can:

* Extract data from REST APIs
* Convert JSON/API responses into structured data
* Transform datasets using Pandas
* Generate Pandas code dynamically
* Save processed data as:

  * CSV
  * JSON
  * Parquet
* Execute ETL tools through LangChain tool calling

### 🔐 SQL Safety

The SQL workflow includes validation to prevent potentially destructive database operations such as:

```text
INSERT
UPDATE
DELETE
DROP
ALTER
TRUNCATE
```

The system is designed primarily for safe data analysis and read operations.

### ⚡ AI Model

The project uses **Groq** through its OpenAI-compatible API endpoint.

Current model configuration:

```text
openai/gpt-oss-20b
```

Groq provides the LLM inference layer while LangChain provides the interface used by the agents.

---

# 🏗️ Architecture

```text
                         ┌──────────────────────────┐
                         │        User Query        │
                         │   Natural Language Input │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │       Data Agent         │
                         │      Router Node         │
                         └────────────┬─────────────┘
                                      │
                         ┌────────────┴────────────┐
                         │                         │
                         ▼                         ▼
              ┌───────────────────┐     ┌───────────────────┐
              │   SQL Analyst     │     │    ETL Analyst    │
              │      Agent        │     │       Agent       │
              └─────────┬─────────┘     └─────────┬─────────┘
                        │                         │
                        ▼                         ▼
              ┌───────────────────┐     ┌───────────────────┐
              │   PostgreSQL      │     │  REST APIs / CSV  │
              │     Database      │     │   Pandas / Files  │
              └───────────────────┘     └───────────────────┘
```

## 🔄 Agent Workflow

```text
User Input
    ↓
Data Agent
    ↓
Query Classification
    ↓
 ┌───────────────┐
 │               │
SQL             ETL
 │               │
 ▼               ▼
SQL Agent      ETL Agent
 │               │
 ▼               ▼
PostgreSQL     API / Files
 │               │
 └───────┬───────┘
         ▼
    Final Response
```

---

# 🛠️ Technology Stack

| Technology    | Purpose                      |
| ------------- | ---------------------------- |
| Python        | Core programming language    |
| LangGraph     | Agent orchestration          |
| LangChain     | LLM and tool integration     |
| Groq          | LLM inference                |
| PostgreSQL    | Relational database          |
| Pandas        | Data transformation          |
| Pydantic      | Structured data validation   |
| psycopg2      | PostgreSQL connection        |
| python-dotenv | Environment configuration    |
| uv            | Python dependency management |

---

# 📁 Project Structure

```text
AI-SQL-Data-Agent/
│
├── agents/
│   ├── __init__.py
│   ├── data_agent.py
│   ├── sql_analyst.py
│   └── etl_analyst.py
│
├── Models/
│   ├── __init__.py
│   └── schema.py
│
├── utils/
│   ├── __init__.py
│   ├── database.py
│   ├── etl_tools.py
│   └── llm_pick.py
│
├── data/
│   ├── extract/
│   ├── transform/
│   ├── users.csv
│   ├── vehicles.csv
│   ├── rides.csv
│   ├── payments.csv
│   └── ratings.csv
│
├── feed_db.py
├── main.py
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
└── README.md
```

---

# 📊 Sample Dataset

The project includes sample datasets for database analysis:

| Dataset  | Records |
| -------- | ------: |
| Users    |  10,000 |
| Vehicles |   3,000 |
| Rides    |  20,000 |
| Payments |  16,073 |
| Ratings  |  12,000 |

These datasets are loaded into PostgreSQL using `feed_db.py`.

---

# ⚙️ Requirements

Before running the project, install:

* Python 3.12+
* PostgreSQL
* Git
* uv
* Groq API key

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/DattaramMuknak/AI-SQL-Data-Agent.git
cd AI-SQL-Data-Agent
```

## 2. Create the virtual environment

Using `uv`:

```bash
uv sync
```

This installs the dependencies defined by the project.

---

# 🔑 Environment Configuration

Create a `.env` file in the project root.

You can use `.env.example` as a template:

```env
GROQ_API_KEY=your_groq_api_key_here

port=5432
database=DataAgent
host=localhost
user=postgres
password=your_postgres_password
```

### ⚠️ Security

Never commit your real `.env` file.

The repository uses `.gitignore` to exclude:

```text
.env
.venv
__pycache__
```

---

# 🗄️ PostgreSQL Setup

Make sure PostgreSQL is running.

Create a database named:

```text
DataAgent
```

Then load the provided datasets:

```bash
python feed_db.py
```

The script creates the required tables and loads the CSV datasets into PostgreSQL.

---

# ▶️ Running the Project

Run the main Data Agent:

```bash
python main.py
```

The agent will process the natural-language request and route it to the appropriate specialized agent.

---

# 💬 Example SQL Queries

You can ask questions such as:

```text
Show me the top 5 users with the highest ratings.
```

```text
What is the average rating for each vehicle type?
```

```text
Show me the number of rides for each vehicle type.
```

```text
What is the total payment amount collected?
```

The Data Agent determines that these are SQL-related requests and routes them to the SQL Analyst Agent.

---

# 🔄 Example ETL Request

You can also provide an API extraction request:

```text
Extract the data from the API endpoint
https://pokeapi.co/api/v2/pokemon
and save it as CSV.
```

The system:

```text
User Request
     ↓
Data Agent
     ↓
ETL Agent
     ↓
extract_load_tool
     ↓
PokeAPI
     ↓
CSV
```

Example output:

```text
data/extract/csv/extracted_data.csv
```

---

# 🔧 ETL Operations

The ETL Agent supports two primary tools.

### 1. Extract & Load

```text
extract_load_tool
```

Used to:

```text
API → JSON → Structured Data → CSV/JSON/Parquet
```

### 2. Transform & Load

```text
transform_load_tool
```

Used to:

```text
Existing Dataset
       ↓
     Pandas
       ↓
Transformation
       ↓
CSV / JSON / Parquet
```

For example:

```text
Transform rides.csv by filtering
rides with rating greater than 4.0
and save the result as JSON.
```

---

# 🧠 LangGraph Agent Design

The project uses LangGraph to orchestrate the agents.

### Main Data Agent

Responsible for:

1. Receiving the user request
2. Understanding the intent
3. Classifying the request
4. Routing it to SQL or ETL
5. Returning the final response

### SQL Analyst Agent

Responsible for:

1. Query curation
2. Schema retrieval
3. SQL generation
4. SQL safety validation
5. Query execution
6. Result processing
7. Final answer generation

### ETL Analyst Agent

Responsible for:

1. Understanding ETL requirements
2. Selecting appropriate tools
3. Extracting API data
4. Generating Pandas transformations
5. Executing transformations
6. Saving the output
7. Reporting the result

---

# 🧩 Data Models

The project uses Pydantic schemas to maintain structured agent state.

### RouterSchema

```python
class RouterSchema(BaseModel):
    answer: Literal["sql", "etl"]
    comments: str
```

### DataAgentSchema

```python
class DataAgentSchema(BaseModel):
    messages: List
    route_response: str
```

### ETLAgentSchema

```python
class ETLAgentSchema(BaseModel):
    messages: List
```

---

# 🔐 Security

The project follows several security practices:

### Environment Security

API keys and database credentials are stored in:

```text
.env
```

and are excluded from Git using:

```text
.gitignore
```

### SQL Validation

The SQL workflow validates generated queries before execution.

Destructive operations such as:

```text
DELETE
DROP
ALTER
UPDATE
INSERT
TRUNCATE
```

are restricted by the SQL safety workflow.

### Structured Outputs

Pydantic models are used to validate structured agent responses.

---

# 📈 Example Workflow

### SQL Request

```text
User:
"Show me the average rating for each vehicle type."

        ↓

Data Agent

        ↓

SQL Analyst Agent

        ↓

Database Schema

        ↓

SQL Generation

        ↓

SQL Safety Validation

        ↓

PostgreSQL

        ↓

Result

        ↓

Natural Language Answer
```

### ETL Request

```text
User:
"Extract Pokemon data from the PokeAPI and save it as CSV."

        ↓

Data Agent

        ↓

ETL Analyst Agent

        ↓

Tool Selection

        ↓

API Request

        ↓

Data Processing

        ↓

CSV Output
```

---

# 🎯 Project Goals

This project demonstrates practical implementation of:

* Agentic AI
* Multi-agent systems
* Natural-language database interaction
* Text-to-SQL
* SQL safety validation
* ETL automation
* Tool calling
* LangGraph workflows
* PostgreSQL integration
* LLM-powered data analysis
* API data extraction
* Pandas-based data transformation

---

# 🧪 Testing the ETL Agent

A working test request:

```text
I want to extract the data from the API endpoint
'https://pokeapi.co/api/v2/pokemon'
and save it to data/extract/csv.
```

Expected output:

```text
Data successfully extracted and saved to:
data/extract/csv/extracted_data.csv
```

---

# 🔮 Future Improvements

Possible future enhancements include:

* Web-based chat interface
* Streaming agent responses
* Authentication and user management
* More database connectors
* Additional ETL tools
* Better SQL query optimization
* Agent memory
* Query history
* Data visualization
* Automated data quality checks
* More advanced SQL safety policies
* Docker deployment
* Cloud deployment

---

# 📚 Learning Resources

* [LangGraph](https://langchain-ai.github.io/langgraph/)
* [LangChain](https://python.langchain.com/)
* [PostgreSQL](https://www.postgresql.org/docs/)
* [Groq](https://console.groq.com/)

---

# 👨‍💻 Author

**Dattaram Muknak**

AI & Data Science Engineer | AI/ML | Backend | Data Engineering

GitHub:
https://github.com/DattaramMuknak

---

# 📄 License

This project is created as an AI engineering and learning project.

---

## ⭐ If you find this project useful

Feel free to explore the code, raise issues, and contribute improvements.

**Built with Python, LangGraph, LangChain, Groq, PostgreSQL, and Pandas.**
