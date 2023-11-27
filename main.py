#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import json
openai.api_type = "azure"
openai.api_base = "https://arkano-openai-dev.openai.azure.com/"
openai.api_version = "2023-09-15-preview"

openai.api_key =  "430f140c6a1d4518900a39d4e7c452cd"#os.getenv("OPENAI_API_KEY")

def responder(_dias, _destino):
    dias = _dias
    destino = _destino
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Leer este documento en linea: https://storagearkanopocnorcenus.blob.core.windows.net/colbunpoctravelprediction/MAC007 Manual Gestión de viajes y rendición de gastos.pdf y calcular el costo en USD o CLP segun corresponda por dia de los viaticos de un empleado que estará "+str(dias)+" dias en "+str(destino)+". Solamente tener en cuenta los gastos diarios en comida y traslados. Excluir los demas items de gastos.",
        temperature=0,
        max_tokens=227,
        top_p=0.73,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None)
    return response

_cant_dias = int(input("Cantidad de días: "))
_destino = str(input("Destino del viaje: "))

resp = responder(_cant_dias, _destino)
print(resp.choices[0].text)