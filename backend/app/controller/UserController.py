'''
Desc : Tempat mengotrol tentang User
'''

from app.model.user import User
from app.model.gambar import Gambar
from app import response, app, db, uploadconfig
from flask import request
from flask_jwt_extended import *
from datetime import timedelta, datetime
import os                                               # library os digunakan untuk menyimpan atau memindahkan file dari koputer lokal ke server
import uuid
from werkzeug.utils import secure_filename

''' 
Desc : Fungsi dibawah ini digunakan untuk upload file
'''
def upload():
    try:
        judul = request.form.get('judul')
        
        if 'file' not in request.files:
            return response.badRequest([], "File Tidak Tersedia")
        
        file = request.files['file']

        if file.filename == '':
            return response.badRequest([], "File Tidak Tersedia")
        
        if file and uploadconfig.allowed_file(file.filename):              # ini memanggil function allowed extension apaka ada
            uid = uuid.uuid4()                                             # uuid supaya nama file nya berbeda
            filename = secure_filename(file.filename)
            renamefile = "Flask-"+str(uid)+filename

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))    # tempat untuk simpan di pathnya upload

            uploads = Gambar(judul=judul, pathname=renamefile)
            db.session.add(uploads)
            db.session.commit()

            return response.success(
                {
                'judul' : judul,
                'pathname' : renamefile
                },
                "Success mengupload file"
            )
        
        else:
            return response.badRequest([], "File Diluar Extension yang diijinkan")
        
    except Exception as e:
        print(e)


'''
Desc : Fungsi dibawah ini untuk menambahkan user 
'''
def buatAdmin():

    try:
        nama = request.form.get('nama')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1

        users = User(name=nama,email=email,level=level)     # construktor mode
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('', 'Success Menambahkan Data Admin!')
    except Exception as e:
        print(e)

'''
Desc : Fungsi dibawah ini untuk menampilkan user yang telah melakukan login
'''

def singleObject(data):
    data = {
        'id' : data.id,
        'nama': data.name,
        'email': data.email,
        'level': data.level
    }
    return data

'''
Desc : Fungsi login, mengambil data imputan dari form data, dan mengecek sesuai tidak email atau passwordnya, juga token jwt nya
        cuma bisa sekali dilakukan
'''
def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            return response.badRequest([], "Email tidak terdaftar")
        
        if not user.checkPassword(password):
            return response.badRequest([], "Kombinasi Password Salah")
        
        data = singleObject(user)

        expires = timedelta(days=5)                         # digunakan untuk token setelah login masa kadarluasa, tidak mengunakan datetime lagi tapi langsung
        expires_refresh = timedelta(days=5)                  # digunakan untuk memperbarui

        acces_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

        return response.success({
            "data" : data,
            "access_token" : acces_token,
            "refresh_token" : refresh_token,
        }, "Sukses Login!")
    
    except Exception as e:
        print(e)
