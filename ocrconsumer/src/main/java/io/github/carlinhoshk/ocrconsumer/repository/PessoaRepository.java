package io.github.carlinhoshk.ocrconsumer.repository;

import io.github.carlinhoshk.ocrconsumer.entities.Pessoa;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PessoaRepository extends JpaRepository<Pessoa, String> {
}
