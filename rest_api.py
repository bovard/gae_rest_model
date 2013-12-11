import webapp2

from google.appengine.ext import ndb


class Operations:
    CREATE = "CREATE"
    READ = "READ"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    CRUD = ["CREATE", "READ", "UPDATE", "DELETE"]


def get_path_and_qsp(path):
    split = path.split('?')
    path = split[0]
    qsp = {}
    if len(split) > 1:
        params = split[1].split('&')
        for param_def in params:
            param_def = param_def['=']
            qsp[param_def[0]] = param_def[1]
    return path, qsp


class RestHandler(webapp2.RequestHandler):
    def get(self, path):
        self.response.write('Hello world!')

    def post(self, path):
        # create an entity and get the location
        # returns a 201 with location
        self.response.write('Hello world!')

    def head(self, path):
        self.response.write('Hello world!')

    def options(self, path):
        self.response.write('Hello world!')

    def put(self, path):
        # create a new entity with a specified id
        # or completely replace all the properties of an entity
        # must be idempotent -> same server state no matter how many are run
        self.response.write('Hello world!')

    def delete(self, path):
        self.response.write('Hello world!')

    def trace(self, path):
        self.response.write('Hello world!')


class RestModel(ndb.Model):

    def __init__(self, *args, **kwargs):
        self.operations = Operations.CRUD
        self.category = None
        super(RestModel, self).__init__()

    @classmethod
    def to_html(self):
        pass

    @classmethod
    def to_json(self):
        pass

    @classmethod
    def to_xml(self):
        pass

    def to_html(self):
        pass

    def to_json(self):
        pass

    def to_xml(self):
        pass


class RestMixin:

    def __init__(self, *args, **kwargs):
        self.version = kwargs.get('version')
        self.description = kwargs.get('description')


class IntegerProperty(ndb.IntegerProperty, RestMixin):
    def __init__(self, *args, **kwargs):
        super(IntegerProperty, self).__init__(*args, **kwargs)
        RestMixin.__init__(self, *args, **kwargs)


class FloatProperty(ndb.FloatProperty):
    def __init__(self, *args, **kwargs):
        super(FloatProperty, self).__init__(*args, **kwargs)
        RestMixin.__init__(self, *args, **kwargs)


class StringProperty(ndb.StringProperty):
    def __init__(self):
        super(StringProperty, self).__init__()
        RestMixin.__init__(self, *args, **kwargs)


class TextProperty(ndb.TextProperty):
    def __init__(self):
        super(TextProperty, self).__init__()
        RestMixin.__init__(self, *args, **kwargs)


class BlobProperty(ndb.BlobProperty):
    def __init__(self):
        super(BlobProperty, self).__init__()
        RestMixin.__init__(self, *args, **kwargs)


class DateTimeProperty(ndb.DateTimeProperty):
    def __init__(self):
        super(DateTimeProperty, self).__init__()
        RestMixin.__init__(self, *args, **kwargs)


class DateProperty(ndb.DateProperty):
    def __init__(self):
        super(DateProperty, self).__init__()
        RestMixin.__init__(self, *args, **kwargs)


class TimeProperty(ndb.TimeProperty):
    def __init__(self):
        super(TimeProperty, self).__init__()


class GeoPtProperty(ndb.GeoPtProperty):
    def __init__(self):
        super(GeoPtProperty, self).__init__()


class KeyProperty(ndb.KeyProperty):
    def __init__(self):
        super(KeyProperty, self).__init__()


class BlobKeyProperty(ndb.BlobKeyProperty):
    def __init__(self):
        super(BlobKeyProperty, self).__init__()


class UserProperty(ndb.UserProperty):
    def __init__(self):
        super(UserProperty, self).__init__()


class StructuredProperty(ndb.StructuredProperty):
    def __init__(self):
        super(StructuredProperty, self).__init__()


class LocalStructuredProperty(ndb.LocalStructuredProperty):
    def __init__(self):
        super(LocalStructuredProperty, self).__init__()


class JsonProperty(ndb.JsonProperty):
    def __init__(self):
        super(JsonProperty, self).__init__()


class PickleProperty(ndb.PickleProperty):
    def __init__(self):
        super(PickleProperty, self).__init__()


class GenericProperty(ndb.GenericProperty):
    def __init__(self):
        super(GenericProperty, self).__init__()


class ComputedProperty(ndb.ComputedProperty):
    def __init__(self):
        super(ComputedProperty, self).__init__()
