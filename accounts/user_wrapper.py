class DummyMeta:
    """Minimal _meta replacement for Django auth system"""
    pk = None  # Just a placeholder so Django's login() won't crash


class MongoUserWrapper:
    """
    Wraps a MongoUser document to make it compatible with Django's login/session system.
    """
    def __init__(self, mongo_user):
        self.mongo_user = mongo_user
        self._meta = DummyMeta()  # <-- FIX: Add a dummy _meta

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def id(self):
        return str(self.mongo_user.id)

    @property
    def pk(self):
        return str(self.mongo_user.id)

    @property
    def username(self):
        return self.mongo_user.username

    @property
    def email(self):
        return self.mongo_user.email

    @property
    def is_active(self):
        return self.mongo_user.is_active

    @property
    def is_staff(self):
        return self.mongo_user.is_staff

    @property
    def is_superuser(self):
        return self.mongo_user.is_superuser

    def get_full_name(self):
        return self.mongo_user.get_full_name()

    def get_short_name(self):
        return self.mongo_user.get_short_name()

    def __str__(self):
        return self.mongo_user.username
