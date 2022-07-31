from flask_script import Manager
from apps import create_app

from apps.users.modles import User    #用不到也不能删
app = create_app()
manager = Manager(app)
if __name__ == '__main__':
    manager.run()
