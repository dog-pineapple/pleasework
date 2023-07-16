import pickle
import streamlit_authenticator as stauth
from pathlib import Path
names = ['zapravka']
usernames = ['zapravkakpvmrr']
passwords = ['Zapravka_liq280315']

hashed_passwords = stauth.Hasher(passwords).generate()
file_path = Path(__file__).parent/'hashed_pw.pkl'
with file_path.open('wb') as f:
    pickle.dump(hashed_passwords, f)
