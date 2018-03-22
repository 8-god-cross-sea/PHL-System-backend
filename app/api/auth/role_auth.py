from app import auth


class RoleAuth(object):
    EVERYONE = 0
    USER = 0b00001
    ADMIN = 0b10000
    ANY_USER = 0b11111

    def __init__(self, access_dict={}, role_mask=EVERYONE):
        self.role_mask = role_mask
        self.access_dict = access_dict

    def authorize(self, fun_name):
        mask = self.access_dict.get(fun_name, None)
        cur_role = mask if mask is not None else self.role_mask

        if not cur_role:
            return True

        user = auth.get_logged_in_user()
        if not user:
            return False

        return user.permission & cur_role
