from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema.messages import HumanMessage


def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo",
                       openai_api_key=openai_api_key,
                       base_url="https://api.aigc369.com/v1"
                       )
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

# memory = ConversationBufferMemory(return_messages=True)
# answer = get_chat_response("李白的历史文学地位",memory,"sk-kQ0D1f1Ltj9vGcZWrRgpO5Yj3IDU6zoGqTVi911vVtmQ6GBf")
# print(answer)