#!/usr/bin/env python3
"""
Voice Transcription Tool using OpenAI Whisper API
Transcribes audio files (MP3, WAV, M4A, etc.) to text
"""

import os
import sys
import requests
from pathlib import Path

# API Configuration
API_KEY = os.environ.get("OPENAI_API_KEY", "")
API_URL = "https://api.openai.com/v1/audio/transcriptions"

def transcribe_audio(filepath, model="whisper-1", language=None):
    """
    Transcribe audio file using OpenAI Whisper API
    
    Args:
        filepath: Path to audio file (mp3, mp4, mpeg, mpga, m4a, wav, webm)
        model: Model to use (default: whisper-1)
        language: Optional language code (e.g., 'de', 'en')
    
    Returns:
        dict: API response with transcription text
    """
    if not API_KEY:
        print("❌ Error: OPENAI_API_KEY not set")
        print("Set it with: export OPENAI_API_KEY='your-api-key'")
        return None
    
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return None
    
    # Supported formats
    supported_ext = ['.mp3', '.mp4', '.mpeg', '.mpga', '.m4a', '.wav', '.webm', '.ogg']
    file_ext = Path(filepath).suffix.lower()
    
    if file_ext not in supported_ext:
        print(f"❌ Unsupported format: {file_ext}")
        print(f"Supported: {', '.join(supported_ext)}")
        return None
    
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": model
    }
    
    if language:
        data["language"] = language
    
    try:
        with open(filepath, 'rb') as audio_file:
            files = {
                "file": (os.path.basename(filepath), audio_file)
            }
            
            print(f"🔊 Transcribing: {filepath}")
            print(f"   Format: {file_ext}")
            print(f"   Model: {model}")
            if language:
                print(f"   Language: {language}")
            print("   Uploading...")
            
            response = requests.post(
                API_URL,
                headers=headers,
                data=data,
                files=files,
                timeout=120
            )
            
            if response.status_code == 200:
                result = response.json()
                return result
            else:
                print(f"❌ API Error: {response.status_code}")
                print(f"Response: {response.text}")
                return None
                
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Transcribe audio files using OpenAI Whisper API'
    )
    parser.add_argument('filepath', help='Path to audio file')
    parser.add_argument(
        '--language', '-l',
        help='Language code (e.g., de, en, fr)'
    )
    parser.add_argument(
        '--model', '-m',
        default='whisper-1',
        help='Model to use (default: whisper-1)'
    )
    parser.add_argument(
        '--output', '-o',
        help='Output file for transcription (optional)'
    )
    
    args = parser.parse_args()
    
    if not API_KEY:
        print("❌ OPENAI_API_KEY environment variable not set")
        print("Set it with: export OPENAI_API_KEY='sk-...'")
        sys.exit(1)
    
    result = transcribe_audio(args.filepath, args.model, args.language)
    
    if result:
        text = result.get('text', '')
        
        print("\n" + "=" * 60)
        print("📝 TRANSCRIPTION:")
        print("=" * 60)
        print(text)
        print("=" * 60)
        
        # Save to file if requested
        if args.output:
            with open(args.output, 'w') as f:
                f.write(text)
            print(f"\n💾 Saved to: {args.output}")
        
        # Also copy to clipboard if on macOS
        if sys.platform == 'darwin':
            try:
                import subprocess
                subprocess.run(['pbcopy'], input=text.encode())
                print("📋 Copied to clipboard")
            except:
                pass
        
        return text
    else:
        print("❌ Transcription failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
