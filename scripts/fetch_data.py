import mysql.connector
import json

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="yugioh_data_warehouse"
)

cursor = my_db.cursor()

cursor.execute("SELECT * FROM yugioh_booster")

result = cursor.fetchall()

rows = []

for row in result:
  row_dict = {
    'booster_id' : row[0],
    'booster_name' : row[1],
    'card_number' : row[2],
    'card_name' : row[3],
    'card_type' : row[4],
    'card_rarity' : row[5],
    'card_attribute' : row[6],
    'card_sub_type' : row[7],
    'card_level' : row[8],
    'card_attack': row[9],
    'card_defense' : row[10],
    'card_text' : row[11]
  }

  rows.append(row_dict)

print(json.dumps(rows))