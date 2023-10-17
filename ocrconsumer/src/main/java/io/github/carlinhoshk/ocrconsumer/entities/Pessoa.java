package io.github.carlinhoshk.ocrconsumer.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Table(name = "pessoas")
@Entity(name = "pessoas")
@Getter
@NoArgsConstructor
@AllArgsConstructor
public class Pessoa {
    @Id
    private String id;

    private String nome;
    private String nascimento;
}
