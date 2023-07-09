import logging
import uuid

from werkzeug.security import check_password_hash, generate_password_hash

from auction_system.database.models import Token, User, UserType, session

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


class Authenticator:
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

            return True
        return False

    def login(self, email, password):
        user = session.query(User).filter_by(email=email.lower()).first()

        if user:
            if check_password_hash(user.password_hash, password):
                token_str = str(uuid.uuid4())
                token = Token(user_id=user.id, token=token_str)
                session.add(token)
                session.commit()

                return token_str

            return False
        return False

    def logout(self, token):
        try:
            user_token = session.query(Token).filter_by(token=token).first()
            session.delete(user_token)
            session.commit()
            return True

        except Exception as e:
            logger.error(e)
