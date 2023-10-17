import json
from confluent_kafka import KafkaError



def enviar_json_kafka(producer, topic, key, mensagem):
    try:
        mensagem_json = json.dumps(mensagem)
        producer.produce(topic, key=key, value=mensagem_json.encode('utf-8'))
        producer.flush()
        print(f'Mensagem JSON enviada com sucesso para o tópico: {topic}')
    except KafkaError as e:
        print(f'Erro ao enviar a mensagem JSON para o tópico {topic}: {str(e)}')
