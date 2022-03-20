"""
    Simple declarative object validation and cleaning helper -- alternative to a full REST library
"""

# Missing value placeholder
undefined = object()


# Customized validation exception
class ValidationError(Exception):
    pass


# Field
class BaseField(object):
    field_name = None

    def __init__(self, required=False, nullable=False, validators=[]):
        self.required = required
        self.nullable = nullable
        self.validators = validators

    def __call__(self):
        raise NotImplementedError()

    def check_empty(self, value):
        if value is undefined:
            if self.required:
                raise ValidationError('is required')

            return False

        if value is None:
            if not self.nullable:
                raise ValidationError('should not be null')

            return False

        return True


class Object(BaseField):
    field_name = 'object'

    def __init__(self, fields, required=False, nullable=False):
        super().__init__(required, nullable)

        self.fields = []

        for name, validator in fields.items():
            if isinstance(validator, tuple):
                source_name = validator[0]
                validator = validator[1]
            else:
                source_name = name

            self.fields.append((name, source_name, validator))

    def __call__(self, state, value):
        if not self.check_empty(value):
            return value

        if not isinstance(value, dict):
            raise ValidationError('not an object')

        result = {}

        # Update path for error reporting
        old_path = state.path

        for dest, source, validator in self.fields:
            item = value.get(source, undefined)

            try:
                # Update path
                if old_path:
                    state.path = old_path + '.' + source
                else:
                    state.path = source

                item = validator(state, item)

                if item is not undefined:
                    result[dest] = item

            except ValidationError as ex:
                state.add_error(state.path, str(ex))

        state.path = old_path

        return result


class GenericField(BaseField):
    field_name = None
    coerce = str

    def __call__(self, state, value):
        if not self.check_empty(value):
            return value

        try:
            value = self.coerce(value)
        except ValueError:
            name = getattr(self.coerce, '__name__') or self.coerce
            raise ValidationError('expected to be %s' % name)

        for v in self.validators:
            v(value)

        return value


# Field type shortcuts
class String(GenericField):
    field_name = 'string'
    coerce = str


class Integer(GenericField):
    field_name = 'integer'
    coerce = int


# Validation state holder
class State(object):
    def __init__(self):
        self.errors = None
        self.data = None
        self.path = ''

    def add_error(self, name, message):
        if not self.errors:
            self.errors = {}

        if name not in self.errors:
            self.errors[name] = [message]
        else:
            self.errors[name].append(message)

    @property
    def valid(self):
        return not bool(self.errors)


def clean(value, validator):
    state = State()

    try:
        state.data = validator(state, value)
    except ValidationError as ex:
        state.add_error(None, str(ex))

    return state
