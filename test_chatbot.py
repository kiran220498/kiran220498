#!/usr/bin/env python3
"""
Simple test script for the chatbot backend
"""

import requests
import json
import time

def test_chatbot():
    """Test the chatbot endpoints"""
    base_url = "http://localhost:5000"
    
    print("🧪 Testing Chatbot Backend")
    print("=" * 40)
    
    # Test health endpoint
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/api/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data['status']}")
            print(f"   AI service available: {data['ai_service_available']}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend. Is it running?")
        return False
    
    # Test chat endpoint
    print("\n2. Testing chat endpoint...")
    test_messages = [
        "Hello, how are you?",
        "What's the weather like today?",
        "Can you help me with programming?",
        "Tell me a joke"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n   Testing message {i}: '{message}'")
        try:
            response = requests.post(
                f"{base_url}/api/chat",
                json={"message": message},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Response received: {data['response'][:100]}...")
                print(f"   📝 Timestamp: {data['timestamp']}")
                print(f"   🆔 Conversation ID: {data['conversation_id']}")
            else:
                print(f"   ❌ Chat failed: {response.status_code}")
                print(f"   Error: {response.text}")
            
            # Small delay between requests
            time.sleep(1)
            
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request failed: {e}")
    
    # Test conversation history
    print("\n3. Testing conversation history...")
    try:
        response = requests.get(f"{base_url}/api/conversation")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Conversation history retrieved")
            print(f"   Messages in history: {len(data['conversation'])}")
        else:
            print(f"❌ Failed to get conversation history: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to get conversation history: {e}")
    
    print("\n" + "=" * 40)
    print("🎉 Testing completed!")
    return True

if __name__ == "__main__":
    test_chatbot()