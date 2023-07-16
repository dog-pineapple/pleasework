import pickle
import streamlit_authenticator as stauth
from pathlib import Path
from PIL import Image
import streamlit as st
import pandas as pd
from h import create_table, add_data, sel, view_all_data, view_part_data, deleting, final
# всякая залупа
PAGE_TITLE = 'Choosing e-liq'
PAGE_ICON = ':cactus:'
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = f'{current_dir}/static/style.css'

with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

image = Image.open('photo/pic.png')
st.image(image)
st.subheader('Made by')

#main part
a1=a2=a3=a4=a5=0

page_bg_img = '''
    <style>
    [data-testid='stAppViewContainer'] {
    background-image: url("https://i.pinimg.com/originals/53/fa/02/53fa026cdabdd2f1f1206564b96e44dc.jpg");
    background-size: cover;

    }
    </style>
    '''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Выбери свою жидкость :)')

branch = st.selectbox("Твой филиал", ["Пассаж", "Вега", "Миндаль", "Космос"])
if branch == "Пассаж":
    create_table('Пассаж')
if branch == "Вега":
    create_table('Вега')
if branch == "Миндаль":
    create_table('Миндаль')
else:
    create_table('Космос')
menu = ['Добавить жидкость', "Выбрать жидкость", "Доступные жидкости | Редактор"]
choice = st.sidebar.selectbox('Меню', menu)
if choice == 'Добавить жидкость':
    log = st.sidebar.text_input('Логин')
    password = st.sidebar.text_input('Пароль', type='password')
    if st.sidebar.checkbox('Войти'):
        if log == 'zapravkakpvmrr' and password == 'Zapravka_liq280315':

            col1, col2, col3 = st.columns(3)
            with col1:
                name = st.text_area('Название жидкости')
            with col2:
                nic = st.selectbox('Вид никотина', ['Соль', "Щёлочь"])
            with col3:
                if nic == 'Соль':
                    mgs = st.selectbox('Крепость', ['12', "20", "40"])
                if nic == 'Щёлочь':
                    mgs = st.selectbox('Крепость', ['0', "3", "6", "9", "12"])
                flavor = st.selectbox("Кислая или сладкая?", ['Кислая', 'Сладкая'])
                specifics = st.selectbox('Вкус', ['Фрукты', 'Ягоды', 'Травы', 'Табак', 'Десерты', 'Напитки'])
                menthol = st.selectbox('Холод', ['С холодом', 'Без холода'])

            # ПРЕДЫДУЩИЙ ВАРИАНТ: if st.button('Добавить жидкость'):
                                      #add_data(branch, name, nic, mgs, flavor, specifics, menthol)
            # НОВЫЙ ВАРИАНТ:
            if st.button('Добавить жидкость'):
                if 'added' + f'{branch}' + f'{name}' + f'{nic}' + f'{mgs}' + f'{flavor}' + f'{specifics}' + f'{menthol}' \
                        not in st.session_state:
                    st.session_state['added' + f'{branch}' + f'{name}' + f'{nic}' + f'{mgs}' + f'{flavor}' + f'{specifics}' +
                                     f'{menthol}'] = add_data(branch, name, nic, mgs, flavor, specifics, menthol)
                st.success(f"Жидкость {name} успешно добавлена")
        else:
            st.error('Неверный логин или пароль, товарищ, перепроверь.')


