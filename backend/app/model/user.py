from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.model.profile import Profile
from app.model.riwayatpinjam import RiwayatPinjam

# jika melakukan perubahan pada model ini, diharuskan, flask db migrate -m "alesannya"
# setelah di migrate, wajib di flask db upgrade

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), index=True, unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    level = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relasi ke table Profile dan Riwayat Pinjam
    profile = db.relationship(Profile, backref='user', uselist=False)
    RiwayatPinjam = db.relationship(RiwayatPinjam, backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.name)
    
    '''
    Desc : Fungsi dibawah ini, akan merubah password dari imputan
        digenerate menjadi hash
    '''
    def setPassword(self,password):
        self.password = generate_password_hash(password)

    def checkPassword(self,password):
        return check_password_hash(self.password, password)
        