import openai
from google.auth import default, transport
from langchain import PromptTemplate
# Build
from langchain_openai import ChatOpenAI
from vertexai.preview import rag
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmBlockThreshold,
    HarmCategory,
    Part,
)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_vertexai import ChatVertexAI

credentials, _ = default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
auth_request = transport.requests.Request()
credentials.refresh(auth_request)


MODEL_LOCATION = "us-central1"
PROJECT_ID='sacred-alliance-433217-e3'
MODEL_ID = "meta/llama3-405b-instruct-maas"  # @param {type:"string"} ["meta/llama3-405b-instruct-maas"]
gemini_model = "google/gemini-1.0-pro"  # @param {type:"string"}

# llm = ChatOpenAI(
#     model=MODEL_ID,
#     base_url=f"https://{MODEL_LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/{MODEL_LOCATION}/endpoints/openapi/chat/completions?",
#     api_key=credentials.token,
#     streaming=True
# )



# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-pro",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2
    
#     # other params...
# )
from langchain_google_vertexai.model_garden_maas.llama import VertexModelGardenLlama
#llm = ChatVertexAI(model_name='llama3-405b-instruct-maas')
llm = ChatVertexAI(model_name= 'gemini-1.0-pro')