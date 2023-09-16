from flask import Flask, request
from flask import jsonify
from dotenv import load_dotenv
from news_service import fetch_news
from flask_cors import CORS, cross_origin

import messages
import constants
import logging

logger = logging.getLogger(__name__)
load_dotenv()

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/search', methods=['POST'])
@cross_origin(supports_credentials=True)
def search_news():
    try:
        search_term = request.args.get('query')
        number_of_results = 10
        logger.info(f"request query: {search_term}, number_of_results: {number_of_results}")
        result = fetch_news(search_term, number_of_results)
        logger.info(f"request processed successfully.")
        if result:
            return jsonify({
                'message': messages.NEWS_FETCHED_SUCCESSFULLY,
                'data': result
            }), constants.HTTPS_STATUS_200
        else:
            return jsonify({
                'message': messages.FAILED_TO_FETCH_NEWS,
                'data': {}
            }), constants.HTTPS_STATUS_422

    except Exception as e:
        logger.error(f"error while serving request {str(e)}")
        return jsonify({
            'message': messages.SERVER_ERROR,
            'data': {}
        }), constants.HTTPS_STATUS_500


if __name__ == '__main__':
    app.run(debug=True)
