# AI Chatbot

A modern, responsive chatbot application built with React and Python Flask, featuring AI-powered responses and a beautiful user interface.

## Features

- 🚀 **Modern React UI** with Tailwind CSS styling
- 🤖 **AI Integration** with OpenAI GPT models (optional)
- 💬 **Real-time Chat** with message history
- 🔄 **Fallback Responses** when AI service is unavailable
- 📱 **Responsive Design** that works on all devices
- ⚡ **Fast Performance** with optimized rendering
- 🎨 **Beautiful Animations** and loading states

## Project Structure

```
├── src/
│   ├── components/
│   │   └── Chatbot.jsx          # Main chatbot component
│   └── App.jsx                   # App with chatbot route
├── backend/
│   ├── chatbot.py                # Python Flask backend
│   ├── requirements.txt          # Python dependencies
│   └── .env.example             # Environment variables template
└── README_CHATBOT.md            # This file
```

## Quick Start

### Frontend (React)

1. **Navigate to the project directory:**
   ```bash
   cd /workspace
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Access the chatbot:**
   - Open your browser and go to `http://localhost:5173/chatbot`
   - Or navigate to the chatbot route from your main application

### Backend (Python Flask)

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env file and add your OpenAI API key if desired
   ```

5. **Start the Flask server:**
   ```bash
   python chatbot.py
   ```

   The backend will run on `http://localhost:5000`

## Configuration

### OpenAI Integration (Optional)

To enable AI-powered responses:

1. **Get an OpenAI API key:**
   - Sign up at [OpenAI](https://openai.com/)
   - Generate an API key in your dashboard

2. **Set the environment variable:**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
   
   Or add it to your `.env` file:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

3. **Restart the backend server**

### Without OpenAI API

The chatbot will work perfectly fine without an API key, using intelligent fallback responses that simulate AI behavior.

## Usage

### Basic Chat

1. Type your message in the input field
2. Press Enter or click the Send button
3. The chatbot will respond with relevant information
4. View your conversation history in the chat window

### Features

- **Message History**: All conversations are stored in the current session
- **Loading States**: Visual feedback while the chatbot is processing
- **Error Handling**: Graceful fallbacks if services are unavailable
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## API Endpoints

The backend provides several endpoints:

- `POST /api/chat` - Send a message and get a response
- `GET /api/health` - Check server and AI service status
- `GET /api/conversation` - Get conversation history
- `DELETE /api/conversation` - Clear conversation history

## Customization

### Styling

The chatbot uses Tailwind CSS classes. You can customize the appearance by modifying the classes in `Chatbot.jsx`.

### Response Logic

Modify the `generateResponse` function in the Python backend to implement custom response logic or integrate with other AI services.

### Models

Change the `MODEL_NAME` variable in `chatbot.py` to use different OpenAI models:
- `gpt-3.5-turbo` (default, fast and cost-effective)
- `gpt-4` (more capable, higher cost)
- `gpt-4-turbo` (latest model with improved performance)

## Troubleshooting

### Backend Connection Issues

- Ensure the Flask server is running on port 5000
- Check that CORS is properly configured
- Verify the backend URL in the React component

### API Key Issues

- Confirm your OpenAI API key is valid
- Check that the environment variable is properly set
- Ensure you have sufficient API credits

### Performance Issues

- The chatbot includes conversation history management to prevent memory issues
- Consider adjusting the `max_history` parameter in the Python backend
- Monitor API rate limits if using OpenAI

## Development

### Adding New Features

1. **Frontend**: Modify `Chatbot.jsx` to add new UI elements
2. **Backend**: Extend `chatbot.py` with new endpoints or logic
3. **Styling**: Use Tailwind CSS classes for consistent design

### Testing

- Test the chatbot with various input types
- Verify fallback responses work when backend is unavailable
- Check responsive design on different screen sizes

## Deployment

### Frontend

Build the React app for production:
```bash
npm run build
```

Deploy the `dist` folder to your hosting service.

### Backend

Deploy the Python backend to your preferred hosting service:
- **Heroku**: Use the `requirements.txt` file
- **AWS**: Use Elastic Beanstalk or Lambda
- **Docker**: Create a Dockerfile for containerization

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the console logs for error messages
3. Verify all dependencies are properly installed
4. Ensure environment variables are correctly set

---

**Enjoy chatting with your AI assistant! 🤖✨**