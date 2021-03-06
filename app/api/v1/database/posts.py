from pymongo import errors

from app import app
from ..assets.error_handlers import custom_response
from ..assets.response import CODES, MIME_TYPES


class PostsDatabase:

    def insert(self):
        try:
            return
        except errors.DuplicateKeyError:
            pass

    def retrieve(self):
        try:
            return
        except Exception as error:
            app.logger.info("Error occurred while retrieving posts rom database.")
            app.logger.exception(error)
            return custom_response("Database connection error.", CODES.get('INTERNAL_SERVER_ERROR'),
                                   MIME_TYPES.get('APPLICATION_JSON'))
