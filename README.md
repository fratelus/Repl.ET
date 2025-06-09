# Repl.ET: Eye Tracking Replication Template

Este repositório segue o padrão Repl.ET para experimentos de rastreamento ocular em Engenharia de Software e Interação Humano-Computador.

## Objetivos
- Promover reprodutibilidade crítica
- Alinhar-se a diretrizes internacionais (FAIR, PRISMA-Eye, iGuidelines, TRRRACED)
- Servir como template validado para submissão científica

## Estrutura
Veja a árvore de diretórios e arquivos padronizados no repositório.

## Como usar

### 1. Instalação
```bash
pip install -r requirements.txt
```

### 2. Preencha os dados
- Edite os arquivos JSON com os dados do seu estudo
- Todos os schemas estão em `schemas/` para referência

### 3. Validação
```bash
python validate_jsons.py
```

### 4. Avaliação de reprodutibilidade
```bash
python repl_et_score.py
```
Gera: `report.json`, `report.md` e `score.png`

### 5. Executar testes
```bash
# Todos os testes
pytest tests/

# Apenas testes unitários (rápidos)
pytest -m unit tests/

# Com relatório de cobertura
python tests/run_tests.py --coverage --html
```

### 6. Checklist final
- Consulte `repl_et_checklist.md` para garantir conformidade
- Use `environment.yml` para reprodutibilidade computacional

## Licença
Consulte o arquivo LICENSE para detalhes.

## Citação
Veja o arquivo `CITATION.cff` para citação recomendada. 