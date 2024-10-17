# ini untuk membuat table, dan di migrate ke mysql

from app import db

# jika melakukan perubahan pada model ini, diharuskan, flask db migrate -m "alesannya"
# setelah di migrate, wajib di flask db upgrade

class Gambar(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    judul = db.Column(db.String(50), nullable=False)
    pathname = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Gambar {}>'.format(self.name)
