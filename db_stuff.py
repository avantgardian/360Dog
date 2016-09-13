from orator import DatabaseManager

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'dog',
        'user': 'root',
        'password': 'password',
        'prefix': ''
    }
}

db = DatabaseManager(config)

def get_user(name):
    user = db.table('users').where('username', name).pluck('username')
    # for user in users:
    #    print(user['name'])
    return user

def get_bones(name):
    bones = db.table('users').where('username', name).pluck('bones')
    return bones

def set_bones(name, bones):
    db.table('users').where('username', name).increment('bones', bones)

def create_user(name, bones):
    db.table('users').insert({
        'username': name,
        'bones': bones
    })
