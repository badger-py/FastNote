from contextlib import contextmanager

from config import Config, Environment
from db import get_db
from models import Note, NoteContentPart, User

c = Config()


with contextmanager(get_db)() as db:
    # create tables
    for i in ["users", "folders", "notes"]:
        db.create_collection(i)

if c.ENVIRONMENT == Environment.DEV:
    from faker import Faker
    import enums

    f = Faker()
    with contextmanager(get_db)() as db:
        p: dict = f.profile()
        user_id = db.users.insert_one(
            User(
                email=p["mail"],
                name=p["name"],
                password="qwerty",  # FIXME: use hash instead
                is_active=True  # after registration it will False, but for testing, True
            ).dict()
        ).inserted_id
        user_id = str(user_id)
        note = Note(
            title="Some title",
            user=user_id,
            content=[
                NoteContentPart(
                    number=0,
                    type=enums.NoteContentPartType.text,
                    data=[
                        f.text()
                    ]
                ),
                NoteContentPart(
                    number=1,
                    type=enums.NoteContentPartType.text,
                    data=[
                        f.text()
                    ]
                )
            ]
        )
        db.notes.insert_one(note)
