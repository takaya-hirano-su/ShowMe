from flask import Blueprint, Response, request

status_handler = Blueprint("status_handler", __name__)

@status_handler.errorhandler(404)
def not_found(error):
    return Response(status=404)

@status_handler.errorhandler(405)
def method_not_allowed(error):
    return Response(status=405)

@status_handler.errorhandler(500)
def internal_server_error(error):
    return Response(status=500)
