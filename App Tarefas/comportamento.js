const baseURL = 'http://127.0.0.1:8000/tarefas'
//Obtem o botão do formulário da página HTML
var btnSalvar = document.querySelector("#btn-confirmar");

//Executa a função anonima ao clicar no botão
btnSalvar.addEventListener("click", function (event) {
    //Evita o comportamento padrão que seria recarregar a página
    event.preventDefault();
    
    //Obtem o formulário da nossa página HTML
    var frmtarefa = document.querySelector("#frmtarefa");

    //Imprime o valor de cada campo do formulário
    console.log(frmtarefa.descricao.value);
    console.log(frmtarefa.nivel.value);
    console.log(frmtarefa.prioridade.value);
    console.log(frmtarefa.situacao.value);
    console.log(frmtarefa.responsavel.value);

    //Cria um elemento tr dentro do documento HTML
    var linhatarefa = document.createElement("tr");

    //Cria quatro elementos td dentro do documento HTML
    var colunadescricao = document.createElement("td");
    var colunanivel = document.createElement("td");
    var colunaprioridade = document.createElement("td");
    var colunasituacao = document.createElement("td");
    var colunaresponsavel = document.createElement("td");

    //Coloca o conteúdo correto em cada elemento td criando anteriormente
    colunadescricao.textContent = frmtarefa.descricao.value;
    colunanivel.textContent = frmtarefa.nivel.value;
    colunaprioridade.textContent = frmtarefa.prioridade.value;
    colunasituacao.textContent = frmtarefa.situacao.value;
    colunaresponsavel.textContent = frmtarefa.responsavel.value;

    //Coloca os elementos td como filhos do elemento tr
    linhatarefa.appendChild(colunadescricao);
    linhatarefa.appendChild(colunanivel);
    linhatarefa.appendChild(colunaprioridade);
    linhatarefa.appendChild(colunasituacao);
    linhatarefa.appendChild(colunaresponsavel);

    //Coloca o elemento tr como filha da tabela de alunos
    var tabelaAlunos = document.querySelector("#tabela-tarefas").querySelector("tbody");
    tabelaAlunos.appendChild(linhatarefa);
})