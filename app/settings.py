from decouple import config

db_name = config('DB_NAME')
db_password = config('DB_PASSWORD')
db_port = config('DB_PORT')
db_user = config('DB_USER')
db_host = config('DB_HOST')

db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

