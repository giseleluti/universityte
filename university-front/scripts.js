const getList = async () => {
  let url = 'http://127.0.0.1:5000/alunos';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.alunos.forEach(item => insertList(item.nome, item.cpf, item.celular, item.endereco, item.cep, item.cidade, item.uf))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

getList()

const postItem = async (inputNome, inputCpf, inputCelular, inputEndereco, inputCep, inputCidade, inputUf) => {
  const formData = new FormData();
  formData.append('nome', inputNome);
  formData.append('cpf', inputCpf);
  formData.append('celular', inputCelular);
  formData.append('endereco', inputEndereco);
  formData.append('cep', inputCep);
  formData.append('cidade', inputCidade);
  formData.append('uf', inputUf);

  let url = 'http://127.0.0.1:5000/aluno';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

const newItem = () => {
  let inputNome = document.getElementById("newNome").value;
  let inputCpf = document.getElementById("newCpf").value;
  let inputCelular = document.getElementById("newCelular").value;
  let inputEndereco = document.getElementById("newEndereco").value;
  let inputCep = document.getElementById("newCep").value;
  let inputCidade = document.getElementById("newCidade").value;
  let inputUf = document.getElementById("newUf").value;

  if (inputCpf === '') {
    alert("O campo CPF é obrigatório!");
  } else if (isNaN(inputCelular)) {
    alert("O campo celular precisa ser números!");
  } else {
    insertList(inputNome, inputCpf, inputCelular, inputEndereco, inputCep, inputCidade, inputUf)
    postItem(inputNome, inputCpf, inputCelular, inputEndereco, inputCep, inputCidade, inputUf)
    alert("Aluno cadastrado!")
  }
}

const insertButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


const removeElement = () => {
  let close = document.getElementsByClassName("close");
  var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeIten = div.getElementsByTagName('td')[1].innerHTML
      if (confirm("Você tem certeza que deseja excluir? Isso também deleta os cursos matriculados.")) {
        div.remove()
        deleteItem(nomeIten)
        alert("Aluno removido!")
      }
    }
  }
}

const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/aluno?cpf=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

const insertList = (nome, cpf, celular, endereco, cep, cidade, uf) => {
  var item = [nome, cpf, celular, endereco, cep, cidade, uf]
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1))
  document.getElementById("newNome").value = "";
  document.getElementById("newCpf").value = "";
  document.getElementById("newCelular").value = "";
  document.getElementById("newEndereco").value = "";
  document.getElementById("newCep").value = "";
  document.getElementById("newCidade").value = "";
  document.getElementById("newUf").value = "";

  removeElement()
}

const postMatricula = async (inputCpfMat, inputCodigoCurso,  inputCurso, inputCodigoDisciplina, inputDisciplina, inputCreditos) => {
  const formData = new FormData();
  formData.append('cpfMat', inputCpfMat);
  formData.append('codigoCurso', inputCodigoCurso);
  formData.append('curso', inputCurso);
  formData.append('codigoDisciplina', inputCodigoDisciplina);
  formData.append('disciplina', inputDisciplina);
  formData.append('creditos', inputCreditos);

  let url = 'http://127.0.0.1:5000/curso';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

const newMatricula = () => {
  let inputCpfMat = document.getElementById("newCpfMat").value;
  let inputCodigoCurso = document.getElementById("newCodigoCurso").value;
  let inputCurso = document.getElementById("newCurso").value;
  let inputCodigoDisciplina = document.getElementById("newCodigoDisciplina").value;
  let inputDisciplina = document.getElementById("newDisciplina").value;
  let inputCreditos = document.getElementById("newCreditos").value;

  if (inputCpfMat === '' && inputCurso === '' && inputDisciplina === '' && inputCreditos === '') {
    alert("Os campos CPF, curso, disciplina e créditos  são obrigatórios!");
  } else if (isNaN(inputCodigoCurso) || isNaN(inputCodigoDisciplina) || isNaN(inputCreditos)) {
    alert("Os campos código disciplina, código curso e créditos precisam ser números!");
  } else {
    insertMatricula(inputCpfMat, inputCodigoCurso,  inputCurso, inputCodigoDisciplina, inputDisciplina, inputCreditos)
    postMatricula(inputCpfMat, inputCodigoCurso,  inputCurso, inputCodigoDisciplina, inputDisciplina, inputCreditos)
    alert("Aluno matriculado no curso!")
  }
}



const insertMatricula = (cpfMat, codicoCurso, curso, codigoDisciplina, disciplina, creditos) => {
  var item = [cpfMat, codicoCurso, curso, codigoDisciplina, disciplina, creditos]
  var table = document.getElementById('matriculaTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1))
  document.getElementById("newCpfMat").value = "";
  document.getElementById("newCodigoCurso").value = "";
  document.getElementById("newCurso").value = "";
  document.getElementById("newCodigoDisciplina").value = "";
  document.getElementById("newDisciplina").value = "";
  document.getElementById("newCreditos").value = "";

  removeElement()
}
