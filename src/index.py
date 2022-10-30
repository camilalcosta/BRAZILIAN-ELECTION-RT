
import requests
import json
import pandas as pd
from time import sleep
from datetime import datetime


def show_results():

    while True:
        result_data = requests.get("https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json")
        if not result_data.status_code == 200:
            print(f"TSE Retornou {result_data.status_code}")
        else:
            json_data = json.loads(result_data.content)
            candidato = []
            votos = []
            porcentagem = []

            for dado in json_data['cand']:
                if dado['seq'] == '1' or dado['seq'] == '2' or dado['seq'] == '3' or dado['seq'] == '4' or\
                        dado['seq'] == '5' or dado['seq'] == '6':
                    candidato.append(dado['nm'])
                    votos.append(dado['vap'])
                    porcentagem.append(dado['pvap'])

            df = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=['Candidato', 'Nº Votos', 'Porcentagem'])

            timestamp = datetime.now()

            print('Ultima Atualização:', timestamp.hour, ':', timestamp.minute, ':', timestamp.second, '\n')
            print(df)

        # updating time 5 secs
        sleep(5)



