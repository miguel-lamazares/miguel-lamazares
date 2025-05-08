const fs = require('fs');

// Lê o template README
const template = fs.readFileSync("README.template.md", "utf-8");

// Função para comentar e descomentar blocos
function commentBlock(content, id) {
  return content.replace(
    new RegExp(`<div id="${id}">([\\s\\S]*?)<\\/div>`, 'gm'),
    `<!-- <div id="${id}">$1</div> -->`
  );
}

function uncommentBlock(content, id) {
  return content.replace(
    new RegExp(`<!--\\s*<div id="${id}">([\\s\\S]*?)<\\/div>\\s*-->`, 'gm'),
    `<div id="${id}">$1</div>`
  );
}

const now = new Date();
const hour = now.getUTCHours();
const showPacmen = Math.floor(hour / 6) % 2 === 0;  // Troca a animação a cada 6 horas

let updated = template;

// Alterna entre Pacman e Snake
if (showPacmen) {
  updated = uncommentBlock(updated, "pacmen");
  updated = commentBlock(updated, "snake");
} else {
  updated = uncommentBlock(updated, "snake");
  updated = commentBlock(updated, "pacmen");
}

fs.writeFileSync("README.md", updated);
