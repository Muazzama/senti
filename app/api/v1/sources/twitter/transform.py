from app import app
from ...assets.error_handlers import custom_response
from ...assets.response import CODES, MIME_TYPES



class TransformData:

    def __init__(self, data):
        self.data = data

    def transform(self):
        try:
            return
        except Exception as error:
            app.logger.info("Error occurred while transforming twitter data.")
            app.logger.exception(error)
            return custom_response("Database connection error.", CODES.get('INTERNAL_SERVER_ERROR'),
                                   MIME_TYPES.get('APPLICATION_JSON'))
