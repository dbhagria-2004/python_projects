from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from langchain.prompts import PromptTemplate



model = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1")

llm = HuggingFacePipeline(pipeline=model)

template = PromptTemplate.from_template("Explain the {topic} in detail for a {age} group person")

chain = template | llm

topic =input("Topic")
age = input("Age")

response = chain.invoke({"topic" : topic, "age" : age})

print(response)