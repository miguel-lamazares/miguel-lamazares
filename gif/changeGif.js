const fs = require('fs');
const path = require('path');

// Define o diretório e o caminho do GIF principal
const dir = './gif';
const principalPath = './gif-principal.gif';

// Lista os arquivos .gif
const files = fs.readdirSync(dir).filter(file => file.endsWith('.gif'));

if (files.length === 0) {
  console.error('Nenhum gif encontrado.');
  process.exit(1);
}

const randomIndex = Math.floor(Math.random() * files.length);
const selectedGif = files[randomIndex];

// Copia o gif aleatório para o caminho do gif principal
fs.copyFileSync(path.join(dir, selectedGif), principalPath);

console.log(`GIF atualizado para: ${selectedGif}`);
