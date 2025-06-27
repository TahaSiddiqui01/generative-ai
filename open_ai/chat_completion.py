# Used for the ChatCompletion API. OPEN AI api can be used to generate any type of text response like code, mathematical equations etc.and

from openai import OpenAI

client = OpenAI()

def chat_completion(query, model="gpt-3.5-turbo", temperature=0.7, max_tokens=150):
    response = client.responses.create(
        input=query,
        model=model,
        max_output_tokens=max_tokens,
        temperature=temperature,
    )

    return response.output_text


# chatOutput = chat_completion("What is the capital of France?", temperature=0)
# print(chatOutput)

# Prompt engineering is a technique used to generate the efficient responses fromt he AI models that match the expected output and fulfill the business requirements. Prompt engineering is an art and science of crafting the input prompts to get the desired output from the AI models. It involves understanding the model's behavior, capabilities, and limitations, and designing prompts that guide the model to produce the most relevant and accurate responses.

# Prompt engineering should be adaptive as the same prompt against differnt models may generate different responses so it is recommended we have to stick to the specific model for the consistency

# We can build evals to measure the performance of the model with different prompts.


# We can use he structured messsage to teach the model about the logical boundries of the prompt and context data usingt the Mardown and XMl tags. It increase the readability of your prompt and helps the model to understand the context better.

# A strucuture message can contan the following parts:

# 1. Identity: Defines purpose, high level goal and the communication behaviour
# 2. Instructions: Provides the specific instructions to the model on how to respond
# 3. Context: Provides the context data to the model to understand the problem better
# 4. Examples: Provides the examples to the model to understand the problem better by providing the input and the desired output



def generate_tech_roadmap(topic, deadline):
    prompt = f"""
    Create a detailed roadmap of the '{topic}' within the deadline of '{deadline}'. This roadmap should include everything that helps both beginne and experts. The roadmap should be strucutured in a way that there should be some engagement to the user even the have vary ing levels of expertise. The roadmap should be divided into different sections, each section should have a clear objective and a set of tasks to achieve that objective. The roadmap should also include the resources required to complete the tasks, the estimated time to complete each task, and the expected outcome of each task. 
    Note: The roadmap should atleast explain what, why and how of the topic. If there is any math or science it should also explain that intuition.
    """

    response = client.responses.create(
        instructions="Act as a roadmap generator for technology topics.",
        input=prompt,
        model="gpt-3.5-turbo",
    )

    # The above code can be written as given below

    # response = client.responses.create(
    #     input= [
    #         {
    #             "role": "developer",
    #             "content": "Act as a roadmap generator for technology topics."
    #         },
    #         {
    #             "role": "user",
    #             "content": prompt
    #         }
    #     ]
    # )

    return response.output_text

def generate_tech_roadmap_with_sm(topic, deadline):

    # Using the structured message to generate the roadmap, context part is missing but you can add it by creating a context variable and passing it to the prompt

    prompt = f"""
    <identity>
        <purpose>Generate a detailed roadmap for the topic '{topic}' within the deadline '{deadline}'.</purpose>
        <goal>Provide a comprehensive roadmap that is engaging for both beginners and experts.</goal>   
        <communication_behaviour>Use clear and structured language to explain the roadmap.</communication_behaviour>
    </identity>

    <instructions>
    <objective>Create a roadmap that is divided into different sections, each section should have a clear objective and a set of tasks to achieve that objective.</objective>
    <tasks>Include the resources required to complete the tasks, the estimated time to complete each task, and the expected outcome of each task.</tasks>
    <note>The roadmap should explain the what, why, and how of the topic. If there is any math or science involved, it should also explain the intuition behind it.</note>
    </instructions>

    <examples>
        <example> For ML roadmap, include sections on data preprocessing, model selection, training, evaluation, and deployment.</example>
    </examples>
    """

    response = client.responses.create(
        instructions="Act as a roadmap generator for technology topics.",
        input=prompt,
        model="gpt-3.5-turbo",
    )


    return response.output_text



# my_roadmap = generate_tech_roadmap("Next.js", "15 days")
my_roadmap = generate_tech_roadmap_with_sm("ML", "15 days")

print(my_roadmap)