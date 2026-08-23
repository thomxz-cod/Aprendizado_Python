# Ambiente Virtual:
```bash
# Só crie na mesma pasta onde ficará a aplicação
python -m venv venv                     # Criar ambiente virtual
source venv/Scripts/activate            # Ativar ambiente virtual (Git Bash / Linux)
# venv\Scripts\activate                 # Ativar ambiente virtual (Prompt de Comando CMD)

deactivate                              # Desativar ambiente virtual
```
<br>

# Dependências:
```bash
# Depois de entrar no ambiente virtual

python.exe -m pip install --upgrade pip # Atualizar o pip

pip install fastapi uvicorn     # Instalar as dependências para o desenvolvimento

pip list                        # Listar todas as bibliotecas instaladas

pip freeze > requirements.txt   # Salvar as versões específicas das dependências no arquivo requirements.txt

pip install -r requirements.txt # Instala as dependências listadas no arquivo requirements.txt
```
<br>

# GitIgnore

O `.gitignore` é um arquivo de configuração que diz quais pastas ou arquivos não devem ser enviados para o repositório na nuvem. Deve ser estruturado como uma lista em que cada arquivo ou diretório fica em sua própria linha.

![alt text](imgs/image.png)

## **ALERTA**
<pre style="white-space: pre-wrap; background: #161b22; padding: 16px; border-radius: 6px;">
Além de haver apenas um arquivo .gitignore por repositório, ele deve estar obrigatoriamente na raiz do diretório (onde fica a pasta oculta .git).
</pre>
<br>

# Fluxo
Depois do projeto já estar no repositório na nuvem:
```bash
git clone url_repository                # Clonar repositório
cd repository                           # Entrar na pasta do projeto
python -m venv venv                     # Criar ambiente para a aplicação
source venv/Scripts/activate            # Ativar ambiente virtual
pip install -r requirements.txt         # Instalar dependências da aplicação
```
<br>

# Uvicorn
Um servidor Web para rodar junto com o *FastAPI*. Para iniciar:
```bash
# Sempre execute depois de ativar o venv e instalar as dependências.
# Deixe rodando em segundo plano para testar a API.
# Também execute sempre na mesma pasta onde o arquivo main.py está localizado.

uvicorn main:app --reload               # :app é o nome da instância da API criada no arquivo main.py
```
