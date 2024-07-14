insert into way values ('1', 'Разрушение'); 
insert into way values ('2', 'Охота');
insert into way values ('3', 'Эрудиция');
insert into way values ('4', 'Гармония');
insert into way values ('5', 'Небытие');
insert into way values ('6', 'Сохранение'); 
insert into way values ('7', 'Изобилие');

insert into character values (1, 'Блейд', 5, 'Ветряной', 1);
insert into character values (2, 'Жуань Мэй', 5, 'Ледяной', 4);
insert into character values (3, 'Дань Хэн: Пожиратель Луны', 5, 'Мнимый', 1);
insert into character values (4, 'Яньцин', 5, 'Ледяной', 2);
insert into character values (5, 'Лоча', 5, 'Мнимый', 7);
insert into character values (6, 'Гепард', 5, 'Ледяной', 6);
insert into character values (7, 'Вельт', 5, 'Мнимый', 5);
insert into character values (8, 'Цинцюэ', 4, 'Квантовый', 3);
insert into character values (9, 'Сушан', 4, 'Физический', 2);
insert into character values (10, 'Тинъюнь', 4, 'Электрический', 4);
insert into character values (11, 'Гуйнайфэнь', 4, 'Огненный', 5);


insert into weapon values (1, 'Недоступная сторона', 5, 1);
insert into weapon values (2, 'Ярче солнца', 5, 1);
insert into weapon values (3, 'Тайная клятва', 4, 1);
insert into weapon values (4, 'Отражение прошлой меня', 5, 4);
insert into weapon values (5, 'Воспоминания о прошлом(S5)', 4, 4);
insert into weapon values (6, 'Сцепленные шестерни(S5)', 3, 4);
insert into weapon values (7, 'Отныне я сама буду мечом', 5, 1);
insert into weapon values (8, 'О падении эона', 5, 1);
insert into weapon values (9, 'В ночи', 5, 2);
insert into weapon values (10, 'Крещение чистой мысли', 5, 2);
insert into weapon values (11, 'Мертвецкий сон', 5, 2);
insert into weapon values (12, 'Эхо из гроба', 5, 7);
insert into weapon values (13, 'Ночь страха', 5, 7);
insert into weapon values (14, 'Беседа после операции', 4, 7);
insert into weapon values (15, 'Момент победы', 5, 6);
insert into weapon values (16, 'Материя памяти', 5, 6);
insert into weapon values (17, 'Первый день моей новой жизни', 4, 6);
insert into weapon values (18, 'Во имя мира', 5, 5);
insert into weapon values (19, 'Непрекращающийся дождь', 5, 5);
insert into weapon values (20, 'Спокойной ночи и мирного сна', 4, 5);
insert into weapon values (21, 'До рассвета', 5, 3);
insert into weapon values (22, 'Остановись, мгновение', 5, 3);
insert into weapon values (23, 'Сегодня тоже мирный день', 4, 3);
insert into weapon values (24, 'Фехтование', 4, 2);
insert into weapon values (25, 'Битва не окончена', 5, 4);
insert into weapon values (26, 'Танцуй! Танцуй! Танцуй!', 4, 4);
insert into weapon values (27, 'Взгляд жертвы', 4, 5);



insert into character_weapon values (1, 1);
insert into character_weapon values (1, 2);
insert into character_weapon values (1, 3);
insert into character_weapon values (2, 4);
insert into character_weapon values (2, 5);
insert into character_weapon values (2, 6);
insert into character_weapon values (3, 2);
insert into character_weapon values (3, 7);
insert into character_weapon values (3, 8);
insert into character_weapon values (4, 9);
insert into character_weapon values (4, 10);
insert into character_weapon values (4, 11);
insert into character_weapon values (5, 12);
insert into character_weapon values (5, 13);
insert into character_weapon values (5, 14);
insert into character_weapon values (6, 15);
insert into character_weapon values (6, 16);
insert into character_weapon values (6, 17);
insert into character_weapon values (7, 18);
insert into character_weapon values (7, 19);
insert into character_weapon values (7, 20);
insert into character_weapon values (8, 21);
insert into character_weapon values (8, 22);
insert into character_weapon values (8, 23);
insert into character_weapon values (9, 24);
insert into character_weapon values (9, 9);
insert into character_weapon values (9, 11);
insert into character_weapon values (10, 25);
insert into character_weapon values (10, 26);
insert into character_weapon values (10, 5);
insert into character_weapon values (11, 20);
insert into character_weapon values (11, 18);
insert into character_weapon values (11, 27);


