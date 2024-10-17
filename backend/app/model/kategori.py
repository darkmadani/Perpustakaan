# ini untuk create table riwayat_pinjam, dan di migrate ke database mysql
# jika melakukan perubahan pada model ini, diharuskan, flask db migrate -m "alesannya"
# setelah di migrate, wajib di flask db upgrade

from app import db
from app.model.kategoribuku import KategoriBuku

class Kategori(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama_kategori = db.Column(db.String(50), nullable=False)

    # relasi ke table KategoriBuku
    Kategori_buku = db.relationship(KategoriBuku, backref='kategori')

    def __repr__(self):
        return '<Kategori {}'.format(self.nama_kategori)