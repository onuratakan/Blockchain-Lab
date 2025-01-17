from setuptools import setup

setup(
    name="blockchain_lab",
    version="0.6.0",
    description="""A fully functional blockchain lab.""",
    long_description="""
# Blockchain Lab
A fully functional blockchain lab.

# Install
```
pip3 install blockchain_lab
```
# Using
## In another script
You can give these parameters in blockchain_lab()

- Node number with "node_number"
- Security circle number with "security_circle_number"
- Path with "path"

### Docker | Create & Delete
```python
from blockchain_lab import blockchain_lab

blockchain_lab().create_docker()
```
```python
from blockchain_lab import blockchain_lab

blockchain_lab().delete_docker()
```
### Local | Create & Delete
```python
from blockchain_lab import blockchain_lab

blockchain_lab().create_local()
```
```python
from blockchain_lab import blockchain_lab

blockchain_lab().delete_local()
```
### Status
```python
from blockchain_lab import blockchain_lab

blockchain_lab.status()
```
### Test with a transaction
```python
from blockchain_lab import blockchain_lab

blockchain_lab.send_transaction(receiver = "decentra-network", amount = 5000, data = "blockchain-lab")
```


## In command line
You can give these parameters in command line arguments of
create and delete functions.

- Node number with "-nn" or "--nodenumber"
- Security circle number with "-scn" or "--securitycirclenumber"
- Path with "-p" or "--path"
### Docker | Create & Delete
```console
blockchain_lab_create_docker
```
```console
blockchain_lab_delete_docker
```
### Local | Create & Delete
```console
blockchain_lab_create_local
```
```console
blockchain_lab_delete_local
```
### Status
```console
blockchain_lab_status
```
### Test with a transaction
```console
blockchain_lab_send_transaction -r decentra-network -a 5000 -d blockchain-lab
```

""",
    long_description_content_type="text/markdown",
    url="https://github.com/Decentra-Network/Blockchain-Lab",
    author="Decentra Network Developers",
    author_email="onur@decentranetwork.org",
    license="MPL-2.0",
    packages=["blockchain_lab"],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "blockchain_lab_create_docker=blockchain_lab.blockchain_lab:blockchain_lab_create_docker",
            "blockchain_lab_create_local=blockchain_lab.blockchain_lab:blockchain_lab_create_local",
            "blockchain_lab_delete_docker=blockchain_lab.blockchain_lab:blockchain_lab_delete_docker",
            "blockchain_lab_delete_local=blockchain_lab.blockchain_lab:blockchain_lab_delete_local",
            "blockchain_lab_status=blockchain_lab.blockchain_lab:blockchain_lab.status",
            "blockchain_lab_send_transaction=blockchain_lab.blockchain_lab:blockchain_lab_send_transaction",
        ],
    },
    python_requires=">=3.6",
    zip_safe=False,
)
