##AI Engineering

# To install dependencies in .vevn
1. Create a venv:
    macOS / Linux(with Python 3):
    python3 -m venv .venv
    
2. Activate it:
    macOS / Linux:
    source .venv/bin/activate

3. Upgrade pip and install:
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt

# Tokenization
- Package to install ``pip install tiktoken``
- command to generate requirements.txt ``pip freeze > requirements.txt``

# To create new .venv using python 3.11 
    /opt/homebrew/bin/python3.11 -m venv .venv-py311 && .venv-py311/bin/python -m pip install --upgrade pip setuptools wheel && .venv-py311/bin/python -m pip install -r requirements.txt