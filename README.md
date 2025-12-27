# 🧪 Teste A/B — Sistema de Recomendação em E-commerce

Este repositório apresenta uma análise de **Teste A/B** com o objetivo de validar, por meio de **teste de hipótese**, se uma nova versão de um site de e-commerce (com sistema de recomendação) apresenta desempenho diferente da versão atual.

Projeto desenvolvido como parte do desafio **#7DaysOfCode – Dados**.

---

## 🎯 Objetivo

Avaliar se a **versão nova do site**, que inclui um sistema de recomendação de produtos, apresenta **taxa de conversão estatisticamente diferente** da versão antiga, sem sistema de recomendação.

---

## 📊 Metodologia

* **Teste A/B (Split Testing)**
* Métrica de sucesso: **Taxa de conversão**
* Amostragem aleatória de **5.000 usuários**
* **Teste Z bicaudal para duas proporções**
* Nível de significância: **α = 0,05**

---

## 🧠 Hipóteses

* **H₀ (Hipótese nula):** a taxa de conversão da versão nova é igual à da versão antiga
* **H₁ (Hipótese alternativa):** a taxa de conversão da versão nova é diferente da versão antiga

---

## 📁 Estrutura do repositório

```
ab-test-recomendacao-ecommerce/
│
├── ab_data.csv                # Dataset do teste A/B
├── teste-hipotese.py          # Script principal com o teste estatístico
├── \images                    # Pasta com gráfico da evolução da taxa de conversão
├── README.md                  # Documentação do projeto
```

---

## 🗂️ Dataset

Base de dados obtida no **Kaggle**, contendo:

* `user_id` — Identificação do usuário
* `timestamp` — Data e hora da interação
* `group` — Grupo do experimento (control / treatment)
* `landing_page` — Página exibida
* `converted` — Conversão (1 = compra, 0 = não compra)

---

## 📈 Resultados

### Análise temporal

O dataset possui a coluna `timestamp`, que permite avaliar o comportamento do Teste A/B ao longo do tempo. A partir dessa informação, foi calculada a **taxa de conversão diária** para os grupos controle e tratamento.

Os resultados iniciais mostram variações naturais ao longo dos dias, por exemplo:

* Em **2017-01-02**, o grupo controle apresentou taxa de conversão de aproximadamente **6,5%**, enquanto o grupo tratamento teve cerca de **3,6%**;
* Em **2017-01-03**, a taxa de conversão do controle foi próxima de **14,3%**, enquanto o tratamento apresentou cerca de **7,0%**.

Apesar dessas oscilações pontuais, não foi observada uma tendência consistente de superioridade do grupo tratamento ao longo do período analisado, o que reforça o resultado do teste estatístico global.

### Taxa de conversão

* **Controle:** 11,83%
* **Tratamento:** 11,21%

### Teste estatístico

* **Z-statistic:** 0,6781
* **p-value:** 0,4977

---

## ✅ Conclusão

Como o **p-value > 0,05**, **não rejeitamos a hipótese nula**.

> Não foi encontrada evidência estatisticamente significativa de que a versão do site com sistema de recomendação apresente desempenho diferente da versão original.

---

## 🛠️ Tecnologias utilizadas

* Python 3.11
* Pandas
* NumPy
* Statsmodels


📌 Projeto desenvolvido para fins educacionais e demonstração de conceitos estatísticos aplicados à Ciência de Dados.
