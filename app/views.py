from flask import jsonify
from datetime import datetime
from app import app

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({
        'status': 'OK',
        'timestamp': datetime.utcnow().isoformat()
    }), 200
