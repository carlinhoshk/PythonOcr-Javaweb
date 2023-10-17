from confluent_kafka import Consumer, KafkaError
import cv2
import numpy as np


def kafka_image_consumer(topic, group_id):
    consumer_config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': group_id,
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(consumer_config)
    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f'Erro no Kafka: {msg.error())
                break

        image_bytes = msg.value()
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
        return image  # Retorna a imagem decodificada

    consumer.close()
