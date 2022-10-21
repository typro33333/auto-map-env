# Auto map enviroment varibles to file configmap k8s.
### Requirements:
- Already install python version 3.
- Upgrade pip3 version.
- Install package in requirements.

### How to run:
1. Create env python package.
```
python3 -m venv env
```
2. Access to env python to install package.
```bash
source env/bin/active
pip install -r 
```
3. Create file input like `yaml, properties, etc...`
4. Run comman to map env
```bash
python3 main.py [input file] [output file] -options
```
5. List options on feature.
- Options: `-s` will map with secret map.

### Issue:
- Map secret key not work clearly.