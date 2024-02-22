import requests

class APIIntegrations:
  def send_request(text, voice_id, chuck_size = 1024, output_file = 'output.mp3' ):
    # Chuck size will be setting automatically
    API_KEY = "" # You will need to have paid plan to get this working
    url = "https://api.elevenlabs.io/v1/text-to-speech/{}/stream".format(voice_id)

    headers = {
      "Accept": "audio/mpeg",
      "Content-Type": "application/json",
      "xi-api-key": "{}".format(API_KEY)
    }

    data = {
      "text": "{}".format(text),
      "model_id": "eleven_monolingual_v1",
      "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
      }
    }

    response = requests.post(url, json=data, headers=headers)
    
    with open(output_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=chuck_size):
            if chunk:
                f.write(chunk)
    
    return output_file

