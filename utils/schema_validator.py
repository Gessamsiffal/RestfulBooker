from jsonschema import validate, ValidationError


class SchemaValidator:

    @staticmethod
    def validate(json_data, schema):
        try:
            validate(instance=json_data, schema=schema)
        except ValidationError as e:
            raise AssertionError(f'JSON ошибка валидации: {e.message}')