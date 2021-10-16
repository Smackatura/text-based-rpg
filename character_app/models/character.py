# import the function that will return an instance of a connection
from character_app.config.mysqlconnection import connectToMySQL

# model the class after the friend table from our database



class Character:
    # Roles can be added here in order to be added as options for the user
    roles = {
            "Warrior":{"attack":7,"defense":4,"speed":4},
            "Archer":{"attack":3,"defense":2,"speed":7},
            "Paladin":{"attack":3,"defense":9,"speed":3},
            "Jester":{"attack":7,"defense":2,"speed":9}
        }

    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.role = data['role']
        self.attack = data['attack']
        self.defense = data['defense']
        self.speed = data['speed']
        self.user_id = data['user_id']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM characters;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('charas_db').query_db(query)
        # Create an empty list to append our instances of friends
        characters = []
        # Iterate over the db results and create instances of friends with cls.
        for character in results:
            characters.append( cls(character) )
        return characters

    @classmethod
    def add(cls, data):
        query = "INSERT INTO characters(name, role, attack, defense, speed, user_id) VALUES (%(name)s, %(role)s, %(attack)s, %(defense)s, %(speed)s, %(user_id)s);"
        return connectToMySQL('charas_db').query_db(query, data)

    @classmethod
    def get(cls, data):
        query = "SELECT * FROM characters WHERE id=%(id)s;"
        results = connectToMySQL('charas_db').query_db(query, data)
        return cls(results[0])

    @classmethod
    def edit(cls, data):
        query = "UPDATE characters SET name=%(name)s WHERE id=%(id)s;"
        return connectToMySQL('charas_db').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM characters WHERE id = %(id)s;"
        return connectToMySQL('charas_db').query_db(query, data)