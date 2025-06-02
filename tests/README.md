# 🧪 Repl.ET Test Suite

Esta suíte de testes automatizada garante a qualidade, integridade e conformidade do repositório Repl.ET com padrões científicos.

## 📋 Tipos de Testes

### 🔍 **Schema Tests** (`test_schemas.py`)
- Validação de todos os schemas JSON Draft 7
- Verificação de que dados validam contra seus schemas
- Garantia de consistência estrutural

### 🔗 **Data Integrity Tests** (`test_data_integrity.py`)
- Consistência de IDs entre arquivos (participantes, estímulos, AOIs)
- Validação de coordenadas de AOIs
- Verificação de existência de arquivos referenciados
- Integridade da pipeline de análise

### 🎯 **Scoring System Tests** (`test_repl_et_score.py`)
- Testes do sistema de avaliação de reprodutibilidade
- Validação de pontuações (0.0 - 1.0)
- Testes de todos os 10 eixos de avaliação

## 🚀 Como Executar

### Instalação
```bash
pip install -r requirements.txt
```

### Execução Básica
```bash
# Todos os testes
pytest tests/

# Apenas testes específicos
pytest tests/test_schemas.py
pytest tests/test_data_integrity.py
pytest tests/test_repl_et_score.py
```

### Por Categoria
```bash
# Testes unitários (rápidos)
pytest -m unit tests/

# Testes de integração
pytest -m integration tests/

# Incluir testes lentos
pytest -m slow tests/
```

### Com Cobertura
```bash
# Relatório de cobertura no terminal
pytest --cov=. --cov-report=term-missing tests/

# Relatório HTML
pytest --cov=. --cov-report=html tests/
# Veja: htmlcov/index.html

# Script completo
python tests/run_tests.py --coverage --html
```

## 📊 Interpretação dos Resultados

### ✅ **Testes Passando**
- Todos os componentes estão funcionando corretamente
- Dados estão consistentes e válidos
- Repository segue padrões Repl.ET

### ⚠️ **Warnings**
- Arquivos opcionais ausentes (podem ser ignorados)
- Schemas não encontrados (verifique estrutura)

### ❌ **Falhas**
- **Schema validation errors**: Corrigir campos obrigatórios em JSONs
- **Data integrity errors**: Verificar consistência entre arquivos
- **File not found errors**: Adicionar arquivos referenciados

## 🔧 Configuração

### `pytest.ini`
Configuração central do pytest com:
- Marcadores de teste (unit, integration, slow)
- Supressão de warnings desnecessários
- Formatação de output

### `conftest.py`
Fixtures compartilhadas:
- `temp_repo_structure`: Estrutura temporária para testes
- `sample_*`: Dados de exemplo para validação
- `populated_repo`: Repositório completo para testes

## 🎯 Integração com CI/CD

```yaml
# .github/workflows/tests.yml
- name: Run tests
  run: |
    pip install -r requirements.txt
    python tests/run_tests.py --coverage
```

## 📈 Métricas de Qualidade

Os testes verificam:
- **100% dos schemas** são válidos JSON Schema Draft 7
- **Todos os JSONs** validam contra seus schemas
- **Consistência cross-file** de IDs e referências
- **Scoring bounds** (0.0 ≤ score ≤ 1.0)
- **Estrutura de arquivos** conforme padrão Repl.ET

---

**Execute `python tests/run_tests.py --help` para todas as opções disponíveis.** 