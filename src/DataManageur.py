import redis

class dataManageur:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def get(self, key):
        return self.r.get(key)

    def set(self, key, value):
        self.r.set(key, value)
        
    def save(self,path_folder='./data/'):
        for key in self.r.keys():
            value = self.r.get(key)
            file_path = path_folder + key.decode("utf-8") + '.txt'
            # save the value in a file
            with open(file_path, 'w') as f:
                f.write(value.decode("utf-8"))  # decode the bytes to a string