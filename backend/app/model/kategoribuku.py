# ini untuk create table riwayat_pinjam, dan di migrate ke database mysql
# jika melakukan perubahan pada model ini, diharuskan, flask db migrate -m "alesannya"
# setelah di migrate, wajib di flask db upgrade

from app import db
from app.model.buku import Buku
from app.model.kategori import Kategori

class KategoriBuku(db.Model):
    kode_buku = db.Column(db.BigInteger, db.ForeignKey(Buku.id), primary_key=True)
    kategori_id = db.Coumn(db.BigInteger, db.ForeignKey(Kategori.id), primary_key=True)

    def __repr__(self):
        return f'<KategoriBuku Buku: {self.kode_buku}, Kategori: {self.kategori_id}'

