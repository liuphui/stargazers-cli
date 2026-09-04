# Stargazers CLI
## Introduction
This repository contains code for a lightweight command-line tool written in Python. It allows users to discover the most-starred GitHub repositories for any programming language.

## Setup & Configuration
1. **Create a .env file in the project root**:
```bash
touch .env
```

2. **Add your GH token**:
```bash
GITHUB_TOKEN=github_pat_token
```

## Installation
1. **Clone the repository**:
```bash
git clone [https://github.com/liuphui/stargazers-cli.git](https://github.com/liuphui/stargazers-cli.git)
cd stargazers-cli
```

2. **Create and activate a virtual environment**:
```bash
python -m venv venv

# On Windows
venv/Scripts/activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install in editable mode**:
```bash
pip install -e .
```

## Usage
Run the CLI directly using the `stargazers` command. For example:
```bash
# Find top 10 Python repositories
stargazers --lang python

# Find top 5 Rust repositories
stargazers --lang rust --lim 5

# Find top 50 TypeScript repositories
stargazers --lang typescript --lim 50
```