elif choice == "Выбрать жидкость":
    def my(h, n, m, x, y):

        if h == 1:
            if n == 1:
                if m == 1:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Кислая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Кислая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Кислая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Кислая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Кислая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Кислая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Кислая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Кислая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Кислая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Кислая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Кислая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Кислая", "Напитки", "Без холода")

                else:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Сладкая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Сладкая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Сладкая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Сладкая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Сладкая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Сладкая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Сладкая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Сладкая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Сладкая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Сладкая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Соль", 12, "Сладкая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Соль", 12, "Сладкая", "Напитки", "Без холода")

            elif n == 2:
                if m == 1:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Кислая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Кислая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Кислая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Кислая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Кислая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Кислая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Кислая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Кислая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Кислая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Кислая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Кислая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Кислая", "Напитки", "Без холода")

                else:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Сладкая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Сладкая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Сладкая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Сладкая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Сладкая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Сладкая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Сладкая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Сладкая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Сладкая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Сладкая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Соль", 20, "Сладкая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Соль", 20, "Сладкая", "Напитки", "Без холода")

            else:
                if m == 1:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Кислая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Кислая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Кислая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Кислая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Кислая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Кислая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Кислая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Кислая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Кислая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Кислая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Кислая", "Напитки", "С холодом")
                            st.write(result)
                        else:
                            result = sel(branch, "Соль", 40, "Кислая", "Напитки", "Без холода")

                else:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Сладкая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Сладкая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Сладкая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Сладкая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Сладкая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Сладкая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Сладкая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Сладкая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Сладкая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Сладкая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Соль", 40, "Сладкая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Соль", 40, "Сладкая", "Напитки", "Без холода")

        else:
            if n == 4:
                if m == 1:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Кислая", "Напитки", "Без холода")

                else:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 0, "Сладкая", "Напитки", "Без холода")

            elif n == 5:
                if m == 1:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Кислая", "Напитки", "Без холода")

                else:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 3, "Сладкая", "Напитки", "Без холода")

            elif n == 6:
                if m == 1:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Кислая", "Напитки", "Без холода")

                else:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 6, "Сладкая", "Напитки", "Без холода")

            elif n == 7:
                if m == 1:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Кислая", "Напитки", "Без холода")

                else:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 9, "Сладкая", "Напитки", "Без холода")

            else:
                if m == 1:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Кислая", "Напитки", "Без холода")

                else:
                    if x == 1:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Фрукты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Фрукты", "Без холода")

                    elif x == 2:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Ягоды", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Ягоды", "Без холода")

                    elif x == 3:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Травы", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Травы", "Без холода")

                    elif x == 4:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Десерты", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Десерты", "Без холода")

                    elif x == 5:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Табак", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Табак", "Без холода")

                    else:
                        if y == 1:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Напитки", "С холодом")

                        else:
                            result = sel(branch, "Щёлочь", 12, "Сладкая", "Напитки", "Без холода")

        df = pd.DataFrame(result)
        st.dataframe(df)
    one = st.radio('Соль или щелочь?', ("Соль", "Щелочь"))
    if one == 'Соль':
        two = st.radio('Крепость?', ("12", "20", "20 ultra"))
        a1 = 1
    else:
        two = st.radio('Крепость?', ("0", "3", "6", '9', '12'))
        a1 = 2
    if two == '12':
        a2 = 1
    elif two == '20':
        a2 = 2
    elif two == '20 ultra':
        a2 = 3
    elif two == '0':
        a2 = 4
    elif two == '3':
        a2 = 5
    elif two == '6':
        a2 = 6
    elif two == '9':
        a2 = 7
    else:
        a2 = 8
    three = st.radio('Кислое или сладкое?', ("Кислое", "Сладкое"))
    if three == 'Кислое':
        a3 = 1
    else:
        a3 = 2
    four = st.radio('Сложный выбор', ("Фрукты", "Ягоды", "Десерты", "Травы",
                                          "Табак", "Напитки"))
    if four == 'Фрукты':
        a4 = 1
    elif four == 'Ягоды':
        a4 = 2
    elif four == 'Травы':
        a4 = 3
    elif four == 'Десерты':
        a4 = 4
    elif four == 'Табак':
        a4 = 5
    else:
        a4 = 6
    five = st.radio('C холодом?', ("Да", "Нет"))
    if five == 'Да':
        a5 = 1
    else:
        a5 = 2




    my(a1, a2, a3, a4, a5)

if choice == 'Доступные жидкости | Редактор':
    log = st.sidebar.text_input('Логин')
    passw = st.sidebar.text_input('Пароль', type='password')
    if st.sidebar.checkbox('Войти'):
        if log == 'zapravkakpvmrr' and passw == 'Zapravka_liq280315':
            result2 = view_all_data(branch)
            df2 = pd.DataFrame(result2)
            st.dataframe(df2)
            selected_liquid = st.selectbox("Удалить", view_part_data(branch))
            if st.button("Удалить жидкость"):
                deleting(branch, selected_liquid)
                final(branch, selected_liquid)
                st.success(f'Жидкость {selected_liquid} была успешно удалена!')
                result2 = view_all_data(branch)
                df2 = pd.DataFrame(result2)
                st.dataframe(df2)



