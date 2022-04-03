from ast import Delete
from email import message
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.post_model import Post

class RPost(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', 
        type=str,
        required=True,
        help="Please give this post a title!"
    )
    parser.add_argument('user_id', 
        type=int,
        required=True,
        help="This post must belong to a user!"
    )

    def get(self, title):
        post = Post.find_by_title(title)
        if post:
            return post.json(), 200
        return {'message': 'This post does not exist within the database!'}, 404

    @jwt_required
    def post(self, title):
        if Post.find_by_title(title):
            return {'message': f'A post titled {title} already exists!'}
        
        data = RPost.parser.parse_args()
        post = Post(title, **data)
        try:
            post.save_post()
        except:
            return {'message': 'An error occurred while adding this post!'}, 500
        
        return post.json(), 201

    @jwt_required
    def delete(self, title):
        post = Post.find_by_title(title)
        if post:
            post.delete_post()
        return {'message': 'Success!'}, 410

class PostList(Resource):
    def get(self):
        return {'posts': [post.json() for post in Post.query.all()]}, 200
