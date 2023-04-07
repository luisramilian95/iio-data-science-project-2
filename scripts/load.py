import os
import pandas as pd  
import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="yugioh_data_warehouse"
)

sql = """INSERT INTO yugioh_booster 
    (booster_name, card_number, card_name, card_type, card_rarity, card_attribute, 
    card_sub_type,  card_level, card_attack, card_defense, card_text)  
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

cursor = my_db.cursor()


def load_file(file_name):

    if not file_name.endswith('csv'):
        return

    dataset = pd.read_csv('./dataset/'+file_name)
    dataset = dataset.rename(columns=lambda name: name.lstrip().rstrip())
    dataset = dataset.fillna('')


    booster_name = file_name.replace('yugioh_boosters - ', '')
    booster_name = booster_name.replace('csv', '').strip()
    print(booster_name)


    for index, row in dataset.iterrows():

        card_number = row['Card #'].strip()
        card_name = row['Card Name'].strip()

        card_type = row['Type'].strip()
        card_rarity = row['Rarity'].strip()
        card_attribute = row['Attribute'].strip()
        card_sub_type = row['Sub Type'].strip()
        card_text = row['Card Text'].strip()

        card_level = str(row['Level']).strip()
        card_level = "-1" if card_level == '?' else card_level
        card_level = None if card_level == '' else int(float(card_level))

        card_attack = str(row['ATK']).strip()
        card_attack = "-1" if card_attack == '?' else card_attack
        card_attack =   None if card_attack == '' else int(float(card_attack))

        card_defense = str(row['DEF']).strip()
        card_defense = "-1" if card_defense == '?' else card_defense
        card_defense =  None if card_defense == '' else int(float(card_defense))
         
        val = (booster_name, card_number, card_name, card_type, card_rarity, card_attribute,
               card_sub_type, card_level, card_attack, card_defense, card_text)

        cursor.execute(sql, val)

    my_db.commit()
  

files = os.listdir('./dataset')    

for file_name in files:
    load_file(file_name)

