# Workflow 
1. download_engine.py
* calls construction.py -- DONE
* calls housing_indexes.py
* calls market_indexes.py
* calls commodities_indexes.py (oil, lumber, utilities)
* calls headlines.py (title, author, source, date)
* saves downloaded data in data/raw/...

1. cleaner_engine.py
* creates backup of yesterday in data/clean/backup/
* calls construction_cleaner.py
* calls housing_cleaner.py
* calls market_cleaner.py
* calls commodities_cleaner.py
* calls headlines_cleaner.py
* saves clean data in data/clean/...

1. digest_engine.py
* calls gather.py
* calls prepare.py
* calls send.py
