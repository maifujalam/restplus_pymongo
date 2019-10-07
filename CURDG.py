import pymongo,json

class CURDG():
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
    def connection(self):
        try:
            self.client=pymongo.MongoClient('localhost',27017)
            print(self.client)
        except Exception:
            print("Connection Error")

    def create(self,json_data):
        print(json_data)
        self.client['curd']['c1'].insert_one(json_data)

    def update(self,olds,news):
        print(olds,news)
        query={"name":olds}
        newvalue={"$set":{"name":news}}
        result=self.client['curd']['c1'].update_many(query,newvalue)
        return result

    def read(self,id):   #Read Retails of a particular user
        record = self.client['curd']['c1'].find({'id':id}, {'_id': False})
        return record

    def readAll(self):
        records = self.client['curd']['c1'].find({},{'_id':False})
        return records   #Hare returning Cursor object

    def delete(self,id):
        myquery = {"id": id}
        record = self.client['curd']['c1'].delete_many(myquery)  # Filtering
        print(record.deleted_count)
        return record.deleted_count

if __name__ == "__main__":
    ob=CURDG()
    ob.connection()
    #ob.create("aa","ccc")
    #ob.update("aa","cccc")'''
