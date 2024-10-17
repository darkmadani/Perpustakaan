# ini untuk create table buku, dan di migrate ke database mysql
# jika melakukan perubahan pada model ini, diharuskan, flask db migrate -m "alesannya"
# setelah di migrate, wajib di flask db upgrade

from app import db
from app.model.kategoribuku import KategoriBuku
from app.model.riwayatpinjam import RiwayatPinjam

class Buku(db.Model):
    id = db.Column(db.BigIntenger, primary_key=True, autoincrement=True)
    judul = db.Column(db.String(50), nullable=False)
    gambar = db.Column(db.String(50), nullable=False)
    pengarang = db.Column(db.String(50), nullable=False)
    deskripsi = db.Column(db.Text)
    penerbit = db.Column(db.String(50), nullable=False)
    tahun_terbit = db.Column(db.String(10), nullable=False)

    # Relasi ke Tabel KategoriBuku dan Riwayat Pinjam
    kategori_buku = db.relationship(KategoriBuku, backref='buku')
    riwayat_pinjam = db.relationship(RiwayatPinjam, backref='buku')

    def __repr__(self):
        return '<Buku {}>'.format(self.judul)
