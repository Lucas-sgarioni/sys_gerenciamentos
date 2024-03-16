# desafio_microsservico

Desafio: Sistema de Pedidos e Pagamentos

Objetivo: Desenvolver dois microserviços em Python que se comuniquem via REST API. O primeiro microserviço será responsável pelo gerenciamento de pedidos, enquanto o segundo lidará com os pagamentos.

Microserviço 1: Gerenciamento de Pedidos
Tecnologias:
Banco de Dados: Utilize um banco de dados relacional como PostgreSQL para armazenar os detalhes dos pedidos.
Cache: Implemente um cache Redis para armazenar informações de pedidos frequentemente acessadas, reduzindo a carga no banco de dados.
REST API: Exponha endpoints para criar, atualizar, visualizar e deletar pedidos.
Funcionalidades:
Criar um novo pedido.
Atualizar um pedido existente.
Visualizar detalhes de um pedido específico.
Deletar um pedido.
Listar todos os pedidos.

Microserviço 2: Sistema de Pagamentos
Tecnologias:
Banco de Dados: Utilize um banco de dados como PostgreSQL para armazenar os detalhes dos pagamentos.
Mensageria: Implemente um sistema de mensageria usando AWS SQS para processar pagamentos de forma assíncrona.
REST API: Exponha endpoints para processar e verificar o status de pagamentos.
Funcionalidades:
Processar um pagamento para um pedido específico.
Verificar o status de um pagamento.
Listar todos os pagamentos.
Integração entre os Microserviços
Quando um pedido é criado no microserviço de gerenciamento de pedidos, ele deve enviar uma mensagem para a fila do AWS SQS, que será consumida pelo microserviço de pagamentos para iniciar o processamento do pagamento.
O microserviço de pagamentos deve atualizar o status do pagamento no banco de dados e enviar uma atualização para o microserviço de pedidos.
Requisitos Adicionais
Implementar autenticação JWT para proteger as APIs.
Utilize Docker para conteinerizar os microserviços e suas dependências.