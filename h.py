import sqlite3
import streamlit as st
def connection(db_name):
    return sqlite3.connect(db_name)

def create_table(table):
    q = connection('data.db')
    q.execute(f'CREATE TABLE IF NOT EXISTS {table}(name TEXT, nic TEXT, mgs INT,'
              'flavor TEXT, specifics TEXT, menthol TEXT)')
    q.commit()
    q.close()

def add_data(table, name, nic, mgs, flavor, specifics, menthol):
    q = connection('data.db')
    q.execute(f'INSERT INTO {table}(name, nic, mgs, flavor, specifics, menthol)'
              'VALUES (?,?,?,?,?,?)', (name, nic, mgs, flavor, specifics, menthol))
    q.commit()
    q.close()

def sel(table, one, two, three, four, five):
    q = connection('data.db')
    data = q.execute(f'''SELECT name FROM {table} WHERE nic=? and mgs= ? and flavor= ? and specifics=?
     and menthol=?''', (one, two, three, four, five)).fetchall()
#    data = q.fetchall()
    q.close()
    return data

def view_all_data(table):
    q = connection('data.db')
    result = q.execute(f'SELECT * from {table}').fetchall()
#    result = q.fetchall()
    q.commit()
    q.close()
    return result


def view_part_data(table):
    q = connection('data.db')
    parted = q.execute(f'SELECT name FROM {table}').fetchall()
#    parted = q.fetchall()
    q.commit()
    q.close()
    return parted


def deleting(table, liq):
    q = connection('data.db')
    q.execute(f'DELETE FROM {table} WHERE name=?', (liq))
    q.commit()
    q.close()

def final(table, naming):
    q = connection('data.db')
    thing1 = q.execute(f'SELECT nic FROM {table} WHERE name=?', (naming))
    thing2 = q.execute(f'SELECT mgs FROM {table} WHERE name=?', (naming))
    thing3 = q.execute(f'SELECT flavor FROM {table} WHERE name=?', (naming))
    thing4 = q.execute(f'SELECT specifics FROM {table} WHERE name=?', (naming))
    thing5 = q.execute(f'SELECT menthol FROM {table} WHERE name=?', (naming))
    q.commit()
    return thing1, thing2, thing3, thing4, thing5
    del st.session_state['added' + f'{table}' + f'{naming}' + f'{thing1}' + f'{thing2}' + f'{thing3}' + f'{thing4}' +
                                 f'{thing5}']
    q.close()