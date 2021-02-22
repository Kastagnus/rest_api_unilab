from werkzeug.security import safe_str_cmp
from MyProject.models.user import UserModel

def authentication(username, password):
    user = UserModel.search_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload["identity"]
    return UserModel.search_by_id(user_id), None