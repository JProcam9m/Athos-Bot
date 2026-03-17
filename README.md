# 🤖 Athos Bot

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/library-discord.py-2.0+-blue)](https://discordpy.readthedocs.io/en/stable/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

O **Athos Bot** é um assistente multifuncional para Discord, focado em automação, moderação e experiência do usuário. Desenvolvido em Python, ele combina comandos clássicos de prefixo com as tecnologias mais recentes do Discord, como **Modais (formulários)** e **Interações por Botões**.

---

## ✨ Funcionalidades Principais

* **🖼️ Gerador de Embeds (Visual)**: Sistema exclusivo via `!criar_embed` que abre um formulário (Modal) para criar anúncios personalizados com título, descrição, cor e imagem.
* **🎭 Registro por Reações**: Sistema automático de atribuição de cargos para linguagens de programação (Python, JS, C#, Java, etc.) através de emojis customizados.
* **👋 Boas-vindas Premium**: Saudação automática para novos membros com Embeds elegantes, exibindo o avatar do usuário, data de criação da conta e contador de membros em tempo real.
* **🛡️ Moderação Ágil**: Controle total sobre o chat com comandos de limpeza (`clear`) e trancamento de canais (`lock/unlock`).
* **🔍 Utilidades Avançadas**: Comandos para buscar o **Avatar** e o **Banner** de perfil dos usuários em alta definição.

---
## 📋 Registro de Linguagens de Programação
![alt text](screenshots/registro.png) 

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**: Base robusta para processamento assíncrono.
* **Discord.py**: Framework principal para integração com a API do Discord.
* **Python-dotenv**: Gerenciamento seguro de variáveis de ambiente (`BOT_TOKEN`).

---

## 📋 Tabela de Comandos

![alt text](screenshots/comandos.png) 

### 🛡️ Administração e Moderação
| Comando | Descrição | Permissão |
| :--- | :--- | :--- |
| `!setup_registro` | Envia o painel de cargos por reação | Administrador |
| `!criar_embed` | Abre o botão para o **Editor Visual de Embeds** | Administrador |
| `!clear [qtd]` | Remove mensagens em massa do canal | Gerenciar Mensagens |
| `!lock` / `!unlock` | Bloqueia ou desbloqueia o envio de mensagens | Gerenciar Canais |

### 🛠️ Utilidades e Social
| Comando | Descrição | Permissão |
| :--- | :--- | :--- |
| `!avatar [@user]` | Exibe a foto de perfil do usuário | Livre |
| `!banner [@user]` | Mostra o banner de perfil do usuário | Livre |
| `!ping` | Verifica a latência de conexão do bot | Livre |
| `!comandos` | Lista a central de ajuda organizada | Livre |
| `!ola` / `!suave` | Comandos de interação rápida | Livre |

---

## ⚙️ Como Configurar

1. **Variáveis de Ambiente**:
   Crie um arquivo `.env` na raiz do projeto e adicione seu token:
   ```env
   BOT_TOKEN=SEU_TOKEN_AQUI
