from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/trends")
async def trends(
    token: str = Form(...),
    team_id: str = Form(...),
    team_domain: str = Form(...),
    channel_id: str = Form(...),
    channel_name: str = Form(...),
    user_id: str = Form(...),
    user_name: str = Form(...),
    command: str = Form(...),
    text: str = Form(...),
    response_url: str = Form(...),
    trigger_id: str = Form(...)
):
    return JSONResponse({
        "response_type": "in_channel",
        "text": "📊 *Here are your test trends:*",
        "attachments": [{"text": "🔍 Reddit: r/ChatGPT, r/SideHustle\n📈 Google: AI Stocks\n📺 YouTube: MrBeast"}]
    })
