from api.v1.routes import api
from flask_restplus import Resource, fields

example_namespace = api.namespace('example_namespace', description='Example Namespace')


@example_namespace.route('')
class Example(Resource):
    response_obj = api.model('Message', {
        'message': fields.String(description='Message', required=True)
    })

    @api.marshal_with(response_obj)
    def get(self):
        return {'message': 'Hello World!'}

    @api.marshal_with(response_obj)
    def post(self):
        return {'message': 'Hello World!'}, 201

    @api.marshal_with(response_obj)
    def put(self):
        return {'message': 'Hello World!'}, 201

    @api.marshal_with(response_obj)
    @api.response(202, 'Deleted')
    def delete(self):
        return {'message': 'Hello World!'}, 202
