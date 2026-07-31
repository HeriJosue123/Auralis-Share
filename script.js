const preguntas=[

{

q:"¿Qué es el dominio?",

a:[

"Los valores que puede tomar la entrada",

"Los resultados",

"Una gráfica",

"Una pendiente"

],

c:0

},

{

q:"¿Qué restringe un dominio?",

a:[

"Raíces",

"Denominadores",

"Logaritmos",

"Todas las anteriores"

],

c:3

},

{

q:"Una curva de nivel une puntos con...",

a:[

"Distinto valor",

"El mismo valor",

"Mayor pendiente",

"Menor pendiente"

],

c:1

}

];

let actual=0;

let score=0;

let vidas=3;

let tiempo=20;

let intervalo;

const start=document.getElementById("start");

const menu=document.getElementById("menu");

const game=document.getElementById("game");

const final=document.getElementById("final");

const question=document.getElementById("question");

const answers=document.getElementById("answers");

const vidasHTML=document.getElementById("vidas");

const scoreHTML=document.getElementById("score");

const resultado=document.getElementById("resultado");

const bar=document.getElementById("bar");

const time=document.getElementById("time");

start.onclick=()=>{

menu.classList.add("hidden");

game.classList.remove("hidden");

cargar();

};

function cargar(){

clearInterval(intervalo);

tiempo=20;

time.innerHTML=tiempo;

intervalo=setInterval(()=>{

tiempo--;

time.innerHTML=tiempo;

if(tiempo==0){

perderVida();

}

},1000);

question.innerHTML=preguntas[actual].q;

answers.innerHTML="";

preguntas[actual].a.forEach((texto,i)=>{

let b=document.createElement("button");

b.innerHTML=texto;

b.onclick=()=>responder(i,b);

answers.appendChild(b);

});

bar.style.width=((actual)/preguntas.length)*100+"%";

}

function responder(i,b){

clearInterval(intervalo);

if(i==preguntas[actual].c){

score++;

scoreHTML.innerHTML=score;

b.classList.add("correct");

}else{

b.classList.add("wrong");

perderVida();

}

setTimeout(()=>{

actual++;

if(actual==preguntas.length||vidas==0){

fin();

}else{

cargar();

}

},900);

}

function perderVida(){

clearInterval(intervalo);

vidas--;

vidasHTML.innerHTML=vidas;

if(vidas==0){

fin();

}else{

actual++;

if(actual<preguntas.length){

cargar();

}

}

}

function fin(){

game.classList.add("hidden");

final.classList.remove("hidden");

resultado.innerHTML=

"Tu puntaje fue "+score+" de "+preguntas.length;

}