insert into relic values (1, 'Долгоживущий ученик', 'Повышает макс. HP на 12%.', 'Повышает крит. шанс владельца на 8% на 2 хода, когда тот атакован или расходует HP. Эффект складывается до 2 раз. При складывании число ходов для эффекта не увеличивается.');
insert into relic values (2, 'Первооткрыватель мертвых вод', 'Повышает урон, наносимый противникам с ослаблениями, на 12%.', 'Повышает крит. шанс на 4%. Крит. урон владельца, наносимый противникам с не менее, чем 2/3 ослаблениями, повышается на 8%/12% соответственно. После того как владелец накладывает ослабление на противника, указанные выше эффекты повышаются на 100% на 1 ход.');
insert into relic values (3, 'Вор падающего метеора', 'Повышает эффект пробития на 16%.', 'Дополнительно повышает эффект пробития на 16%. Восстанавливает 3 единицы энергии после пробития вражеской уязвимости.');
insert into relic values (4, 'Часовщик сонных махинаций', 'Повышает эффект пробития на 16%.', 'Использование сверхспособности владельца повышает эффект пробития всех союзников на 30% на 2 хода. Этот эффект не может складываться.');
insert into relic values (5, 'Стрелок дикой пшеницы', 'Повышает силу атаки на 12%.', 'Повышает скорость владельца на 6%, а также урон его базовой атаки на 10%.');
insert into relic values (6, 'Охотник ледникового леса', 'Повышает ледяной урон на 10%.', 'При использовании сверхспособности повышает крит. урон на 25% на 2 хода.');
insert into relic values (7, 'Скиталец блуждающего облака', 'Исходящее исцеление +10%.', 'В начале боя моментально восстанавливает 1 очко навыков всем членам отряда.');
insert into relic values (8, 'Рыцарь дворца чистоты', 'Повышает защиту на 15%.', 'Повышает владельцу поглощаемый щитом урон на 20%.');
insert into relic values (9, 'Страж снежной метели', 'Снижает получаемый урон на 8%.', 'В начале хода, если значение HP владельца ниже или равно 50%, немедленно восстанавливает 8% здоровья и 5 ед. энергии.');
insert into relic values (10, 'Головорез бандитской пустыни', 'Повышает мнимый урон на 10%.', 'Когда владелец наносит урон противнику с ослаблениями, его крит. шанс повышается на 10%, а когда владелец наносит урон противнику со статусом Заключение, его крит. урон повышается на 20%.');
insert into relic values (11, 'Гений бриллиантовых звезд', 'Квантовый урон +10%.', 'Когда владелец наносит урон выбранному противнику, игнорирует 10% защиты. Если у выбранного противника есть квантовая уязвимость, владелец дополнительно игнорирует 10% защиты.');
insert into relic values (12, 'Чемпион уличного бокса', 'Физический урон +10%.', 'После совершения атаки или получения урона к силе атаки +5% до конца битвы. Складывается до 5 раз.');
insert into relic values (13, 'Вестник, блуждающий в хакерском пространстве', 'Повышают скорость на 6%.', 'Повышает скорость всех союзников на 12%, когда владелец применяет сверхспособность к союзнику, на 1 ход. Эффект не складывается.');
insert into relic values (14, 'Пленник мрачной темницы', 'Повышает силу атаки на 12%.', 'За каждый имеющийся у противника эффект с периодическим уроном (до макс. 3) при нанесении урона владелец игнорирует 6% от защиты этого противника.');
						  
						  
						  
