import os
import sys
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()


def main():
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        google_api_key=os.getenv("GEMINI_KEY"),
    )

    prompt_template = PromptTemplate(
        input_variables=["text"],
        template="You are a helpful assistant that translates English to Spanish. Translate the user sentence.\n\n{text}"
    )

    formatted_prompt = prompt_template | model
    ai_msg = formatted_prompt.invoke(input={"text":sys.argv[1]})
    print(ai_msg.content)


if __name__ == "__main__":
    main()
