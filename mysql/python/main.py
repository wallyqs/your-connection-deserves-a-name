from datetime import datetime
import time
import pymysql.cursors


def output(message:str):
    now = datetime.now()
    time = now.strftime("%Y/%m/%d %H:%M:%S")
    print(f"{time} {message}")


mysql_host = '127.0.0.1'
mysql_username = 'root'
mysql_password = 'secret'
mysql_database = 'dummy'
connection_name = "unit-conversion-app"

# Building the connection
dsn = f"mysql://{mysql_username}:{mysql_password}@{mysql_host}/{mysql_database}"
output(f"Connecting to MySQL on {dsn}");

connection = pymysql.connect(host=mysql_host,
                             user=mysql_username,
                             password=mysql_password,
                             database=mysql_database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             program_name=connection_name)

with connection:
    with connection.cursor() as cursor:
        # Do a "kind of" PING statement to build up the connection
        sql = "SELECT 1"
        cursor.execute(sql)

    # connection is not autocommit by default.
    # So you must commit to save your changes.
    connection.commit()
    output(f"Connecting to MySQL on {dsn}  ... Successful");

    output("")
    output("Keeping the connection open ...")
    output("You can connect to the PostgreSQL database and execute the query:")
    output("	SELECT")
    output("	    session_connect_attrs.ATTR_VALUE AS program_name,")
    output("	    processlist.*")
    output("	FROM information_schema.processlist")
    output("	LEFT JOIN  performance_schema.session_connect_attrs ON (")
    output("	    processlist.ID = session_connect_attrs.PROCESSLIST_ID")
    output("	    AND session_connect_attrs.ATTR_NAME = \"program_name\"")
    output("	)")
    output("Hit CTRL + C or cancel the process to stop.")
    output("")

    # Just looping to keep the process running.
    # In detail we do not keep the connection active, but rely on the standard timeout.
    # This way we provide time for the user to check the connection name behaviour.
    with connection.cursor() as cursor:
        while True:
            sql = "SELECT 1"
            cursor.execute(sql)
            time.sleep(5)
