const form = document.getElementById('task-form');
const taskList = document.getElementById('task-list');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const title = document.getElementById('title').value;
  const note = document.getElementById('note').value;
  const category = document.getElementById('category').value;
  const priority = document.getElementById('priority').value;
  const deadline = document.getElementById('deadline').value;

  form.addEventListener('submit', function (e) {
  e.preventDefault();

  const title = document.getElementById('title').value;
  const note = document.getElementById('note').value;
  const category = document.getElementById('category').value;
  const priority = document.getElementById('priority').value;
  const deadline = document.getElementById('deadline').value;

  const li = document.createElement('li');
  li.className = 'task-item';

  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.className = 'task-check';

  checkbox.addEventListener('change', () => {
    li.classList.toggle('concluida', checkbox.checked);
  });

  li.innerHTML = `
    <strong>${title}</strong> - <em>${category}</em> [${priority}]
    <div class="meta">Prazo: ${deadline ? new Date(deadline).toLocaleString() : 'Sem prazo'}</div>
    <p>${note}</p>
  `;

  li.prepend(checkbox); // Adiciona o checkbox no início da tarefa
  taskList.appendChild(li);
  form.reset();
});
});
