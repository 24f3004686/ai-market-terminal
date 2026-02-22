import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_analyze(asset, indicators):
    prompt = f"""
You are a professional financial analyst.

Asset: {asset}

Market indicators:
{indicators}

Give:
1. Trend (Bullish/Bearish/Sideways)
2. Momentum analysis
3. Risk level
4. Short-term outlook
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
