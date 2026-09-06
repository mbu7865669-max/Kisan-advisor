import asyncio
import os
from tools import get_crop_information, get_weather, get_market_price

from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

# Load API key from .env
load_dotenv()

# We are using Gemini instead of an OpenAI API key
set_tracing_disabled(True)

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
model="gemini-3.6-flash",
    openai_client=client,
)

agent = Agent(
    name="Kisan Advisor",
    instructions="""
    You are Kisan Advisor, an AI agricultural assistant for Pakistani farmers.

    Help farmers understand:
    1. What crops may be suitable for them.
    2. How they can protect their crops.
    3. When they should consider selling their crops.

    Give practical, simple answers.
    Do not invent weather or market prices.
    If information is unavailable, clearly say so.
    """,
    model=model,
    tools=[get_crop_information,get_weather,get_market_price]
)


async def main():
    print("\n==============================")
    print("     KISAN ADVISOR")
    print("==============================")
    print("Ask me anything about agriculture.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Farmer: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        result = await Runner.run(
            agent,
            user_input
        )

        print("\nKisan Advisor:", result.final_output)
        print()

if __name__ == "__main__":
    asyncio.run(main())