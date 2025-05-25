from marshmallow import Schema, fields, validate

class BlacklistSchema(Schema):
    email = fields.Email(required=True)
    app_uuid = fields.Str(required=True, validate=validate.Length(equal=36))
    blocked_reason = fields.Str(validate=validate.Length(max=255))