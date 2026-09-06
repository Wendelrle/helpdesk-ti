console.log("Página de chamados carregada");
const formulario = document.getElementById("form-chamados");
const listaChamados = document.getElementById("lista-chamados");
console.log(formulario);

formulario.addEventListener("submit", function(evento) {
  evento.preventDefault();

const titulo = document.getElementById("titulo").value;
const descricao = document.getElementById("descricao").value;
const categoria = document.getElementById("categoria").value;
const prioridade = document.getElementById("prioridade").value;

console.log(titulo);
console.log(descricao);
console.log(categoria);
console.log(prioridade);

const dadosChamado = {
    titulo: titulo,
    descricao: descricao,
    categoria: categoria,
    prioridade: prioridade
};

console.log(dadosChamado);

fetch("http://127.0.0.1:8000/chamados", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(dadosChamado)
})
.then(() => {
    window.location.reload();
});11

  console.log("Botão Abrir chamado foi clicado");
});
fetch("http://127.0.0.1:8000/chamados")
    .then(resposta => resposta.json())
    .then(dados => {
    console.log(dados);
    listaChamados.innerHTML = "";
    dados.chamados.forEach(function(chamado) {
    console.log(chamado);

    const item = document.createElement("div");
    item.classList.add("chamado-card");
    item.innerHTML = `
    <strong>Chamado #${chamado[0]}</strong><br>
    <strong>Título:</strong> ${chamado[1]}<br>
    <strong>Descrição:</strong> ${chamado[2]}<br>
    <strong>Categoria:</strong> ${chamado[3]}<br>
    <strong>Prioridade:</strong> ${chamado[4]}<br>
    <strong>Status:</strong> ${chamado[5]}
`;
    listaChamados.appendChild(item);
});
});

