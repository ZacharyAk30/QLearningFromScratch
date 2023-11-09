import redis

class dataManageur:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def get(self, key):
        return self.r.get(key)

    def set(self, key, value):
        self.r.set(key, value)