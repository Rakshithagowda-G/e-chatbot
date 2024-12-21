from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# Predefined responses for the chatbot
responses = {
     "hey": {"text": "Hi there! How can I assist you today?", "image": None},
      "hi": {"text": "Hi there! How can I assist you today?", "image": None},
    "hello": {"text": "Hi there! How can I assist you today?", "image": None},
    "help": {"text": "Sure! I can help you with your queries about our e-commerce platform.", "image": None},
    "price": {"text": "Our products range from $10 to $500. What are you looking for?", "image": None},
    "new arrivals": {
        "text": "Check out our latest arrivals!",
        "image": "https://media.istockphoto.com/id/523788889/photo/online-home-appliance-shopping.jpg?s=2048x2048&w=is&k=20&c=vWyDtCE23GN93ddo0za0qGzgtNx9reAjzvNPmsLOyaw="
    },
    "bye": {"text": "Goodbye! Have a great day!", "image": None}, 
     "shipping": {"text": "We offer free shipping on orders over $50. Fast delivery guaranteed!", "image": None},
    "return policy": {"text": "We accept returns within 30 days of purchase. Contact our support for help.", "image": None},
    "payment options": {"text": "We accept credit cards, debit cards, PayPal, and more.", "image": None},
    "gift cards": {"text": "Looking for a perfect gift? Our gift cards start at $25.", "image": "https://example.com/images/gift-cards.jpg"},
    "track order": {"text": "You can track your order by visiting the 'Order Tracking' page on our website.", "image": None},
    "customer support": {"text": "Our customer support team is available 24/7 to assist you.", "image": None},
    "popular items": {"text": "These are our top-selling items this season!", "image": "https://example.com/images/popular-items.jpg"},
    "contact us": {"text": "You can reach us via email at support@example.com or call us at 1-800-123-4567.", "image": None},
    "sales": {"text": "Don't miss out on our seasonal sales with up to 70% off.", "image": "https://example.com/images/sales.jpg"},
    "store hours": {"text": "Our stores are open from 9 AM to 9 PM, Monday to Saturday.", "image": None},
    "holiday deals": {"text": "Check out our special holiday deals and offers!", "image": "https://example.com/images/holiday-deals.jpg"} # Ensure this is correct
}
@app.route('/api/chat/', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "").lower().strip()
        
        # Default response if no match
        response = responses.get(user_message, {"text": "I'm sorry, I didn't understand that. Could you please rephrase?", "image": None})
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"text": "An error occurred. Please try again!", "image": None}), 500

# For testing the API
@app.route('/')
def home():
    return jsonify({"message": "E-Commerce Chatbot API is running!"})

if __name__ == '__main__':
    app.run(debug=True)