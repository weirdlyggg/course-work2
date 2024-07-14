from telebot import *
from dbService import *

token = "7021958106:AAG7GmAzO1Flc2UJ14FTHv3AC6aAYnOgj0w"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    addUserIfAbsent(message.from_user.id, message.from_user.username)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Поиск по персонажу", callback_data='search_way'))
    markup.add(types.InlineKeyboardButton("Поиск по оружию", callback_data='search_weapon_by_way'))
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'search_way')
def search_way_handler(call):
    show_ways(call.message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == 'search_weapon_by_way')
def search_weapon_by_way_handler(call):
    show_weapon_ways(call.message.chat.id)


def show_weapon_ways(chat_id):
    markup = types.InlineKeyboardMarkup()
    for way_id, way_name in getWays():
        markup.add(types.InlineKeyboardButton(way_name, callback_data=f'weapon_way_{way_id}'))
    bot.send_message(chat_id, "Выберите путь:", reply_markup=markup)


def show_ways(chat_id):
    markup = types.InlineKeyboardMarkup()
    for way_id, way_name in getWays():
        markup.add(types.InlineKeyboardButton(way_name, callback_data=f'way_{way_id}'))
    bot.send_message(chat_id, "Выберите путь:", reply_markup=markup)


@bot.message_handler(commands=['admin'])
def admin_first_message(message):
    markup = types.InlineKeyboardMarkup()
    userrole = getUserRole(message.from_user.id)
    if userrole == 'admin' or userrole == 'superuser':
        markup.add(types.InlineKeyboardButton("Изменение роли пользователя", callback_data='new_rolename'))
        markup.add(types.InlineKeyboardButton("Добавление новых оружий", callback_data='new_weapon'))
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "У вас нет прав админа")


@bot.callback_query_handler(func=lambda call: call.data == 'new_rolename')
def admin_message(call):
    markup = types.InlineKeyboardMarkup()
    userrole = getUserRole(call.from_user.id)
    if userrole == 'admin' or userrole == 'superuser':
        for (username, rolename) in getUsersExceptSuperUser():
            markup.add(types.InlineKeyboardButton(username + " " + rolename, callback_data=f'chose_{username}'))
        bot.send_message(call.message.chat.id, "Изменить права этих пользователей:", reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, "У вас нет прав админа")


@bot.callback_query_handler(func=lambda call: call.data == 'new_weapon')
def add_weapon_command(call):
    if getUserRole(call.from_user.id) == 'admin' or 'superuser':
        bot.send_message(call.message.chat.id, "Введите название нового оружия:")
        bot.register_next_step_handler(call.message, get_weapon_name)
    else:
        bot.send_message(call.message.chat.id, "У вас нет прав для выполнения этой команды.")


weapon_data = {}


def get_weapon_name(message):
    weapon_data['name'] = message.text
    bot.send_message(message.chat.id, "Введите количество звезд для этого оружия:")
    bot.register_next_step_handler(message, get_weapon_stars)


def get_weapon_stars(message):
    try:
        weapon_data['stars'] = int(message.text)
        bot.send_message(message.chat.id, "Введите ID пути для этого оружия:")
        bot.register_next_step_handler(message, get_way_id)
    except ValueError:
        bot.send_message(message.chat.id, "Количество звезд должно быть числом. Попробуйте снова:")
        bot.register_next_step_handler(message, get_weapon_stars)


def get_way_id(message):
    try:
        weapon_data['way_id'] = int(message.text)
        weapon_id = addWeaponToDb(weapon_data['name'], weapon_data['stars'], weapon_data['way_id'])
        bot.send_message(message.chat.id, "Оружие добавлено. Введите ID персонажей, для которых оно подходит, через запятую:")
        bot.register_next_step_handler(message, process_character_ids_for_link, weapon_id)
    except ValueError:
        bot.send_message(message.chat.id, "ID пути должно быть числом. Попробуйте снова:")
        bot.register_next_step_handler(message, get_way_id)


def process_character_ids_for_link(message, weapon_id):
    character_ids = message.text.split(',')
    for c_id in character_ids:
        try:
            c_id = int(c_id.strip())
            linkWeaponToCharacter(c_id, weapon_id)
        except ValueError:
            bot.send_message(message.chat.id, f"ID персонажа {c_id} должно быть числом. Связь не установлена.")
    bot.send_message(message.chat.id, f"Оружие {weapon_data['name']} успешно связано с указанными персонажами.")


@bot.callback_query_handler(func=lambda call: call.data.startswith('way_'))
def query_handler(call):
    way_id = call.data.split('_')[1]
    markup = types.InlineKeyboardMarkup()
    for (c_name,) in getCharacter(way_id):
        markup.add(types.InlineKeyboardButton(c_name, callback_data=f'character_{c_name}'))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите персонажа:",
                          reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('weapon_way_'))
def weapon_query_handler(call):
    way_id = call.data.split('_')[2]
    weapons = getWeaponsByWayId(way_id)
    if weapons:
        markup = types.InlineKeyboardMarkup()
        for w_id, w_name, w_stars in weapons:
            markup.add(types.InlineKeyboardButton(f"{w_name}, {w_stars} звёзд", callback_data=f'weapon_{w_id}'))
        bot.send_message(call.message.chat.id, "Выберите оружие:", reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, "Оружие не найдено для данного пути.")


