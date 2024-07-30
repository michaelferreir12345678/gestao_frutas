Feature: Cadastro de Frutas
  Scenario: Cadastro de uma nova fruta
    Given que estou na página de cadastro de frutas
    When eu preencho o formulário com dados válidos
    And eu submeto o formulário
    Then a fruta deve ser cadastrada com sucesso
