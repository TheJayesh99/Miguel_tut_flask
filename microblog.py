from main_app import app, db
from main_app.models import User, Posts

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Posts': Posts}