@bot.callback_query_handler(func=lambda call: call.data.startswith('weapon_'))
def weapon_handler(call):
    w_id = call.data.split('_')[1]
    characters = getCharactersByWeaponId(w_id)
    if characters:
        markup = types.InlineKeyboardMarkup()
        for c_id, c_name in characters:
            markup.add(types.InlineKeyboardButton(c_name, callback_data=f'character_{c_name}'))
        bot.send_message(call.message.chat.id, "Выберите персонажа:", reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, "Персонажи не найдены для данного оружия.")


@bot.callback_query_handler(func=lambda call: call.data.startswith('character_'))
def character_handler(call):
    c_name = call.data.split('_')[1]
    character_info = getCharacterInfo(c_name)
    if character_info:
        c_id, name, stars, damage_type = character_info
        addUserSearchHistory(call.from_user.id, c_name)
        info_message = f"<b><i>Имя персонажа:</i></b> {name}\n<b><i>Редкость:</i></b> {stars} звёзд\n<b><i>Тип урона:</i></b> {damage_type}\n"
        info_message += f'\n\n<b><i>Подходящие оружия:</i></b>\n\n'

        weapons = getWeaponsByCharacterId(c_id)
        if weapons:
            for w_name, w_stars in weapons:
                info_message += f"<b>*</b> {w_name}, {w_stars} звёзд\n"
        else:
            info_message += "Оружие не найдено."

        info_message += f'\n\n<b><i>Реликвии:</i></b>\n\n'

        relic = getRelicByCharacterId(c_id)
        if relic:
            for r_id, r_name, r_2_parts_effects, r_4_parts_effects in relic:
                info_message += f'<b>{r_name}</b>\n<b>2 части:</b> {r_2_parts_effects}\n<b>4 части:</b> {r_4_parts_effects}\n\n'
        else:
            info_message += "Реликвии не найдены."

        info_message += f'\n\n<b><i>Планетарные украшения:</i></b>\n\n'

        jewelry = getJewelryByCharacterId(c_id)
        if jewelry:
            for pj_id, pj_name, pj_effect in jewelry:
                info_message += f'<b>{pj_name}</b>\n<b>2 части:</b> {pj_effect}\n\n'
        else:
            info_message += "Планетарные украшения не найдены."

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("История запросов", callback_data='search_history'))

        bot.send_message(call.message.chat.id, info_message, parse_mode='HTML', reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, "Информация о персонаже не найдена.")


@bot.message_handler(func=lambda message: True)
def search_character(message):
    c_name = message.text.strip()
    character_info = getCharacterInfo(c_name)

    if character_info:
        c_id, name, stars, damage_type = character_info
        addUserSearchHistory(message.from_user.id, c_name)
        info_message = f"<b><i>Имя персонажа:</i></b> {name}\n<b><i>Редкость:</i></b> {stars} звёзд\n<b><i>Тип урона:</i></b> {damage_type}\n"
        info_message += f'\n\n<b><i>Подходящие оружия:</i></b>\n\n'

        weapons = getWeaponsByCharacterId(c_id)
        if weapons:
            for w_name, w_stars in weapons:
                info_message += f"<b>*</b> {w_name}, {w_stars} звёзд\n"
        else:
            info_message += "Оружие не найдено."

        info_message += f'\n\n<b><i>Реликвии:</i></b>\n\n'

        relic = getRelicByCharacterId(c_id)
        if relic:
            for r_id, r_name, r_2_parts_effects, r_4_parts_effects in relic:
                info_message += f'<b>{r_name}</b>\n<b>2 части:</b> {r_2_parts_effects}\n<b>4 части:</b> {r_4_parts_effects}\n\n'
        else:
            info_message += "Реликвии не найдены."

        info_message += f'\n\n<b><i>Планетарные украшения:</i></b>\n\n'

        jewelry = getJewelryByCharacterId(c_id)
        if jewelry:
            for pj_id, pj_name, pj_effect in jewelry:
                info_message += f'<b>{pj_name}</b>\n<b>2 части:</b> {pj_effect}\n\n'
        else:
            info_message += "Планетарные украшения не найдены."

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("История запросов", callback_data='search_history'))

        bot.send_message(message.chat.id, info_message, parse_mode='HTML', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         "Персонаж не найден. Повторите попытку или воспользуйтесь поиском по кнопкам.")


@bot.callback_query_handler(func=lambda call: call.data == 'search_history')
def search_history_handler(call):
    search_history = getUserSearchHistory(call.from_user.id)
    if search_history:
        markup = types.InlineKeyboardMarkup()
        for c_name in search_history:
            markup.add(types.InlineKeyboardButton(c_name, callback_data=f'character_{c_name}'))
        bot.send_message(call.message.chat.id, "Ваши последние запросы:", reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, "История запросов пуста.")


@bot.callback_query_handler(func=lambda call: call.data.startswith('chose_'))
def choose_to_change(call):
    markup = types.InlineKeyboardMarkup()
    username = call.data[6:]
    markup.add(
        types.InlineKeyboardButton("Сделать админом", callback_data='change_to_admin_' + username),
        types.InlineKeyboardButton("Сделать юзером", callback_data='change_to_user_' + username)
    )
    bot.send_message(call.message.chat.id, "На что поменять текущую роль пользователя?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('change_'))
def change(call):
    if 'admin' in call.data:
        changeRolename(call.data[16:], 'admin')
    else:
        changeRolename(call.data[15:], 'user')
    bot.send_message(call.message.chat.id, "Вы успешно поменяли роль выбранного пользовтеля!")


bot.polling()
