import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
auction_numbers = []
total_players = 0
current_player_index = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_auction():
    global auction_numbers, total_players, current_player_index
    try:
        total_players = int(request.form['total_players'])
        if total_players < 1:
            return jsonify({"error": "Please enter a number greater than 0."}), 400
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid input. Please enter a valid number."}), 400

    auction_numbers = list(range(1, total_players + 1))
    random.shuffle(auction_numbers)
    current_player_index = 0
    return jsonify({"success": True})

@app.route('/next_player', methods=['POST'])
def next_player():
    global current_player_index, auction_numbers, total_players
    if current_player_index < total_players:
        number = auction_numbers[current_player_index]
        current_player_index += 1
        is_last = current_player_index >= total_players
        return jsonify({
            "number": number,
            "progress": f"[{current_player_index}/{total_players}]",
            "is_last": is_last
        })
    else:
        return jsonify({"number": "Auction Complete", "is_last": True})

if __name__ == '__main__':
    app.run(debug=True)
