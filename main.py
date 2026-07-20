from langchain.agents import AgentExecutor
from orquestador import AgenteOrquestador

def main():
    agente = AgenteOrquestador()
    ejecutor = AgentExecutor(
                    agent = agente.agente,
                    tools = agente.tools,
                    verbose = True
                )
    
    pregunta = "Ayudame a entender la varianza en fianzas"

    respuesta = ejecutor.invoke({"input" : pregunta})

    print(respuesta)

if __name__=="__main__":
    main()