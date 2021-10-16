# from character_app.config.mysqlconnection import connectToMySQL
# from character_app.models.user import User

# out of time, need to present this.. not a mvp feature.



# class Battle:
#     def __init__(self, data):
#         self.id = data['id']
#         self.win = data['win']
#         self.lose = data['lose']
#         self.user_id = data['user_id']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
#         self.poster = None
#         self.users_who_liked = []

#     @classmethod
#     def get_battle(cls, data):
#         query= "SELECT * FROM battles WHERE id = %(id)s"
#         results = connectToMySQL("charas_db").query_db(query, data)
#         if len(results) < 1:
#             return False
#         return cls(results[0])
    # @classmethod
    # def delete(cls, data):
    #     query = "DELETE FROM battles WHERE id = %(id)s"
    #     return connectToMySQL("thoughts_forum").query_db(query, data)
    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE battles SET content=%(content)s WHERE id = %(id)s"
    #     return connectToMySQL("thoughts_forum").query_db(query, data)
    # @classmethod
    # def add_post(cls, data):
    #     query = "INSERT INTO battles(content, user_id) VALUES(%(content)s, %(user_id)s)"
    #     return connectToMySQL("thoughts_forum").query_db(query, data)
    # @classmethod
    # def get_all_user_liked_battles(cls, data):
    #     battles_liked = []
    #     query = "SELECT post_id FROM liked_battles JOIN users ON users.id=user_id WHERE user_id=%(id)s"
    #     results = connectToMySQL("thoughts_forum").query_db(query, data)
    #     for result in results:
    #         battles_liked.append(result['post_id'])
    #     return battles_liked

    # @classmethod
    # def like_post(cls, data):
    #     query = "INSERT INTO liked_battles(post_id,user_id) VALUES(%(post_id)s,%(user_id)s)"
    #     return connectToMySQL("thoughts_forum").query_db(query, data)

    # @classmethod
    # def dislike_post(cls, data):
    #     query = "DELETE FROM liked_battles WHERE post_id=%(post_id)s AND user_id=%(user_id)s"
    #     return connectToMySQL("thoughts_forum").query_db(query, data)

    # @classmethod
    # def get_all_battles(cls):
    #     query = "SELECT * FROM battles "\
    #             "LEFT JOIN users ON users.id = battles.user_id "\
    #             "LEFT JOIN liked_battles ON battles.id = liked_battles.post_id "\
    #             "LEFT JOIN users AS users2 ON users2.id = liked_battles.user_id "\
    #             "ORDER BY battles.created_at DESC"

    #     results = connectToMySQL("charas_db").query_db(query)
    #     all_battles = []

    #     for result in results:
    #         new_post = True
    #         like_user_data = {
    #             "id" : result["users2.id"],
    #             "user_name": result["users2.user_name"],
    #             "email": result["users2.email"],
    #             "password": result["users2.password"],
    #             "created_at": result["users2.created_at"],
    #             "updated_at": result["users2.updated_at"]
    #         }
            
    #         #If curr row is still for last processed post, there are more users_who_liked the post
    #         if len(all_battles) >0 and all_battles[len(all_battles) -1].id == result['id']:
    #             all_battles[len(all_battles)-1].users_who_liked.append(User(like_user_data))
    #             new_post = False

    #         if new_post:
    #             post = cls(result)
    #             poster_data = {
    #                 "id" : result["users.id"],
    #                 "user_name": result["user_name"],
    #                 "email": result["email"],
    #                 "password": result["password"],
    #                 "created_at": result["users.created_at"],
    #                 "updated_at": result["users.updated_at"]
    #             }
    #             post.poster = User(poster_data)
    #             #There is a user who liked this post that needs to be processed
    #             if result['users2.id'] is not None:
    #                 post.users_who_liked.append(User(like_user_data))
    #             all_battles.append(post)
    #     return all_battles

    # @classmethod
    # def get_user_battles(cls, data):
    #     query = "SELECT * FROM battles WHERE user_id =%(user_id)s"
    #     battles = connectToMySQL("charas_db").query_db(query, data)
    #     results = []
    #     for battle in battles:
    #         results.append(cls(battle))
    #     return results
    # @staticmethod
    # def validate_post(data):
    #     is_Valid = True
    #     if len(data['content']) < 5:
    #         flash("Thought is required and Should be at least 5 characters", "error")