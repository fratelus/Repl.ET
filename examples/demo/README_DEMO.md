# 🎯 Repl.ET Demo: Eye Movements in Code Review

Este é um **exemplo completo e realista** do repositório Repl.ET, baseado em uma replicação hipotética do estudo de Kip et al. sobre movimentos oculares durante revisão de código.

## 📊 Sobre o Estudo Demo

- **Objetivo**: Replicar os achados de como desenvolvedores examinam código para detectar bugs vs. compreensão
- **Participantes**: 5 desenvolvedores Java (2-8 anos de experiência)
- **Estímulos**: 5 métodos Java (3 com bugs, 2 limpos)
- **Equipment**: Tobii Pro X3-120 (120Hz)
- **Métricas**: Duração de fixação, contagem de regressões, tempo em AOIs

## 🗂️ Estrutura do Demo

```
Demo/ReplET/
├── metadata.json                    # Metadados completos do estudo
├── participants/                    # 5 participantes realistas
├── equipment/                       # Specs detalhadas do eye tracker
├── stimuli/                        
│   ├── stimuli_raw/                # 5 arquivos Java (.java)
│   ├── stimuli_metadata.json      # Metadados dos estímulos
│   └── stimuli_annotations.json   # Ground truth dos bugs
├── aois/                           # 12 AOIs definidas
├── collection/
│   ├── protocol.json              # Protocolo detalhado
│   └── logs/session_P01.log       # Exemplo de log de sessão
├── preprocessing/                  # Pipeline de 6 etapas
├── analysis/
│   ├── results_tables/            # Dados de exemplo (CSV)
│   └── analysis.json              # Métricas e métodos
├── validity/                      # Ameaças e limitações
└── reproducibility/               # DOI, preregistro, etc.
```

## 🧪 Como Testar o Demo

1. **Navegue para a pasta Demo**:
   ```bash
   cd Demo/ReplET
   ```

2. **Valide todos os JSONs**:
   ```bash
   python validate_jsons.py
   ```

3. **Execute avaliação de reprodutibilidade**:
   ```bash
   python repl_et_score.py
   ```

4. **Veja os resultados**:
   - `report.json`: Pontuações por eixo
   - `score.png`: Gráfico radar
   - `report.md`: Sumário interpretável

5. **Execute os testes automatizados**:
   ```bash
   pytest tests/
   # ou com cobertura:
   python tests/run_tests.py --coverage --html
   ```

## 🎯 Dados Realistas Incluídos

- **Código Java** com bugs reais (off-by-one, null pointer, recursão infinita)
- **AOIs** baseadas em elementos sintáticos do código
- **Métricas** padrão de eye tracking (duração, regressões, scanpaths)
- **Protocolo** detalhado de calibração e controle de qualidade
- **Análises estatísticas** usando métodos apropriados (ANOVA, mixed models)

## 📈 Exemplo de Resultados Esperados

O demo deve gerar pontuações altas (0.75-1.0) para a maioria dos eixos, demonstrando um estudo bem documentado e reprodutível conforme padrões FAIR e diretrizes de eye tracking.

---

**Este demo serve como template de referência para pesquisadores implementarem seus próprios estudos usando o padrão Repl.ET.** 