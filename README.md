# E-Commerce Chatbot

This project is an E-Commerce Chatbot built using React for the frontend and Flask for the backend. The chatbot can respond to various user queries and display both text and images dynamically.

---

## Features

- **Dynamic Responses**: Provides predefined responses to user queries.
- **Image Support**: Displays images for specific responses.
- **Smooth Scrolling**: Automatically scrolls to the latest message.
- **Interactive Design**: User-friendly interface with a modern look.
- **Customizable**: Easily extendable for additional queries and responses.

---

## Technologies Used

### Frontend
- **React**: JavaScript library for building user interfaces.
- **CSS**: Styling for the chatbot UI.

### Backend
- **Flask**: Lightweight Python web framework.
- **Flask-CORS**: Handles cross-origin resource sharing.

---

## Setup and Installation

### Prerequisites
Ensure you have the following installed:
- Node.js (for React)
- Python (for Flask)

### Frontend Setup
1. Navigate to the `frontend` folder.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```

### Backend Setup
1. Navigate to the `backend` folder.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask server:
   ```bash
   python app.py
   ```

---

## Usage
1. Start the frontend and backend servers as described in the setup.
2. Open the React application in your browser (typically at `http://localhost:3000`).
3. Interact with the chatbot by typing messages in the input box.

---

## Sample User Queries

- `hello`
- `help`
- `price`
- `new arrivals`
- `shipping`
- `return policy`

---

## File Structure

### Frontend
- **`src/components/Chatbot.js`**: Chatbot logic and rendering.
- **`src/Chatbot.css`**: Styles for the chatbot interface.

### Backend
- **`app.py`**: Flask server with chatbot API.
- **`responses`**: Predefined chatbot responses.

---

## API Endpoints

### `/api/chat/`
- **Method**: POST
- **Payload**:
  ```json
  {
    "message": "<user_message>"
  }
  ```
- **Response**:
  ```json
  {
    "text": "<response_text>",
    "image": "<response_image_url>"
  }
  ```

---

## Contribution
Feel free to fork the repository and submit pull requests for new features, bug fixes, or enhancements.

---

## License
This project is licensed under the MIT License.

---

## Contact
For questions or feedback, reach out to [rakshithag043@gmail.com].

