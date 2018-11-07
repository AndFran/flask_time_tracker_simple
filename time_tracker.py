from app import flask_app, db
from app.models import User, TrackedItem


@flask_app.shell_context_processor
def get_shell_context():
    return {"db": db, "User": User, "TrackedItem": TrackedItem}
