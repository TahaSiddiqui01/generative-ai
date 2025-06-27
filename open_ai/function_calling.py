from openai import OpenAI
import json
import os
client = OpenAI()
tools = [{
    "type": "function",
    "name": "best_candidate",
    "description": "It will check whether the candidate is eligible based on their programming languages.",
    "parameters": {
        "type": "object",
        "properties": {
            "programming_languages": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "The programming languages the candidate is proficient in."
            }
        },
        "required": ["programming_languages"],
        "additionalProperties": False
    },
    "strict": True
}]


def best_candidate(programming_languages):
    eligible_languages = ["python", "go", "ruby", "rust", "elixir", "c++"]
    matched = [lang for lang in programming_languages if lang.lower() in eligible_languages]
    if matched:
        return f"You are eligible for the job because you know: {', '.join(matched)}."
    return "You are not eligible for the job based on your programming languages."


input_messages = [{"role": "user", "content": "My programming languages are GO and C++. Can you check if I am eligible for the job?"}]

response = client.responses.create(
    model="gpt-3.5-turbo-0125",
    input=input_messages,
    tools=tools,
)

print("Response: ", response.output)

tool_call = response.output[0]
args = json.loads(tool_call.arguments)

result = best_candidate(args["programming_languages"])

input_messages.append(tool_call)
input_messages.append({
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
})

response_2 = client.responses.create(
    model="gpt-3.5-turbo-0125",
    input=input_messages,
    tools=tools,
)
print(response_2.output_text)