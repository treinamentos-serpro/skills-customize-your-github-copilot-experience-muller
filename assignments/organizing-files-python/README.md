# 📘 Atividade: Automatizando a Organização de Arquivos

## 🎯 Objetivo

Crie um programa em Python que organize automaticamente arquivos de uma pasta em subpastas de acordo com suas extensões. Você praticará o uso de `pathlib`, funções, condicionais e operações seguras com arquivos.

## 📝 Tarefas

### 🛠️ Listar os arquivos da pasta

#### Descrição
Implemente uma função que receba o caminho de uma pasta e mostre os arquivos encontrados nela. Ignore subpastas nesta primeira versão.

#### Requisitos
O programa concluído deve:

- Usar `pathlib.Path` para representar o caminho da pasta.
- Exibir o nome de cada arquivo encontrado.
- Ignorar diretórios e continuar funcionando quando a pasta estiver vazia.


### 🛠️ Classificar arquivos por extensão

#### Descrição
Crie uma função que transforme a extensão de um arquivo em uma categoria. Use pelo menos as categorias `imagens`, `documentos`, `planilhas` e `outros`.

#### Requisitos
O programa concluído deve:

- Classificar `.jpg`, `.jpeg`, `.png` e `.gif` como `imagens`.
- Classificar `.pdf`, `.docx` e `.txt` como `documentos`.
- Classificar `.csv`, `.xlsx` e `.ods` como `planilhas`.
- Classificar extensões desconhecidas como `outros`.
- Tratar extensões em letras maiúsculas e minúsculas da mesma forma.


### 🛠️ Organizar os arquivos automaticamente

#### Descrição
Use as funções anteriores para criar as subpastas necessárias e mover cada arquivo para sua categoria. Teste primeiro com uma pasta de exemplo que contenha cópias de arquivos, nunca com uma pasta importante do computador.

#### Requisitos
O programa concluído deve:

- Criar uma subpasta somente quando ela for necessária.
- Usar `shutil.move()` para mover os arquivos.
- Não mover subpastas nem o próprio arquivo do programa.
- Informar na tela o caminho de origem e o destino de cada arquivo movido.
- Continuar funcionando se a pasta de origem já estiver organizada ou não tiver arquivos.

Exemplo de saída:

```text
foto.png -> imagens/foto.png
notas.txt -> documentos/notas.txt
```