insert into planet_jewelry values (1, 'Звездистая арена', 'Повышает крит. шанс на 8%. Если крит. шанс владельца выше или равен 70%, урон его базовой атаки и навыка повышается на 20%.');
insert into planet_jewelry values (2, 'Замершее Салсотто', 'Повышает крит. шанс на 8%. Если крит. шанс владельца выше или равен 50%, урон его сверхспособности и бонус-атаки повышается на 15%.');
insert into planet_jewelry values (3, 'Флот нестареющих', 'Повышает HP на 12%. Когда скорость достигает 120 единиц и выше, все союзники получают бонус к силе атаки 8%.');
insert into planet_jewelry values (4, 'Сломанный киль', 'Повышает сопротивление эффектам на 10%. Если сопротивление эффектам владельца выше или равно 30%, крит. урон всех союзников повышается на 10%.');
insert into planet_jewelry values (5, 'Запечатывающая космос станция', 'Повышает силу атаки на 12%. Если скорость владельца выше или равна 120 ед., то его сила атаки дополнительно повышается на 12%.');
insert into planet_jewelry values (6, 'Небесный фронт Глатирамер', 'Повышает силу атаки владельца на 12%. Если скорость владельца выше или равна 135/160 ед., то наносимый им урон повышается на 12%/18%.');
insert into planet_jewelry values (7, 'Белобог Архитекторов', 'Повышает защиту владельца на 15%. Если шанс попадания эффектов владельца равен 50% или выше, защита дополнительно повышается на 15%.');
insert into planet_jewelry values (8, 'Пангалактическое коммерческое предприятие', 'Повышает шанс попадания эффектов владельца на 10%. Помимо этого, повышает силу атаки владельца на 25% от текущего шанса попадания эффектов, максимум на 25%.');
								   
								   
								   

insert into character_relic values (1, 1);	
insert into character_relic values (1, 2);
insert into character_relic values (2, 3);
insert into character_relic values (2, 4);
insert into character_relic values (3, 2);
insert into character_relic values (3, 5);
insert into character_relic values (4, 5);
insert into character_relic values (4, 6);
insert into character_relic values (5, 5);
insert into character_relic values (5, 7);
insert into character_relic values (6, 8);
insert into character_relic values (6, 9);
insert into character_relic values (7, 2);
insert into character_relic values (7, 10);
insert into character_relic values (8, 2);
insert into character_relic values (8, 11);
insert into character_relic values (9, 2);
insert into character_relic values (9, 12);
insert into character_relic values (10, 5);
insert into character_relic values (10, 13);
insert into character_relic values (11, 5);
insert into character_relic values (11, 14);




insert into character_jewelry values (1, 1);
insert into character_jewelry values (1, 2);
insert into character_jewelry values (2, 3);
insert into character_jewelry values (2, 4);
insert into character_jewelry values (3, 1);
insert into character_jewelry values (3, 5);
insert into character_jewelry values (4, 1);
insert into character_jewelry values (4, 6);
insert into character_jewelry values (5, 3);
insert into character_jewelry values (5, 4);
insert into character_jewelry values (6, 4);
insert into character_jewelry values (6, 7);
insert into character_jewelry values (7, 5);
insert into character_jewelry values (7, 8);
insert into character_jewelry values (8, 1);
insert into character_jewelry values (8, 6);
insert into character_jewelry values (9, 1);
insert into character_jewelry values (9, 5);
insert into character_jewelry values (10, 3);
insert into character_jewelry values (10, 4);
insert into character_jewelry values (11, 5);
insert into character_jewelry values (11, 8);

ALTER TABLE tg_users ALTER COLUMN tg_id TYPE BIGINT;

insert into tg_users values (121313, 'ArmashMarina', 'admin');
insert into tg_users values (386297131, 'weirdlyggg', 'admin');

UPDATE tg_users
SET tg_username = 'weirdlyggg', tg_rolename = 'superuser'
WHERE tg_id = 386297131;


