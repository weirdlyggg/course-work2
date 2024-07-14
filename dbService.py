from peewee import *


connection = PostgresqlDatabase(
    'honkai-star-rail',
    user='postgres',
    password='postgres',
    host='localhost',
    port=5434
)


def getWays():
    cursor = connection.cursor()
    cursor.execute("SELECT way_id, way_name FROM way")
    results = cursor.fetchall()
    cursor.close()
    return results


def getCharacter(way_id):
    cursor = connection.cursor()
    cursor.execute("SELECT c_name FROM character WHERE way_id = %s", (way_id,))
    results = cursor.fetchall()
    cursor.close()
    return results


def getCharacterInfo(c_name):
    cursor = connection.cursor()
    cursor.execute("SELECT c_id, c_name, c_stars, c_damage_type FROM character WHERE LOWER(c_name) = LOWER(%s)", (c_name,))
    result = cursor.fetchone()
    cursor.close()
    return result


def getWeaponsByWayId(way_id):
    cursor = connection.cursor()
    cursor.execute("SELECT w_id, w_name, w_stars FROM weapon WHERE way_id = %s", (way_id,))
    results = cursor.fetchall()
    cursor.close()
    return results


def getCharactersByWeaponId(w_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT c.c_id, c.c_name
        FROM character c
        JOIN character_weapon cw ON c.c_id = cw.c_id
        WHERE cw.w_id = %s
    """, (w_id,))
    results = cursor.fetchall()
    cursor.close()
    return results


def getWeaponsByCharacterId(c_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT w.w_name, w.w_stars
        FROM weapon w
        JOIN character_weapon cw ON w.w_id = cw.w_id
        WHERE cw.c_id = %s
    """, (c_id,))
    results = cursor.fetchall()
    cursor.close()
    return results


def addUserIfAbsent(tg_id, tg_username):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM tg_users WHERE tg_id = %s
    """, (tg_id,))
    if len(cursor.fetchall()) == 0:
        cursor.execute("""
            INSERT INTO tg_users
            VALUES (%s, %s, 'user')
        """, (tg_id, tg_username))
        connection.commit()
    cursor.close()


def getUserRole(tg_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT tg_rolename FROM tg_users 
        WHERE tg_id = %s
    """, (tg_id,))
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        return "no role"
    else:
        return str(*result)


def changeRolename(tg_username, tg_rolename):
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE tg_users
        SET tg_rolename = %s
        WHERE tg_username = %s
    """, (tg_rolename, tg_username))
    cursor.close()


def getUsersExceptSuperUser():
    cursor = connection.cursor()
    cursor.execute("""
        SELECT tg_username, tg_rolename 
        FROM tg_users
        WHERE tg_rolename != 'superuser'
    """)
    result = cursor.fetchall()
    return result


def getRelicByCharacterId(c_id):
    cursor = connection.cursor()
    cursor.execute("""SELECT r.r_id, r.r_name, r.r_2_parts_effects, r.r_4_parts_effects 
        FROM relic r 
        JOIN character_relic cr ON r.r_id = cr.r_id
        JOIN character c ON c.c_id = cr.c_id
        WHERE cr.c_id = %s
    """, (c_id,))
    results = cursor.fetchall()
    cursor.close()
    return results


def getJewelryByCharacterId(c_id):
    cursor = connection.cursor()
    cursor.execute("""SELECT pj.pj_id, pj.pj_name, pj.pj_effect
        FROM planet_jewelry pj
        JOIN character_jewelry cj ON pj.pj_id = cj.pj_id
        JOIN character c ON c.c_id = cj.c_id
        WHERE cj.c_id = %s
    """, (c_id,))
    results = cursor.fetchall()
    cursor.close()
    return results


def getNextWeaponId():
    cursor = connection.cursor()
    cursor.execute("SELECT COALESCE(MAX(w_id), 0) + 1 FROM weapon")
    next_id = cursor.fetchone()[0]
    cursor.close()
    return next_id


def addWeaponToDb(weapon_name, weapon_stars, way_id):
    next_w_id = getNextWeaponId()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO weapon (w_id, w_name, w_stars, way_id) 
        VALUES (%s, %s, %s, %s)
    """, (next_w_id, weapon_name, weapon_stars, way_id))
    connection.commit()
    cursor.close()
    return next_w_id


def linkWeaponToCharacter(c_id, w_id):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO character_weapon (c_id, w_id) 
        VALUES (%s, %s)
    """, (c_id, w_id))
    connection.commit()
    cursor.close()


def addUserSearchHistory(tg_id, c_name):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO user_search_history (tg_id, c_name)
        VALUES (%s, %s)
    """, (tg_id, c_name))
    connection.commit()
    cursor.close()


def getUserSearchHistory(tg_id, limit=5):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT c_name FROM user_search_history 
        WHERE tg_id = %s
        ORDER BY search_time DESC
        LIMIT %s
    """, (tg_id, limit))
    results = cursor.fetchall()
    cursor.close()
    return [result[0] for result in results]