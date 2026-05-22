# Stable Protocol Indexer v3 (Multicollateral)

### Warning: This is only for version 3 of the main contracts. 

| Project              | Version | V3 | 
|----------------------|---------|----|
| MOC (Money on Chain) | V1      | ❌  |
| ROC (RIF on Chain)   | V3      | ✅  |


## Introduction

To speed up the dapp we need an indexer of the blockchain of our contracts. 
This service is required to display operations in the dapp.  The indexer query the status of the contracts and write to mongo database, so the app query the mongo instead of blockchain (slow).

### Jobs

 1. **Scan Raw TX**: Indexing blocks
 2. **Scan Events**: Indexing events transactions
 3. **Scan TX Status**: Scan transaction status
 4. **Scan Blocks not processed**
 5. **Scan Blocks confirming**
 

### Requirements

* Mongo db
* Python installed

### Usage

**Requirement and installation**
 
* We need Python <= 3.10
* Is not compatible with version 3.11 & 3.12!

Install libraries

`pip install -r requirements.txt`

**Usage**

Select settings from settings/ and copy to ./config.json also change url, db uri and db name. 

**Run**

`python ./app_run_indexer.py `


### Docker (Recommended)

Build, change path to correct environment

```
docker build -t stable_protocol_indexer -f Dockerfile --build-arg CONFIG=./settings/staging/flipmoney-testnet/config.json .
```

Run

```
docker run -d \
--name stable_protocol_indexer_moc_mainnet \
--env APP_MONGO_URI=mongodb://localhost:27017 \
--env APP_MONGO_DB=roc_mainnet \
--env APP_CONNECTION_URI=https://public-node.testnet.rsk.co \
stable_protocol_indexer
```

**Note on multicollateral & using task runner settings:**

in config:

```
"contracts_white_list": [
    "0xeD74d959A38866fCD280E8ADcF30b9BbeA971112"
  ],
```

we need to whitelist the address of task runner proxy
