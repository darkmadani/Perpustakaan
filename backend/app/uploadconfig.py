# Tempat Konfigurasi Upload

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','pdf'])

def allowed_file(filename):

    '''
    Desc : Fungsi untuk mengecek extension nya sesuai atau tidak
    '''
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS