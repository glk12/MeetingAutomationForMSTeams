# 🤖 MeetingAutomationForMSTeams

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

Automação inteligente para entrada em reuniões do Microsoft Teams com gerenciamento via banco de dados SQLite.

## 📋 Descrição

Este script automatiza completamente o processo de entrada em reuniões do Microsoft Teams, permitindo:
- ✅ Entrada automática em reuniões agendadas
- ✅ Silenciamento automático do microfone
- ✅ Gerenciamento de reuniões via banco de dados SQLite
- ✅ Interface de linha de comando interativa
- ✅ Monitoramento em tempo real de reuniões agendadas

## 🚀 Funcionalidades

- **Automação Completa**: Entra automaticamente nas reuniões usando ID e senha
- **Gestão de Áudio**: Silencia o microfone antes de entrar na reunião
- **Banco de Dados**: Armazena e gerencia reuniões recorrentes
- **Menu Interativo**: Interface CLI para CRUD de reuniões
- **Multi-threading**: Monitora reuniões enquanto permite interação do usuário
- **Agendamento Semanal**: Suporte para reuniões recorrentes por dia da semana

## 📦 Pré-requisitos

- **Sistema Operacional**: Windows (devido ao uso de pywinauto e pywin32)
- **Python**: 3.8 ou superior
- **Microsoft Teams**: Instalado e configurado
- **Dependências**: Listadas em `requirements.txt`

## 🔧 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/glk12/MeetingAutomationForMSTeams.git
cd MeetingAutomationForMSTeams
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o caminho do Microsoft Teams

Edite o arquivo `main.py` e `functions.py` e ajuste a variável `path_teams` com o caminho correto da instalação do Teams no seu sistema:

```python
path_teams = "C:\\Program Files\\WindowsApps\\MSTeams_XXXXX\\ms-teams.exe"
```

**Como encontrar o caminho:**
- Abra o Explorador de Arquivos
- Digite `%LocalAppData%\Packages` na barra de endereços
- Procure por uma pasta que comece com `MSTeams_`
- O executável geralmente está em `MSTeams_XXXXX\ms-teams.exe`

## 💻 Como Usar

### Executar o programa
```bash
python main.py
```

### Menu Interativo

Ao executar, você verá o menu:
```
1- Inserir reunião
2- Deletar reunião
3- Listar reuniões
4- Editar reunião
```

### Cadastrar uma reunião

1. Selecione opção `1`
2. Forneça as informações:
   - **Nome**: Identificador da reunião (ex: "Daily Standup")
   - **Horário**: Formato HH:MM (ex: "09:00")
   - **Dia da semana**: Em inglês (monday, tuesday, etc.)
   - **ID da reunião**: Código fornecido pelo Teams
   - **Senha**: Senha da reunião (se houver)

### Exemplo de uso
```
1- Inserir reunião
Nome da reunião: Daily Team Meeting
Horário da reunião (HH:MM): 09:00
Dia da semana da reunião(em inglês): monday
ID da reunião: 123 456 789
Senha da reunião: abc123
```

## 🗄️ Estrutura do Banco de Dados

O banco SQLite (`reunioes.db`) armazena:
- Nome da reunião
- Horário (HH:MM)
- Dia da semana
- ID da reunião do Teams
- Senha da reunião

## 📁 Estrutura do Projeto

```
MeetingAutomationForMSTeams/
├── main.py              # Script principal com menu e threading
├── functions.py         # Funções de automação do Teams
├── reunioes.py          # Classe para gerenciamento do banco de dados
├── requirements.txt     # Dependências do projeto
├── reunioes.db          # Banco de dados SQLite (criado automaticamente)
├── LICENSE              # Licença MIT
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal
- **pywinauto**: Automação de interface Windows
- **pywin32**: Interação com APIs do Windows
- **SQLite**: Banco de dados local
- **Threading**: Execução paralela de tarefas

## ⚠️ Troubleshooting

### Erro: Teams não abre
- Verifique se o caminho `path_teams` está correto
- Certifique-se de que o Teams está instalado
- Execute como Administrador se necessário

### Erro: Reunião não inicia automaticamente
- Verifique se o ID e senha estão corretos
- Confirme que o horário está no formato HH:MM
- Verifique o fuso horário do sistema

### Erro ao instalar dependências
- Atualize o pip: `python -m pip install --upgrade pip`
- Instale Visual C++ Build Tools se necessário (para pywin32)

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

**glk12** - [GitHub](https://github.com/glk12)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## ⭐ Mostre seu apoio

Se este projeto foi útil, considere dar uma ⭐!

---

**Nota**: Este projeto é destinado apenas para uso educacional e automação pessoal. Use de forma responsável.
