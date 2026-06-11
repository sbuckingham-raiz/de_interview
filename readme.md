# Raiz DE Interview
Repo for the Raiz Data Engineer technical interview round.

## Table of Contents
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)

---

## Repository Structure
```plaintext
├── src/               # Contains a Postgres client with methods that connect and ingest files as well as a file with utilitiy functions.
├── .env-example       # Example of .env file
├── data.csv           # File that you will be ingesting
├── main.py            # Entry point for your program  
├── readme.md          # You're here 
└── requirements.txt   # Python libraries to install for the project
```

---
## Getting Started
1. **Clone the Repository**
``` bash
git clone https://github.com/sbuckingham-raiz/de_interview.git
```
2. **Set Up the Environment**
``` bash
cp ./.env-example ./.env
```
3. **Install Dependencies**
``` bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```