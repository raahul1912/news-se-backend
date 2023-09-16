## News Search Backend

### News API Key Setup
  1. go to https://gnews.io 
  2. create an account and verify email 
  3. get api key

### Environment Setup 
create a .env file with
    add news api key in .env file 

### Virtual Environment Setup
create an virtualenv 
    virtualenv -p python3 news_app_env
    
activate virtualenv 
    source news_app_env/bin/activate

### Install required packages 
    pip install -r requirements.txt

### Start Application
application will run on 5000 port in debug mode 
    python main.py
