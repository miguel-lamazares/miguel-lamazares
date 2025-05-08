const fs = require('fs');
const path = require('path');

// Define o diretório de onde os GIFs serão retirados
const dir = path.join(__dirname, 'gif'); // Ajuste o caminho para a pasta 'gif'
const principalPath = path.join(__dirname, 'gif-principal.gif'); // Caminho do gif principal

// Verifica se o diretório 'gif' existe
if (!fs.existsSync(dir)) {
  console.error('A pasta "gif" não foi encontrada!');
  process.exit(1);
}

// Lista os arquivos .gif dentro da pasta 'gif'
const files = fs.readdirSync(dir).filter(file => file.endsWith('.gif'));

if (files.length === 0) {
  console.error('Nenhum GIF encontrado na pasta.');
  process.exit(1);
}

// Escolhe um GIF aleatório da lista
const randomIndex = Math.floor(Math.random() * files.length);
const selectedGif = files[randomIndex];

// Verifica se o arquivo selecionado existe antes de copiar
const sourceGifPath = path.join(dir, selectedGif);
if (!fs.existsSync(sourceGifPath)) {
  console.error(`O arquivo ${selectedGif} não foi encontrado.`);
  process.exit(1);
}

// Copia o GIF selecionado para o GIF principal
fs.copyFileSync(sourceGifPath, principalPath);

console.log(`GIF atualizado com sucesso: ${selectedGif}`);
