Webservice
===========

Exemplo de webservice que coleta informações de usuários do facebook e as fornece por meio de um serviço.


Como executar
==============

Instale todos as bibliotecas necessárias com:
    `pip install -r requirements.txt`


Primeiro você precisa criar as tabelas do projeto, para isso execute o comando:

    `python manage.py create_tables`

Para rodar o servidor, execute:

    `python manage.py runserver`


Exemplos de requisições
=======================

    * Listar todos os dados
        GET http://localhost:5000/person/

    * Incluir usuário
        POST http://localhost:5000/person/ {facebookId: 12312312}

    * Excluir usuário
        DELETE http://localhost:5000/person/<facebookId>


Testes
=======

Para executar os testes rode:
   `nosetests tests/`


Para visualizar o relatório de cobertura execute:
    `nosetests tests/ --with-coverage --cover-package=webservice`

