import logging
import uuid

import Pyro4
from werkzeug.security import check_password_hash, generate_password_hash

from auction_system.server.database import session
from auction_system.server.database.models import User, UserType

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


@Pyro4.expose
class Authenticator(object):
    def register(self, email, password, user_type):
        users = session.query(User).filter_by(email=email.lower()).all()

        if users:
            logger.debug("User already exists")
            raise ValueError("User already exists")

        if not users:
            user = User(
                email=email.lower(),
                password_hash=generate_password_hash(password),
                user_type=UserType(user_type),
            )

            session.add(user)
            session.commit()
            return user.id, user.token

        return False

    def login(self, email, password):
        user = session.query(User).filter_by(email=email.lower()).first()

        if user:
            if check_password_hash(user.password_hash, password):
                return user.id, user.token

            return False
        return False

    def logout(self, token):
        try:
            user = session.query(User).filter_by(token=token).first()
            user.token = str(uuid.uuid4())
            session.commit()
            return True

        except Exception as e:
            logger.error(e)
            return False
