from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from model import Session, Curso, Aluno
from logger import logger
from schemas import *

from flask_cors import CORS


info = Info(title="University-API", version="1.2.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
aluno_tag = Tag(name="Aluno", description="Inclusão, listagem e exclusão de matrícula no sistema da universidade na base")
curso_tag = Tag(name="Curso", description="Inclusão do  curso referente a matrícula e suas respectivas disciplinas na base")


@app.get('/home', tags=[home_tag])
def home():
    return redirect('/openapi')


@app.post('/aluno', tags=[aluno_tag],
          responses={"200": AlunoViewSchema, "409": ErrorViewSchema, "400": ErrorViewSchema})
def cadastra_aluno(form: AlunoSchema):
    aluno = Aluno(
        cpf=form.cpf,
        nome=form.nome,
        endereco=form.endereco,
        cep=form.cep,
        cidade=form.cidade,
        uf=form.uf,
        celular=form.celular)
    logger.debug(f"matriculando aluno de nome: '{aluno.nome}'")
    try:
        session = Session()
        session.add(aluno)
        session.commit()
        logger.debug(f"Cadastrado aluno: '{aluno.nome}'")
        return view_aluno(aluno), 200

    except IntegrityError as e:
        error_msg = "Aluno já cadastrado na base :/"
        logger.warning(f"Erro ao cadastrar aluno '{aluno.nome}', {error_msg}")
        return {"mensage": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo cadastro :/"
        logger.warning(f"Erro ao criar cadastro '{aluno.nome}', {error_msg}")
        return {"mensage": error_msg}, 400


@app.get('/alunos', tags=[aluno_tag],
         responses={"200": ListagemAlunoSchema, "404": ErrorViewSchema})
def get_aluno():
    logger.debug(f"Listando alunos matriculados ")
    session = Session()
    alunos = session.query(Aluno).all()

    if not alunos:
        return {"alunos": []}, 200
    else:
        logger.debug(f"%d matriculas encontradas" % len(alunos))
        print(alunos)
        return view_alunos(alunos), 200


@app.get('/aluno', tags=[aluno_tag],
         responses={"200": AlunoViewSchema, "404": ErrorViewSchema})
def busca_aluno(query: AlunoGetSchema):
    aluno_cpf = query.cpf
    aluno_nome = query.nome
    logger.debug(f"Buscando dados sobre aluno #{aluno_cpf}")
    session = Session()
    aluno = session.query(Aluno).filter(Aluno.cpf == aluno_cpf).first()

    if not aluno:
        error_msg = "Aluno não encontrado na base :/"
        logger.warning(f"Erro ao buscar aluno '{aluno_cpf}', {error_msg}")
        return {"mensage": error_msg}, 404
    else:
        logger.debug(f"Aluno matriculado encontrado: {aluno_cpf}")
        return view_aluno(aluno), 200


@app.delete('/aluno', tags=[aluno_tag],
            responses={"200": AlunoDelSchema, "404": ErrorViewSchema})
def del_aluno(query: AlunoGetSchema):
    aluno_cpf = unquote(unquote(query.cpf))
    aluno_nome = unquote(unquote(query.nome))
    print(aluno_nome)
    logger.debug(f"Excluindo aluno #{aluno_nome}")
    session = Session()
    count = session.query(Aluno).filter(Aluno.cpf == aluno_cpf).delete()
    session.commit()
    if count:
        logger.debug(f"Excluido aluno #{aluno_cpf}")
        return {"mensage": "Aluno removido da base  ", "nome": aluno_nome}
    else:
        error_msg = "Aluno não encontrado na base :/"
        logger.warning(f"Erro ao excluir aluno #'{aluno_nome}', {error_msg}")
        return {"mensage": error_msg}, 404


@app.post('/curso', tags=[curso_tag],
          responses={"200": AlunoViewSchema, "404": ErrorViewSchema})
def add_matricula(form: CursoSchema):
    aluno_id = form.id
    aluno_cpf = form.cpf
    curso = Curso(
        cpf=form.cpf,
        codigo_curso=form.codigo_curso,
        curso=form.curso,
        codigo_disc=form.codigo_disc,
        disciplina=form.disciplina,
        creditos=form.creditos)

    logger.debug(f"Matriculando aluno  ao curso #{aluno_cpf}")
    session = Session()
    aluno = session.query(Aluno).filter(Aluno.cpf == aluno_cpf).first()

    if not aluno:
        error_msg = "Aluno não encontrado na base :/"
        logger.warning(f"Erro ao matricular aluno '{aluno_cpf}', {error_msg}")
        return {"mensage": error_msg}, 404

    aluno.adiciona_curso(curso)
    session.commit()

    logger.debug(f"Matriculado aluno  #{aluno_cpf}")

    return view_aluno(aluno), 200
