# Registro de execução

**Data:** 15/10/2026

**Resultado:** 5 testes aprovados, sem falhas, em 1,77 segundo.

Execução da suíte existente com `python -m pytest -v`, realizando chamadas ao JSONPlaceholder.

| Teste | Resultado |
| --- | --- |
| `test_posts.py::test_get_posts` | Aprovado |
| `test_posts.py::test_create_post` | Aprovado |
| `test_users.py::test_get_all_users` | Aprovado |
| `test_users.py::test_get_single_user` | Aprovado |
| `test_users.py::test_get_user_not_found` | Aprovado |

Resumo retornado pelo Pytest:

```text
5 passed in 1.77s
```

Ambiente: Python 3.12.14, Pytest 9.1.1 e Requests 2.34.2, no Windows.

Este registro corresponde à execução nessa data. A suíte depende de um serviço externo; o resultado não representa cobertura completa da API nem garantia de execuções futuras.

[Executar a suíte](../README.md#preparação-e-execução) · [Escopo dos testes](../README.md#escopo) · [Código](../)
