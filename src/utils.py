import os

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


chat = ChatOpenAI(
    model_name="gpt-4-turbo-preview",
    temperature=0.5
)


def check_password(password):
    return password == os.environ["USER_AUTH_KEY"]


def get_response(query, chat_history):
    template = """
    Use the following pieces of chat history and user question to answer the query at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    
    Chat history: {chat_history}

    User question: {user_question}
    
    Helpful Answer:
    """

    system_template = SystemMessagePromptTemplate.from_template("Act as Alex Hormozi. Answer the following questions "
                                                                "in the style of Alex Hormozi.")

    user_prompt = HumanMessagePromptTemplate.from_template(template)

    prompt = ChatPromptTemplate.from_messages([system_template, user_prompt])

    chain = prompt | chat | StrOutputParser()

    return chain.stream({
        "chat_history": chat_history,
        "user_question": query
    })
