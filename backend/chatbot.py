from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-api-key-here')
MODEL_NAME = "gpt-3.5-turbo"  # You can change this to other models

# Initialize OpenAI client
try:
    openai.api_key = OPENAI_API_KEY
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
except Exception as e:
    logger.error(f"Failed to initialize OpenAI client: {e}")
    client = None

class ChatbotEngine:
    def __init__(self):
        self.conversation_history = []
        self.max_history = 10
        
    def add_message(self, role, content):
        """Add a message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only the last max_history messages
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
    
    def get_ai_response(self, user_message):
        """Generate AI response using OpenAI API"""
        try:
            if not client:
                return self.get_fallback_response(user_message)
            
            # Prepare conversation context
            messages = [
                {"role": "system", "content": "You are a helpful, friendly, and knowledgeable AI assistant. Provide clear, accurate, and helpful responses to user questions. Keep responses concise but informative."}
            ]
            
            # Add recent conversation history
            for msg in self.conversation_history[-6:]:  # Last 6 messages for context
                if msg["role"] in ["user", "assistant"]:
                    messages.append({"role": msg["role"], "content": msg["content"]})
            
            # Add current user message
            messages.append({"role": "user", "content": user_message})
            
            # Generate response
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                max_tokens=500,
                temperature=0.7,
                timeout=30
            )
            
            ai_response = response.choices[0].message.content
            return ai_response
            
        except Exception as e:
            logger.error(f"Error generating AI response: {e}")
            return self.get_fallback_response(user_message)
    
    def get_fallback_response(self, user_message):
        """Fallback responses when AI service is unavailable"""
        fallback_responses = [
            f"I understand you're asking about '{user_message}'. This is a fallback response as the AI service is currently unavailable. In a production environment, you would typically have access to OpenAI's GPT models or other AI services.",
            f"That's an interesting question about '{user_message}'! I'm currently operating in fallback mode, but normally I'd provide you with detailed AI-generated insights.",
            f"Regarding '{user_message}', I'd love to help you with that! I'm temporarily using fallback responses, but the full AI capabilities would give you much more comprehensive answers.",
            f"Great question about '{user_message}'! I'm in fallback mode right now, but the AI integration would provide you with intelligent, contextual responses.",
            f"I appreciate your question about '{user_message}'. I'm currently using backup responses, but the AI service would offer much more sophisticated assistance."
        ]
        
        import random
        return random.choice(fallback_responses)
    
    def process_message(self, user_message):
        """Process user message and return response"""
        # Add user message to history
        self.add_message("user", user_message)
        
        # Generate AI response
        ai_response = self.get_ai_response(user_message)
        
        # Add AI response to history
        self.add_message("assistant", ai_response)
        
        return {
            "response": ai_response,
            "timestamp": datetime.now().isoformat(),
            "conversation_id": len(self.conversation_history)
        }

# Initialize chatbot engine
chatbot = ChatbotEngine()

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'error': 'Message is required',
                'status': 'error'
            }), 400
        
        # Process message and get response
        result = chatbot.process_message(user_message)
        
        return jsonify({
            'response': result['response'],
            'timestamp': result['timestamp'],
            'conversation_id': result['conversation_id'],
            'status': 'success'
        })
        
    except Exception as e:
        logger.error(f"Error processing chat request: {e}")
        return jsonify({
            'error': 'Internal server error',
            'status': 'error'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'ai_service_available': client is not None
    })

@app.route('/api/conversation', methods=['GET'])
def get_conversation():
    """Get conversation history"""
    return jsonify({
        'conversation': chatbot.conversation_history,
        'status': 'success'
    })

@app.route('/api/conversation', methods=['DELETE'])
def clear_conversation():
    """Clear conversation history"""
    chatbot.conversation_history = []
    return jsonify({
        'message': 'Conversation cleared',
        'status': 'success'
    })

if __name__ == '__main__':
    # Check if OpenAI API key is set
    if OPENAI_API_KEY == 'your-api-key-here':
        logger.warning("OpenAI API key not set. Using fallback responses.")
    
    app.run(debug=True, host='0.0.0.0', port=5000)