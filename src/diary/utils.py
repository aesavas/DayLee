from cryptography.fernet import Fernet
import base64

def encrypt_diary(request, diary):
    f = Fernet(request.user.profile.secret_key)
    enc_diary = f.encrypt(diary.encode()).decode()
    return enc_diary

def decrypt_diary(request, enc_diary):
    f = Fernet(request.user.profile.secret_key)
    diary = f.decrypt(enc_diary.encode()).decode()
    return diary
