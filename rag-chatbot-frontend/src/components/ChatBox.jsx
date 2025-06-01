import React, { useState } from "react";
import axios from "axios";

const ChatBox = () => {
  const [question, setQuestion] = useState("");
  const [chatLog, setChatLog] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!question.trim()) return;

    const userMsg = { type: "user", message: question };
    setChatLog((prev) => [...prev, userMsg]);
    setQuestion("");

    try {
      const response = await axios.post("http://127.0.0.1:8000/ask", {
        query: question,
      });
      const botMsg = { type: "bot", message: response.data.answer };
      setChatLog((prev) => [...prev, botMsg]);
    } catch (error) {
      console.error("Error:", error);
      const errorMsg = { type: "bot", message: "❌ Error contacting backend." };
      setChatLog((prev) => [...prev, errorMsg]);
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "600px", margin: "auto" }}>
      <h2>LangChain + Gemini ChatBot 💬</h2>
      <div style={{ border: "1px solid #ccc", padding: "1rem", height: "300px", overflowY: "auto" }}>
        {chatLog.map((msg, idx) => (
          <p key={idx} style={{ textAlign: msg.type === "user" ? "right" : "left" }}>
            <strong>{msg.type === "user" ? "You" : "Bot"}:</strong> {msg.message}
          </p>
        ))}
      </div>
      <form onSubmit={handleSubmit} style={{ marginTop: "1rem" }}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask a question..."
          style={{ width: "80%", padding: "0.5rem" }}
        />
        <button type="submit" style={{ padding: "0.5rem" }}>Send</button>
      </form>
    </div>
  );
};

export default ChatBox;
