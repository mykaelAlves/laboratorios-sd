Inicie o Docker: Certifique-se de que o daemon do Docker esteja em execução.

Construa e Execute o Projeto:

    No Linux ou macOS, execute o script: ./buildAndRun.sh

    No Windows, execute o script: buildAndRun.bat

Aguarde a Inicialização: Espere até que o servidor Open Liberty esteja completamente inicializado. Você pode acompanhar os logs com o comando docker logs -f CONTAINER_ID.

Acesse a Aplicação: Abra seu navegador e acesse a URL: http://localhost:9080/resources/sample