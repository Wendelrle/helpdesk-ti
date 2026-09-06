console.log("Página de cadastro carregada");
const formulario = document.getElementById("form-cadastro");
console.log(formulario);
formulario.addEventListener("submit", function(evento) {

    evento.preventDefault();
    const nome = document.getElementById("nome").value; 
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    const confirmarsenha = document.getElementById("confirmar-senha").value;
    if (senha !== confirmarsenha) {
        alert("As senhas não são iguais!");
        return;
    }
const dadosUsuario = {
    nome: nome,
    email: email,
    senha: senha
};

console.log(dadosUsuario);

  fetch("http://127.0.0.1:8000/usuarios", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(dadosUsuario)
})
.then(resposta => resposta.json())
.then(dados => {
    console.log(dados);
    alert(dados.mensagem);
});
});