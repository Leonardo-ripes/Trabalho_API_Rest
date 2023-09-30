from marshmallow import Schema, fields

class MovieSchema(Schema):
    id = fields.String(required=False)
    type = fields.String(required=True)
    title = fields.String(required=True)
    director = fields.String(required=True)
    cast = fields.String(required=True)
    country = fields.String(required=True)
    date_added = fields.String(required=True)
    release_year = fields.Integer(required=True)
    rating = fields.String(required=True)
    duration = fields.String(required=True)
    listed_in = fields.String(required=True)
    description = fields.String(required=True)