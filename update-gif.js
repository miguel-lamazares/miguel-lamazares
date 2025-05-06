const fs = require("fs");
const path = require("path");

const gifFolder = "./gif";
const baseUrl = "https://github.com/miguel-lamazares/miguel-lamazares/blob/main/gif/";

const gifs = fs.readdirSync(gifFolder).filter(file => file.endsWith(".gif"));

if (gifs.length === 0) {
  console.error("Nenhum gif encontrado na pasta gif/");
  process.exit(1);
}

const escolhido = gifs[Math.floor(Math.random() * gifs.length)];
const gifUrl = `${baseUrl}${encodeURIComponent(escolhido)}`;

let readme = fs.readFileSync("README.md", "utf8");

readme = readme.replace(
  /<!-- start-cs2 -->[\s\S]*?<!-- end-cs2 -->/,
  `<!-- start-cs2 -->\n<img height="150" src="${gifUrl}"/>\n<!-- end-cs2 -->`
);

fs.writeFileSync("README.md", readme);
console.log(`GIF atualizado para: ${escolhido}`);