# Raiz DE Interview
Repo for the Raiz Data Engineer technical interview round.

## Table of Contents
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Interview Questions](#interview-q)

---

## Repository Structure
```plaintext
├── src/               # Contains a Postgres client and utility functions
├── .env-example       # Example of .env file
├── data.csv           # File that you will be ingesting
├── main.py            # Entry point for your program  
├── readme.md          # You're here 
└── requirements.txt   # Python libraries to install for the project
```

---
## Getting Started
1. **Make a directory named de_interview**
2. **Clone the Repository into this directory**
``` bash
git clone https://github.com/sbuckingham-raiz/de_interview.git ./de_interview
```
3. **Set Up the Environment**
``` bash
cp ./.env-example ./.env
```
4. **Install Dependencies**
``` bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

---
## Interview Questions
1. **Load the file data.csv into a Postgres database table named "data" **