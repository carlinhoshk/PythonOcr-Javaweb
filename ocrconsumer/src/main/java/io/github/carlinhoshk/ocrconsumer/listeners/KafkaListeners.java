package io.github.carlinhoshk.ocrconsumer.listeners;

import com.fasterxml.jackson.databind.ObjectMapper;
import io.github.carlinhoshk.ocrconsumer.entities.Pessoa;
import io.github.carlinhoshk.ocrconsumer.repository.PessoaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaListeners {

    @Autowired
    private PessoaRepository pessoaRepository;

    @KafkaListener(topics = "ocr", groupId = "ocr-producer")
    public void listener(String pessoa) {
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            Pessoa p = objectMapper.readValue(pessoa, Pessoa.class);

            pessoaRepository.save(p);
            System.out.println("Recebido: " + p);
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
