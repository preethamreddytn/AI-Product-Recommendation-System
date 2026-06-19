from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
parser = JsonOutputParser()
app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/product")
def get_product(name: str):
    disc = aiapi(name)
    if not disc:
        raise HTTPException(status_code=404, detail="Product not found")
    return disc


def aiapi(name):
    llm = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

    prompt = PromptTemplate.from_template("""
You are an expert product recommendation assistant.

The user is looking for: {product}
Assume region as India.
Recommend 5 suitable products in this category.

Return the response ONLY as valid JSON in this exact format, with no additional text:
{{
  "recommendations": [
    {{
      "name": "Product name",
      "price": "Price in INR",
      "Description": "Brief description of the product",
      "reason": "Why this product is recommended"
    }},
    {{
      "name": "Product name",
      "price": "Price in INR",
      "Description": "Brief description of the product",
      "reason": "Why this product is recommended"
    }}
  ]
}}
If product name is invalid or irrelevant, give null values or proper message.
Make sure to provide exactly 5 products. Each product must have all four fields: name, price, Description, and reason.
""")
    
    chain = prompt | llm | parser
    response = chain.invoke({"product": name})
    return response




