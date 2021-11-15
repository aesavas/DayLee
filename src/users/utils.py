from passlib.hash import pbkdf2_sha256
from cryptography.fernet import Fernet


def create_encrypted_password(master_password):
    """
        To encrypt master_password for storing safely
    """
    enc_pw = pbkdf2_sha256.hash(master_password)
    return enc_pw

def check_master_password(master_password, hash_data):
    """
        To check master_password for viewing diaries
    """
    return pbkdf2_sha256.verify(master_password, hash_data)

def create_secret_key():
    """
        To create secret key for Fernet
    """
    return Fernet.generate_key()

def encrypt_diary(request, diary):
    f = Fernet(request.user.profile.secret_key)
    enc_diary = f.encrypt(diary)
    return enc_diary

def decrypt_diary(request, enc_diary):
    f = Fernet(request.user.profile.secret_key)
    diary = f.decrypt(enc_diary)
    return diary
