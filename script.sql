create database yugioh_data_warehouse;
use yugioh_data_warehouse;

create table yugioh_booster(
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
);