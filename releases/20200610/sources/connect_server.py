import mysql
import config

mydb = mysql.connector.connect(
  host=config.host,
  port=config.port,
  user=config.user,
  password=config.password,
)