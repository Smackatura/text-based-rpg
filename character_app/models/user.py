from character_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular battleression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db = "charas_db"
    def __init__(self, data):
        self.id = data['id']
        self.user_name = data['user_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users(user_name, email, password) VALUES(%(user_name)s, %(email)s, %(password)s)"
        return connectToMySQL("charas_db").query_db(query, data)

    @classmethod
    def get_user(cls, data):
        query= "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL("charas_db").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_user_by_email(cls, data):
        query= "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL("charas_db").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        data = { "email" : user["email"] }
        if User.get_user_by_email(data):
            flash("Email already in use", "error")
            is_valid = False
        if len(user['user_name']) < 2:
            flash("Userame: min 2 characters", "error")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("Email: Please use a valid email address", "error")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be 8 characters long", "error")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Password and Confirm Password must match", "error")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        if len(user['email']) < 1:
            flash("Email cannot be blank", "error")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email", "error")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be 8 characters long", "error")
            is_valid = False
        return is_valid