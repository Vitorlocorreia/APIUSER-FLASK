from flask import Blueprint
from app.controllers import user_controller

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["POST"])
def create_user():
    """Create a new user
    ---
    tags:
      - Users
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
              example: Vitor Luiz
            email:
              type: string
              example: vitor@example.com
    responses:
      201:
        description: User created
    """
    return user_controller.create_user()

@user_bp.route("/users", methods=["GET"])
def get_users():
    """Get all users
    ---
    tags:
      - Users
    responses:
      200:
        description: List of users
    """
    return user_controller.get_users()

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Get a user by ID
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
    responses:
      200:
        description: A user object
    """
    return user_controller.get_user(user_id)

@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Update a user by ID
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      200:
        description: Updated user
    """
    return user_controller.update_user(user_id)

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a user by ID
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
    responses:
      204:
        description: User deleted
    """
    return user_controller.delete_user(user_id)
