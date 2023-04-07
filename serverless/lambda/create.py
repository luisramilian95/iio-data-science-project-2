import os, json
import mysql.connector



sql = """ create table yugioh_booster(
    booster_id int primary key auto_increment,
    booster_name varchar(100),
    card_number varchar(100), 
    card_name varchar(200),
    card_type varchar(100),
    card_rarity varchar(100),
    card_rarity_1 varchar(100),
    card_attribute varchar(10),
    card_sub_type varchar(100), 
    card_level int, 
    card_attack int, 
    card_defense int, 
    card_text text
)
"""



def handler(event, context):

    db = mysql.connector.connect(
        host= os.environ['db_host'],
        user= os.environ['db_user'],
        password= os.environ['db_pass'],
        database=os.environ['db_name']
    )

    cursor = db.cursor()
    cursor.execute(sql)

    body = {
        "message": "database created successfully",
    }

    return {"statusCode": 200, "body": json.dumps(body)}