console.log('Página de login carregada');
const formulario = document.getElementById("form-login");
console.log(formulario);

formulario.addEventListener("submit", function(evento) {
    evento.preventDefault();
    const email = document.getElementById("email").value;
const senha = document.getElementById("senha").value;
const dadoslogin = {
    email:email,
    senha: senha
};

    console.log(email);
    console.log(senha);
    console.log(dadoslogin);

fetch("http://127.0.0.1:8000/login", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(dadoslogin)
   })
.then(resposta => resposta.json())
.then(dados => {
    alert(dados.mensagem);

    if (dados.mensagem === "login realizado com sucesso") {
        console.log("entrou no redirecionamento");
    window.location.href = "chamados.html";
}
});
});
