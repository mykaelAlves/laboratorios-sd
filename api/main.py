from flask import Flask, Response

# 1. Cria a aplicação Flask
app = Flask(__name__)

# 2. Define a rota (o endereço URL)
# O <nome> na URL é uma variável dinâmica que será passada para a função.
# Nota: Para manter a simplicidade MÁXIMA em um único arquivo,
# ignorei os prefixos /HelloAPI/api. A rota será direta.
@app.route("/HelloAPI/api/hello/<nome>")
def say_hello(nome):
    """
    Esta função é executada quando o endereço /hello/<qualquer_coisa> é acessado.
    """
    # 3. Cria a mensagem de resposta, usando a variável 'nome' da URL.
    #    A mensagem é exatamente a que você pediu.
    mensagem = f"Olá, {nome}! Bem-vindo à API EJB."

    # 4. Retorna a resposta como texto simples (text/plain) com codificação UTF-8
    #    para garantir que os acentos ("Olá") funcionem corretamente.
    return Response(mensagem, mimetype='text/plain; charset=utf-8')

# 5. Executa o servidor de desenvolvimento
if __name__ == "__main__":
    # O servidor rodará em localhost (127.0.0.1) na porta 8080
    app.run(port=8080)