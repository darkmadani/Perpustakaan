# ini untuk menampilkan data dalam bentuk JSON

from flask import jsonify, make_response          # Feature untuk json

def success(values, message):
    
    '''
Desc : Fungsi ini akan menampilkan data
jika berahasil, ada respon 200

    '''    
    res = {                                               
        'data': values,
        'message': message
    }

    return make_response(jsonify(res)), 200

def badRequest(values, message):

    '''
Desc : Fungsi ini akan menampilkan data
jika tidak berhasil ada respon 400

    '''    
    res = {
        'data': values,
        'message': message
    }

    return make_response(jsonify(res)), 400
