from orator import Model


class LtiSession(Model):
    __table__ = 'ltiSessions'

    def __setitem__(self, key, item):
        setattr(self, key, item)

    def __getitem__(self, key):
        return getattr(self, key)

    def __contains__(self, key):
        return hasattr(self, key) and getattr(self, key)

    def get(self, key, default=None):
        if hasattr(self, key):
            return getattr(self, key)
        return default
