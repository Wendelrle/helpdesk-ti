console.log("Painel do técnico carregado");

const listaChamados = document.getElementById("lista-chamados");
const filtroStatus = document.getElementById("filtro-status");
const totalChamados = document.getElementById("total-chamados");
let todosChamados = [];

function formatarData(data) {
    const dataFormatada = new Date(data);

    return dataFormatada.toLocaleString("pt-BR", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit"
    });
}

fetch("http://127.0.0.1:8000/chamados")
    .then(resposta => resposta.json())
    .then(dados => {
        console.log(dados);
        todosChamados = dados.chamados;
        totalChamados.textContent = "Total de chamados: " + todosChamados.length;
    
dados.chamados.forEach(function(chamado) {

    listaChamados.innerHTML += `
     <div class="chamado-card">
        <strong>Chamado #${chamado[0]}</strong><br>
        <strong>Título:</strong> ${chamado[1]}<br>
        <strong>Descrição:</strong> ${chamado[2]}<br>
        <strong>Categoria:</strong> ${chamado[3]}<br>
        <strong>Prioridade:</strong> ${chamado[4]}<br>
        <strong>Status atual:</strong> ${chamado[5]}<br>
    <strong>Data de criação:</strong> ${formatarData(chamado[6])}<br>
    <strong>Novo status:</strong>
    <select>
        <option value="Aberto">Aberto</option>
        <option value="Em atendimento">Em atendimento</option>
        <option value="Resolvido">Resolvido</option>
    </select>
    
    <button onclick="alterarStatus(${chamado[0]}, this.previousElementSibling.value)">
    Atualizar status
    </button>
     </div>
     `;
    });
    }); 

    function alterarStatus(chamadoId, novoStatus) {
    fetch(`http://127.0.0.1:8000/chamados/${chamadoId}/status`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            status: novoStatus
        })
    })
    .then(() => {
        alert("Status atualizado com sucesso!");
        window.location.reload();
    }) ;
}
filtroStatus.addEventListener("change", function() {
    const statusEscolhido = filtroStatus.value;
    const chamadosFiltrados = statusEscolhido === "Todos"
    ? todosChamados
    : todosChamados.filter(function(chamado) {
        return chamado[5] === statusEscolhido;
    });

 console.log(chamadosFiltrados);
 totalChamados.textContent = "Total de chamados: " + chamadosFiltrados.length;
 listaChamados.innerHTML = "";
 chamadosFiltrados.forEach(function(chamado) {
    listaChamados.innerHTML += `
    <div class="chamado-card">
    <strong>Chamado #${chamado[0]}</strong><br>
    <strong>Título:</strong> ${chamado[1]}<br>
    <strong>Descrição:</strong> ${chamado[2]}<br>
    <strong>Categoria:</strong> ${chamado[3]}<br>
    <strong>Prioridade:</strong> ${chamado[4]}<br>
    <strong>Data de criação:</strong> ${formatarData(chamado[6])}<br>    <select>
    <option value="Aberto" ${chamado[5] === "Aberto" ? "selected" : ""}>Aberto</option>
    <option value="Em atendimento" ${chamado[5] === "Em atendimento" ? "selected" : ""}>Em atendimento</option>
    <option value="Resolvido" ${chamado[5] === "Resolvido" ? "selected" : ""}>Resolvido</option>
    </select>
    <button onclick="alterarStatus(${chamado[0]}, this.previousElementSibling.value)">
    Atualizar status
    </button>
    </div>
    `;
});
});