const URL_BASE = 'http://localhost:8000';

// Função para chamar as tarefas da API
async function getTarefas() {
  const response = await fetch(`${URL_BASE}/tarefas`);
  const data = await response.json();
  return data;
}

// Função para criar uma nova tarefa
async function postTarefa(tarefa) {
  const response = await fetch(`${URL_BASE}/tarefas`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(tarefa),
  });
  const data = await response.json();
  return data;
}

// Função para atualizar uma tarefa existente
async function putTarefa(tarefaId, tarefa) {
  const response = await fetch(`${URL_BASE}/tarefas/${tarefaId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(tarefa),
  });
  const data = await response.json();
  return data;
}

// Função para excluir uma tarefa existente
async function deleteTarefa(tarefaId) {
  const response = await fetch(`${URL_BASE}/tarefas/${tarefaId}`, {
    method: 'DELETE',
  });
  return response.status;
}

// Função para renderizar as tarefas na página HTML
async function renderTarefas() {
  const tarefas = await getTarefas();
  const tarefasContainer = document.querySelector('#tarefas');

  tarefasContainer.innerHTML = '';

  tarefas.forEach((tarefa) => {
    const tarefaEl = document.createElement('div');
    tarefaEl.innerHTML = `
      <h2>${tarefa.descricao}</h2>
      <p>Nível: ${tarefa.nivel}</p>
      <p>Prioridade: ${tarefa.prioridade}</p>
      <p>Situação: ${tarefa.situacao}</p>
      <p>Responsável: ${tarefa.responsavel || 'Não definido'}</p>
      <button class="btn-editar" data-id="${tarefa.id}">Editar</button>
      <button class="btn-excluir" data-id="${tarefa.id}">Excluir</button>
    `;

    const btnEditar = tarefaEl.querySelector('.btn-editar');
    btnEditar.addEventListener('click', async () => {
      const descricao = prompt('Digite a nova descrição:', tarefa.descricao);
      if (descricao) {
        const tarefaAtualizada = {
          descricao,
          nivel: tarefa.nivel,
          prioridade: tarefa.prioridade,
          situacao: tarefa.situacao,
          responsavel: tarefa.responsavel,
        };
        await putTarefa(tarefa.id, tarefaAtualizada);
        renderTarefas();
      }
    });

    const btnExcluir = tarefaEl.querySelector('.btn-excluir');
    btnExcluir.addEventListener('click', async () => {
      if (confirm(`Tem certeza que deseja excluir a tarefa "${tarefa.descricao}"?`)) {
        await deleteTarefa(tarefa.id);
        renderTarefas();
      }
    });

    tarefasContainer.appendChild(tarefaEl);
  });
}

// Função para criar uma nova tarefa quando o formulário for submetido
const form = document.querySelector('#form-nova-tarefa');
form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const descricao = document.querySelector('#descricao').value;
  const nivel = document.querySelector('#nivel').value;
  const prioridade = document.querySelector('#prioridade').value;
  const situacao = document.querySelector('#situacao').value;
  const responsavel = document.querySelector('#responsavel').value;

  const novaTarefa = {
    descricao,
    nivel,
    prioridade,
    situacao,
    responsavel,
  };

  await postTarefa(novaTarefa);
  renderTarefas();

  form.reset();
});
