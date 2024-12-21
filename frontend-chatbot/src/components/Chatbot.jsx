
import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./Chatbot.css";
import { faUser } from "@fortawesome/free-solid-svg-icons";


const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");
  const chatDisplayRef = useRef(null);

  // Scroll to the bottom of the chat whenever messages change
  useEffect(() => {
    if (chatDisplayRef.current) {
      chatDisplayRef.current.scrollTo({
        top: chatDisplayRef.current.scrollHeight,
        behavior: "smooth",
      });
    }
  }, [messages]);

  const addMessage = (message, sender) => {
    setMessages((prev) => [
      ...prev,
      { text: message.text, image: message.image, sender },
    ]);
  };

  const handleSendMessage = async () => {
    const trimmedInput = userInput.trim();
    if (trimmedInput) {
      addMessage({ text: trimmedInput }, "user");
      setUserInput("");

      try {
        const response = await axios.post("http://127.0.0.1:5000/api/chat/", {
          message: trimmedInput,
        });
        addMessage(response.data, "bot");
      } catch (error) {
        addMessage(
          { text: "Something went wrong. Please try again!", image: null },
          "bot"
        );
      }
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSendMessage();
    }
  };

  return (
    <div className="chatbot-container">
      <div className="chatbot-header"> 
      E-Commerce Chatbot
     
</div>
      <div className="chat-display" ref={chatDisplayRef}>
      
        {messages.map((message, index) => (
          <div key={index} className={`chat-message ${message.sender}`}>
            {message.text && <p>{message.text}</p>}
            {message.image && (
              <img src={message.image} alt="response" className="chat-image" />
            )}
          </div>
        ))}
      </div>
      <div className="chat-input-container">
        <input
          type="text"
          className="chat-input"
          placeholder="Type a message..."
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          onKeyPress={handleKeyPress}
        />
        <button className="chat-send-button" onClick={handleSendMessage}>
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbot;
