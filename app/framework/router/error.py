from flask import Blueprint, Response, abort, jsonify, request

error_router = Blueprint("error_router", __name__)

@error_router.app_errorhandler(400)
def bad_request(error):
    return jsonify({"message": "Bad Request"}), 400

@error_router.app_errorhandler(401)
def unauthorized(error):
    return jsonify({"message": "Unauthorized"}), 401

@error_router.app_errorhandler(403)
def forbidden(error):
    return jsonify({"message": "Forbidden"}), 403

@error_router.app_errorhandler(404)
def not_found(error):
    return jsonify({"message": "Not Found"}), 404

@error_router.app_errorhandler(409)
def conflict(error):
    return jsonify({"message": "Conflict"}), 409

@error_router.app_errorhandler(500)
def internal_server_error(error):
    return jsonify({"message": "Internal Server Error"}), 500
