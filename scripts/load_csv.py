import os
import csv
import mysql.connector


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="yugioh_data_warehouse"
)

sql = """INSERT INTO yugioh_booster_1 
    (booster_name, card_number, card_name, card_type, card_rarity, card_attribute, 
    card_sub_type,  card_level, card_attack, card_defense, card_text)  
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

cursor = db.cursor()


def load_file(file_name, data):
    
    f = open(data, 'r')
    
    records = csv.reader(f) 

    headers = next(records) 
    print('headers: %s' % (headers)) 
    
    booster_name = file_name.replace('dataset/yugioh_boosters+-+', '')
    booster_name = booster_name.replace('+', ' ').strip()
    booster_name = booster_name.replace('csv', '').strip()
    print(booster_name)


    for record in records: 
       
        card_number = None if record[1] == None else record[1].strip()
        card_name = None if record[2] == None else record[2].strip()

        card_type = None if record[3] == None else record[3].strip()
        card_rarity = None if record[4] == None else record[4].strip()
        card_attribute = None if record[5] == None else record[5].strip()
        card_sub_type = None if record[6] == None else record[6].strip()
        card_text = None if record[7] == None else record[7].strip()

        card_level =  '' if record[8] == None else record[8].strip()
        print(card_level)
        card_level = "-1" if card_level == '?' else card_level
        card_level = None if card_level == '' else int(float(card_level))

        card_attack = '' if record[9] == None else record[9].strip()
        card_attack = "-1" if card_attack == '?' else card_attack
        card_attack =   None if card_attack == '' else int(float(card_attack))

        card_defense = '' if record[10] == None else record[10].strip()
        card_defense = "-1" if card_defense == '?' else card_defense
        card_defense =  None if card_defense == '' else int(float(card_defense))
         
        val = (booster_name, card_number, card_name, card_type, card_rarity, card_attribute,
               card_sub_type, card_level, card_attack, card_defense, card_text)

        cursor.execute(sql, val)

        db.commit()



load_file('dataset/yugioh_boosters+-++Absolute+Powerforce+5D1.csv', '../dataset/yugioh_boosters -  Absolute Powerforce 5D1.csv')