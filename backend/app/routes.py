from app import app, response
from app.controller import DosenController
from app.controller import UserController
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# Tempat Konfigurasi Start Halaman


@app.route('/')
def index():
    return "Hello Flask App"

@app.route('/protected', methods=['GET'])
@jwt_required()                                           # diprotecsi dengan jwt_required
def protected():

    '''
    Desc : fungsi ini, digunakan untuk melindungi dari access public, kudu punya token supaya bisa
    '''
    current_user = get_jwt_identity()
    return response.success(current_user, 'Success')

@app.route('/dosen', methods=['GET', 'POST'])   
@jwt_required()             
def bacadosen():
     
     '''
     Desc : Fungsi ini Membaca dari data dosen controller
            Mengunakan Methods GET untuk Meminta data 
     ''' 

     if request.method == 'GET':
         return DosenController.index()
     else:
         return DosenController.save()
     
@app.route('/api/dosen/page', methods=['GET'])
def pagination():

    '''
    Desc : Fungsi ini untuk mengatur Page next or previous
    '''
    return DosenController.pageinate()


@app.route('/file-upload', methods=['POST'])   
def inputFile():
     
     '''
     Desc : Fungsi ini untuk upload files
     ''' 
     return UserController.upload()

     
@app.route('/createadmin', methods=['POST'])                
def admins():
     
     '''
     Desc : Fungsi ini digunakan untuk membuat user admin
     ''' 
     return UserController.buatAdmin()

@app.route('/dosen/<id>', methods=['GET','PUT','DELETE'])
def dosenDetail(id):
     if request.method == 'GET':
         return DosenController.detail(id)
     elif request.method == 'PUT':
         return DosenController.upToDate(id)
     elif request.method == 'DELETE':
         return DosenController.hapus(id)
     
@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()