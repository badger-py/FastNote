from db import get_db


# create tables
db = next(get_db())
for i in ["users", "folders", "notes"]:
    db.create_collection(i)

# NOTE: you can use Faker libary to create fake data
