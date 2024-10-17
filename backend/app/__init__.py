from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

'''
Desc : Tempat inisiasi flask sebelum digunakan method nya
'''

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)               
jwk = JWTManager(app)


# tambahkan Resource model atau class baru
from app.model import user, dosen, mahasiswa, gambar,profile,riwayatpinjam,buku,kategoribuku,kategori
from app import routes