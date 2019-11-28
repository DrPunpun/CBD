from pymongo import *
from datetime import *

cli = MongoClient()

db = cli["cbd"]
rest = db["rest"]

def create_index(arg):
    return rest.create_index([(arg, ASCENDING)], unique=False)

init = datetime.timestamp(datetime.now())
for r in rest.find({'localidade': 'Bronx'}):
    pass
fin = datetime.timestamp(datetime.now())
print(f"Demorou {fin - init}")
create_index('localidade')
#create_index('gastronomia')
#create_index('nome')
init = datetime.timestamp(datetime.now())
for r in rest.find({'localidade': 'Bronx'}):
    pass
fin = datetime.timestamp(datetime.now())
print(f"Demorou {fin - init}")