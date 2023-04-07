import os
import mysql.connector
import json

db = mysql.connector.connect(
  host= os.environ['db_host'],
  user= os.environ['db_user'],
  password= os.environ['db_pass'],
  database=os.environ['db_name']
)

def handler(event, context):

  cursor = db.cursor()
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
      
      'card_attribute' : row[7],
      'card_sub_type' : row[8],
      
      'card_level' : row[9],
      'card_attack': row[10],
      'card_defense' : row[11],
      'card_text' : row[12]
    }

    rows.append(row_dict)

  return {"statusCode": 200, "body": json.dumps(rows)}
