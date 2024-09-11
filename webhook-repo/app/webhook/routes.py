from flask import Blueprint, request, jsonify
from ..extensions import mongo  # Importing MongoDB instance

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

# Route to handle GitHub webhook events
@webhook.route('/receiver', methods=["POST"])
def receiver():
    payload = request.json
    event = request.headers.get('X-GitHub-Event')

    # Process the event based on the type
    if event == 'push':
        data = {
            'author': payload['pusher']['name'],
            'to_branch': payload['ref'].split('/')[-1],  # Extract branch name from the ref
            'timestamp': payload['head_commit']['timestamp'],
            'type': 'push'
        }
        message = f"{data['author']} pushed to {data['to_branch']} on {data['timestamp']}"

    elif event == 'pull_request':
        data = {
            'author': payload['pull_request']['user']['login'],
            'from_branch': payload['pull_request']['head']['ref'],
            'to_branch': payload['pull_request']['base']['ref'],
            'timestamp': payload['pull_request']['updated_at'],
            'type': 'pull_request'
        }
        message = f"{data['author']} submitted a pull request from {data['from_branch']} to {data['to_branch']} on {data['timestamp']}"

    elif event == 'pull_request' and payload['action'] == 'closed' and payload['pull_request']['merged']:
        data = {
            'author': payload['pull_request']['user']['login'],
            'from_branch': payload['pull_request']['head']['ref'],
            'to_branch': payload['pull_request']['base']['ref'],
            'timestamp': payload['pull_request']['merged_at'],
            'type': 'merge'
        }
        message = f"{data['author']} merged branch {data['from_branch']} to {data['to_branch']} on {data['timestamp']}"
    
    else:
        # If event is not handled, return a response
        return jsonify({'message': 'Event not supported'}), 400

    # Insert the data into MongoDB
    mongo.db.webhooks.insert_one(data)

    # Return success response
    return jsonify({'message': message}), 200



