# Automated API Testing

Python tests for selected user and post endpoints of JSONPlaceholder, using Pytest and Requests.

[Execution record](docs/verification.md) · [Run tests](#setup-and-execution)

[English](#scope) · [Português](#automação-de-testes-de-api)

## Scope

Five tests send requests to `https://jsonplaceholder.typicode.com` and check the responses directly.

| Test | Request | Assertions |
| --- | --- | --- |
| `test_get_all_users` | `GET /users` | HTTP 200, JSON list, at least one item |
| `test_get_single_user` | `GET /users/1` | HTTP 200, `id` equals `1`, `email` exists |
| `test_get_user_not_found` | `GET /users/9999` | HTTP 404 |
| `test_get_posts` | `GET /posts` | HTTP 200 |
| `test_create_post` | `POST /posts` | HTTP 201, returned title matches the submitted title |

The POST payload contains `title`, `body`, and `userId`. The test checks the returned title; it does not verify all returned fields or subsequent persistence.

## Setup and execution

Requirements: Python with `venv` and `pip`, and internet access. Dependency versions are not pinned in `requirements.txt`.

From the repository root:

```bash
python -m venv .venv
```

Activate the environment using the command for your shell:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install dependencies and run:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

To run one file:

```bash
python -m pytest test_users.py -v
```

Results appear in the terminal. A [dated execution record](docs/verification.md) is available. No coverage report is included.

## Files

| File | Purpose |
| --- | --- |
| `test_users.py` | Three user tests |
| `test_posts.py` | Two post tests |
| `requirements.txt` | Pytest and Requests dependencies |
| `tests/test_users.py.txt` | Additional HTTP-status example; its `.txt` extension excludes it from default Pytest discovery |

## Limitations

- Tests depend on an external service and its current responses.
- Requests have no explicit timeout, retries, or network-error handling.
- Selected status codes, JSON shape, and fields are checked; there is no complete schema validation.
- Authentication, updates, deletion, performance, and persistence are outside the current suite.

---

# Automação de Testes de API

Testes em Python para rotas de usuários e publicações do JSONPlaceholder, com Pytest e Requests.

## Escopo

A suíte contém cinco testes, com requisições para `https://jsonplaceholder.typicode.com`.

| Teste | Requisição | Verificações |
| --- | --- | --- |
| `test_get_all_users` | `GET /users` | HTTP 200, lista JSON e pelo menos um item |
| `test_get_single_user` | `GET /users/1` | HTTP 200, `id` igual a `1` e presença de `email` |
| `test_get_user_not_found` | `GET /users/9999` | HTTP 404 |
| `test_get_posts` | `GET /posts` | HTTP 200 |
| `test_create_post` | `POST /posts` | HTTP 201 e título retornado igual ao enviado |

O POST envia `title`, `body` e `userId`. O teste verifica o título da resposta, sem validar todos os campos ou a persistência posterior.

## Preparação e execução

É necessário Python com `venv` e `pip`, além de internet. As versões das dependências não estão fixadas.

Na raiz do repositório, crie e ative o ambiente virtual com os comandos de [Setup and execution](#setup-and-execution). Em seguida:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

Para executar somente os testes de usuários:

```bash
python -m pytest test_users.py -v
```

Os resultados aparecem no terminal. Um [registro datado de execução](docs/verification.md) está disponível. O repositório não inclui relatório de cobertura.

## Organização e limites

`test_users.py` contém três testes de usuários e `test_posts.py` contém dois testes de publicações. O exemplo em `tests/test_users.py.txt` não é coletado pelo Pytest por padrão, devido à extensão `.txt`.

As chamadas não têm timeout explícito, tentativas automáticas ou tratamento de erros de rede. As verificações cobrem códigos de resposta e alguns campos, sem validação completa de esquema, autenticação, atualização, exclusão, desempenho ou persistência.
