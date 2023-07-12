# University(API)

Este MVP faz parte da entrega da Disciplina **Desenvolvimento Full Stack Básico** 
- -Puck-rio - Engenharia de software

Consiste em um sistema composto por 2 camadas (servidor front-end e servidor back-end), este último está descrito aqui:
A api é composta de uma base de dados com duas tabelas, aluno e curso, que tem como objetivo cadastrar, deletar e listar as matrículas realizadas em um sistema de uma  universidade. 

---
## Instruções:

É necessário utilizar ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html);

Será necessário ter todas as libs python listadas e instaladas no `requirements.txt`;

Após clonar o repositório, no diretório raiz do projeto e no terminal (depois de ativar o script do enviroment) execute os comandos descritos abaixo:

```
pip install -r requirements.txt
```

Para executar a API  :

```
flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento use o parâmetro reload, que reiniciará o servidor.

```
flask run --host 0.0.0.0 --port 5000 --reload
```

Visualize no navegador [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
