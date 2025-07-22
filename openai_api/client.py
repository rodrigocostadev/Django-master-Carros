from openai import OpenAI
from django.conf import settings


client = OpenAI(
    # api_key = 'INSERIR API KEY'
    api_key=settings.OPENAI_API_KEY
)

def get_car_ai_bio(model, brand, year):

    message= """
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas sobre esse modelo.
    """

    message = message.format(brand, model, year)

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message
             },
        ],
        model='gpt-3.5-turbo',  # ou 'gpt-4' se preferir        
        max_tokens=250,
        temperature=0.7,
    )
    return response.choices[0].message.content # O response vai ser um JSON, a chave de acesso ao valor da resposta é choices, e 0 para pegar o primeiro valor




