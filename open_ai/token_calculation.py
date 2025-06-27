import tiktoken

# Find the encoding type for the specified model

# For encoding and decodin the text we have to first get the encoding object we can use one of the following methods:
# 1. tiktoken.encoding_for_model(model_name)
# 2. tiktoken.get_encoding(encoding_name)


# encoding_obj = tiktoken.encoding_for_model("gpt-3.5-turbo")
encoding_obj = tiktoken.get_encoding("cl100k_base")

token_ids = encoding_obj.encode("What is the capital of France?")

print("Token Ids: ", token_ids)

testFromToken = encoding_obj.decode(token_ids)

print("Decoded Text: ", testFromToken)

tokens_spend = len(token_ids)

print("Tokens Spend: ", tokens_spend)


# Conclusion: We can use the tiktoken library to know the exact encoding of the text and caluclate the token before sending the request to the OpenAI API. This will help us to avoid the token limit errors and also help us to optimize the prompts for better performance. We can also calculate the token usage for the API calls to manage the costs and optimize the usage.