from openai import OpenAI
from prompts import SYSTEM_PROMPT, USER_PROMPT

class LLM:
    def __init__(self, base_url: str, api_key: str) -> None:
        self.client = OpenAI(base_url=base_url, api_key=api_key)

    def make_completion(self, user_prompt: str, 
                        temperature: float = 0.7, 
                        max_tokens: int = 1024, 
                        stream: bool = False) -> str:
        completion = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT.format(user_prompt=user_prompt)}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            stream=stream
        )
        return completion.choices[0].message.content
    