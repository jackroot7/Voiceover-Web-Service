import os
from ninja import NinjaAPI
from utils.dto import QueryParams
from utils.elab import APIIntegrations
api = NinjaAPI()

@api.post("/gererate_voice_from_text")
def voice_to_text_generation(request, params: QueryParams):
    # Generate PDF file for report
    out_put_file = APIIntegrations.send_request(text = params.text, voice_id = params.voice_id, chuck_size = params.chuck_size)
    
    if os.path.isfile(out_put_file):
        return {'code': 200, "out_put_file":out_put_file}
    
    return {'code': 400, "message": "Fail to generate voice. Try to change parameters"}