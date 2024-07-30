Feature: Cadastro de Venda

  Scenario: Cadastro de venda com dados válidos
    Given Eu estou na página de cadastro de vendas
    When Eu seleciono uma fruta e um vendedor, e preencho a quantidade e o desconto
    And Eu clico no botão de cadastrar venda
    Then A venda deve ser cadastrada com sucesso
