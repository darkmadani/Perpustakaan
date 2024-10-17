# ini untuk create table profile, dan di migrate ke database mysql

from app import db
from app.model.user import User

class Profile(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    NIS = db.Column(db.Integer, nullable=False)
    kelas = db.Column(db.String(50), nullable=False)
    angkatan = db.Column(db.Integer, nullable=False)
    alamat = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    photo_profile = db.Column(db.String(50), nullable=False)
    user_iduser = db.Column(db.BigInteger, db.ForeignKey(User.id, ondelete='CASCADE'))

    def __repr__(self):
        return '<Profile {}'.format(self.NIS)

