'''

Desc : 
Dosen Controler ini akan melakukan controling data data, dari model yang kita buat dalam bentuk tabel

'''
from app.model.mahasiswa import Mahasiswa
from app.model.dosen import Dosen
from app import response, app, db           # response untuk mengecek, app, dan db, karena terkait dengan itu
from flask import request, abort, jsonify
import math

def index():

    '''
    Desc : 
    Fungsi ini untuk menampilkan data
    '''
    try:
        dosen = Dosen.query.all()
        data = formatarray(dosen)
        return response.success(data, "Success")
    except Exception as e:
        print(e)


def formatarray(datas):

    '''
    Desc : 
    Fungsi ini untuk mengambungkan atau menampung object
    '''
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):

    '''
    Desc :
    Fungsi ini , Menampung data data, dari object Dosen
    '''

    data = {
        'id': data.id,
        'nidn': data.nidn,
        'nama': data.name,
        'phone': data.phone,
        'alamat': data.alamat
    }

    return data

'''
Desc : 
Fungsi dibawah ini untuk menambahkan Data POST
'''

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))

        if not dosen:
            return response.badRequest([], 'Tidak ada Data Dosen')
        
        dataMahasiswa = formatMahasiswa(mahasiswa)

        data = singleDetailMahasiswa(dosen, dataMahasiswa)

        return response.success(data, "Success")
    
    except Exception as e:
        print(e)

def singleDetailMahasiswa(dosen, mahasiswa):

    '''
    Desc : 
    ini untuk menampung data dosen dan mahasiswa, untuk detail dan return pada fungsi detail
    '''
    data = {
        'id': dosen.id,
        'nidn': dosen.nidn,
        'nama': dosen.name,
        'phone': dosen.phone,
        'mahasiswa': mahasiswa
    }

    return data

def singleMahasiswa(mahasiswa):

    '''
    Desc : 
    Fungsi ini , Menampung data data, dari object Mahasiswa
    '''

    data = {
        'id': mahasiswa.id,
        'nim': mahasiswa.nim,
        'nama': mahasiswa.name,
        'phone': mahasiswa.phone,        
    }
    
    return data

def formatMahasiswa(data):

    '''
    Desc : 
    Fungsi ini untuk mengambungkan
    '''

    array = []
    for i in data:
        array.append(singleMahasiswa(i))
    return array

def save():

    '''
    Desc : 
    fungsi untuk menyimpan hasil dari imputan form, ditambahkan dan disimpan ke object model ataupun database mysql
    '''
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat') 

        saveDosen = Dosen(nidn=nidn, name=nama, phone=phone, alamat=alamat)     # construktor mode dosel
        db.session.add(saveDosen)
        db.session.commit()

        return response.success('', 'Success Menambahkan Data Dosen')
    except Exception as e:
        print(e)

"""
Desc : 
Fungsi Dibawah ini Untuk Update Data PUT
"""

def upToDate(id):
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        input = [
            {
                'nidn': nidn,
                'nama': nama,
                'phone': phone,
                'alamat': alamat
            }
        ]

        upDosen = Dosen.query.filter_by(id=id).first()

        upDosen.nidn = nidn
        upDosen.name = nama
        upDosen.phone = phone
        upDosen.alamat = alamat

        db.session.commit()               # supaya tersimpan

        return response.success(input, 'Success Update Data')
    except Exception as e:
        print(e)

"""
Desc : 
Fungsi Dibawah ini Untuk Menghapus Data
"""

def hapus(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()                # unuk filter_by(id=id), jangan pake == tpi =
        if not dosen:
            return response.badRequest([],'Data Dosen Kosong')
        
        db.session.delete(dosen)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus Data')
    except Exception as e:
        print(e)


'''
Desc : 
Fungsi dibawah ini untuk Pagination
'''
def get_pagination(clss, url, start, limit):
    #ambil data select
    results = clss.query.all()
    #ubah format
    data = formatarray(results)
    count = len(data)

    obj = {}

    if count < start:
        obj['success'] = False
        obj['message'] = "Page Yang dipilih melebihi batas Total Data"
        return obj
    else:
        obj['success'] = True
        obj['start_page'] = start
        obj['per_page'] = limit
        obj['total_data'] = count
        obj['total_page'] = math.ceil(count/limit)

        # previous link
        if start == 1:
            obj['previous'] = ''
        else:
            start_copy = max(1, start-limit)
            limit_copy = start - 1
            obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)

        # next link
        if start + limit > count:
            obj['next'] = ''
        else:
            start_copy = start + limit
            obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
        
        obj['result'] = data[(start - 1): (start - 1 + limit)]
        return obj

# fungsi paging
def pageinate():
    # ambil parameter get
    # sample www.google.com?product = baju

    start = request.args.get('start')
    limit = request.args.get('limit')

    try:
        if start == None or limit == None:
            return jsonify(get_pagination(
                Dosen,
                'http://127.0.0.1:5000/api/dosen/page',
                start=request.args.get('start', 1),
                limit=request.args.get('limit', 3)
            ))
        else:
            return jsonify(get_pagination(
                Dosen,
                'http://127.0.0.1:5000/api/dosen/page',
                start=int(start),
                limit=int(limit)
            ))
            
    except Exception as e:
        print(e)
