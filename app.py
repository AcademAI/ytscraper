from flask import Flask, request, jsonify
from flask_cors import CORS
import scrapetube

app = Flask(__name__)
# docker inspect -f '{{.NetworkSettings.Networks.[Network].IPAddress}}' [container]
CORS(app, origins='http://0.0.0.0:3000')

@app.route('/search', methods=['GET', 'OPTIONS'])
def search():
    search_query = request.args.get('searchQuery')
    max_results = int(request.args.get('maxResults'))

    videos = scrapetube.get_search(search_query, max_results)
    video_ids = [video['videoId'] for video in videos]
    print(f'ГЕНЕРАТОР СОЗДАННЫЙ ИЗ ГЕНЕРАТОРА НА 1 ШАГЕ{video_ids}')

    # Collect all video_ids into a list
    video_ids_list = list(video_id for video_id in video_ids)
    print(f'СЕТ СОЗДАННЫЙ ИЗ СЕТА НА 2 ШАГЕ{video_ids_list}')

    return jsonify(video_ids_list)

if __name__ == '__main__':
    app.run(debug=False, port=8224, host='0.0.0.0')
