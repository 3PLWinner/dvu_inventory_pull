# DVU Inventory Pull
This is the script that will be used to pull from DVU's db to determine storage over the course of the day.

## Table of Contents

-[Installation](#installation)
-[Usage](#usage)


## Installation 

Clone the repo:
```bash
git clone https://github.com/3PLWinner/dvu_inventory_pull.git
```



## Usage
1. Create and activate a virtual environment:
```bash
python -m venv yourenv
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Execute from the command line:
```bash
python ./dvu_inventory_pull.py
```