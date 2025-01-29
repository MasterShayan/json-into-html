from enum import Enum

class DisplayType(Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"
    LINK = "link"

class JsonDefinition:
    def __init__(self):
        self.fields = {}

    def add_field(self, field_name, display_type: DisplayType, options=None):
        if not isinstance(field_name, str) or not field_name:
            raise ValueError("Field name must be a non-empty string.")

        if not isinstance(display_type, DisplayType):
            raise TypeError("display_type must be a DisplayType enum member.")

        if display_type == DisplayType.IMAGE:
            if options and ("width" not in options or "height" not in options):
                raise ValueError("Width and height must be defined for IMAGE display type.")
        elif display_type == DisplayType.LINK:
            if options and ("href_key" not in options or "text_key" not in options):
                raise ValueError("href_key and text_key must be defined for LINK display type.")

        self.fields[field_name] = {"display_type": display_type, "options": options or {}}

    def get_field_definition(self, field_name):
        return self.fields.get(field_name)

    def __repr__(self):
        return f"JsonDefinition(fields={self.fields})"