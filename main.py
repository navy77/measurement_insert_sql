import utils.constant as constant
import os

from utils.influx_to_sqlserver import INFLUX_TO_SQLSERVER

from dotenv import load_dotenv

load_dotenv()


try:

    influx_to_sqlserver = INFLUX_TO_SQLSERVER(
        server=os.getenv('SERVER'),
        database=os.getenv('DATABASE'),
        user_login=os.getenv('USER_LOGIN'),
        password=os.getenv('PASSWORD'),
        table=os.getenv('TABLE'),
        table_log=os.getenv('TABLE_LOG'),
        table_columns=os.getenv('TABLE_COLUMNS'),
        table_columns_log=os.getenv('TABLE_COLUMNS_LOG'),
        columns_init=os.getenv('COLUMNS_INIT'),
        initial_db=os.getenv('INITIAL_DB'),
        influx_server=os.getenv('INFLUX_SERVER'),
        influx_database=os.getenv('INFLUX_DATABASE'),
        influx_user_login=os.getenv('INFLUX_USER_LOGIN'),
        influx_password=os.getenv('INFLUX_PASSWORD'),
        influx_port=os.getenv('INFLUX_PORT'),
        mqtt_topic=os.getenv('MQTT_TOPIC'),

    )
    print
    # influx_to_sqlserver.run()

except Exception as e:
    print(e)
    