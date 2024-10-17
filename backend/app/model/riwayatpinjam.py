# ini untuk create table riwayat_pinjam, dan di migrate ke database mysql
# jika melakukan perubahan pada model ini, diharuskan, flask db migrate -m "alesannya"
# setelah di migrate, wajib di flask db upgrade

from app import db
from app.model.buku import Buku
from app.model.user import User

class RiwayatPinjam(db.Model):
    id_buku = db.Column(db.BigInteger, db.ForeignKey(Buku.id, ondelete='CASCADE'))
    tanggal_pinjam = db.Column(db.Date, nullable=False)
    tanggal_wajib_kembali = db.Column(db.Date, nullable=False)
    tanggal_pengembalian = db.Column(db.Date)
    user_id = db.Column(db.BigInteger, db.ForeignKey(User.id, ondelete='CASCADE'))

    def __repr__(self):
        return f'<RiwayatPinjam Buku: {self.id_buku}, User : {self.user_id}>'