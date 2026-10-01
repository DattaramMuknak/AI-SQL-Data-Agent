from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def pick_llm(level: str):

    level = level.lower()

    if level == "low":
        model = "openai/gpt-oss-20b"

    elif level == "medium":
        model = "openai/gpt-oss-120b"

    elif level == "high":
        model = "openai/gpt-oss-120b"

    else:
        raise ValueError(f"Unsupported level: {level}")

    return ChatOpenAI(
        model=model,
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0
    )


if __name__ == "__main__":
    llm = pick_llm("low")
    response = llm.invoke("What is the capital of France?")
    print(response.content)