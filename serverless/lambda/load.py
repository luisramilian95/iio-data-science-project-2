import os
import mysql.connector
import csv
import boto3

s3Client = boto3.client('s3')

sql = """INSERT INTO yugioh_booster 
    (booster_name, card_number, card_name, card_type, card_rarity, card_attribute, 
    card_sub_type,  card_level, card_attack, card_defense, card_text)  
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

db = mysql.connector.connect(
  host= os.environ['db_host'],
  user= os.environ['db_user'],
  password= os.environ['db_pass'],
  database=os.environ['db_name']
)

cursor = db.cursor()

def handler(event, context) :

    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']

        file_name = object_key.replace('+', ' ')

        print(bucket_name)
        print(file_name)

        booster_name = file_name.replace('dataset/yugioh_boosters - ', '')
        booster_name = booster_name.replace('.csv', '').strip()
        print(booster_name)
        
        cursor.execute(f"SELECT * FROM yugioh_booster where booster_name = '{booster_name}'")
        result = cursor.fetchall()

        if len(result) != 0 :
            continue
    
        data = s3Client.get_object(Bucket=bucket_name,  Key=file_name)['Body']
        data = data.read().decode('utf-8').splitlines()
        print(data)
        
        yugioh_data = csv.reader(data) 
        headers = next(yugioh_data) 
        print('headers: %s' % (headers)) 
        
        for row in yugioh_data: 

            card_number = None if row[1] == None else row[1].strip()
            card_name = None if row[2] == None else row[2].strip()

            card_type = None if row[3] == None else row[3].strip()
            card_rarity = None if row[4] == None else row[4].strip()
            card_attribute = None if row[5] == None else row[5].strip()
            card_sub_type = None if row[6] == None else row[6].strip()
            card_text = None if row[7] == None else row[7].strip()

            card_level =  '' if row[8] == None else row[8].strip()
            card_level = "-1" if card_level == '?' else card_level
            card_level = None if card_level == '' else int(float(card_level))

            card_attack = '' if row[9] == None else row[9].strip()
            card_attack = "-1" if card_attack == '?' else card_attack
            card_attack =   None if card_attack == '' else int(float(card_attack))

            card_defense = '' if row[10] == None else row[10].strip()
            card_defense = "-1" if card_defense == '?' else card_defense
            card_defense =  None if card_defense == '' else int(float(card_defense))
            
            val = (booster_name, card_number, card_name, card_type, card_rarity, card_attribute,
                card_sub_type, card_level, card_attack, card_defense, card_text)
                
            cursor.execute(sql, val)

        db.commit()