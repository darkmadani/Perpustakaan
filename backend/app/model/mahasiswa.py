from app import db
from app.model.dosen import Dosen

# jika melakukan perubahan pada model ini, diharuskan, flask db migrate -m "alesannya"
# setelah di migrate, wajib di flask db upgrade

class Mahasiswa(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nim = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    dosen_satu = db.Column(db.BigInteger, db.ForeignKey(Dosen.id, ondelete='CASCADE'))     # ForeignKey supaya terhubung dengan table Dosen
    dosen_dua = db.Column(db.BigInteger, db.ForeignKey(Dosen.id, ondelete='CASCADE'))      # tambahkan, ondelete='CASCADE' jika ada foreignkey, soalnya nanti dihapus gk bisa

    def __repr__(self):
        return '<Mahasiswa {}>'.format(self.name)