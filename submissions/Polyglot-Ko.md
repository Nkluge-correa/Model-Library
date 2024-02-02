# Polyglot-Ko

## Model Details

- Name: [Polyglot-Ko](https://huggingface.co/EleutherAI/polyglot-ko-12.8b) 📚
- Model Size: 12.8B
- Dataset: 863 GB of Korean language data curated by [TUNiB](https://tunib.ai/)
- Input/Output Format: Text
- Research Field: Natural Language Processing
- Contains an Impact Assessment: Yes
- Associated Risks: Disinformation, Algorithmic Discrimination, Social Engineering, Environmental Impacts
- Date of Publication: 4/3/2023
- Organization: [EleutherAI](https://www.eleuther.ai) (Non-profit)
- Country/Origin: United States of America
- License: Apache 2.0 License
- Publication: [A Technical Report for Polyglot-Ko: Open-Source Large-Scale Korean Language Models](https://arxiv.org/abs/2306.02254)

## Description

[Polyglot-Ko](https://huggingface.co/EleutherAI/polyglot-ko-12.8b/tree/main) is a series of large-scale Korean autoregressive language models made by the EleutherAI polyglot team, available in sizes from 1.3B to 12.8B. The model consists of 40 transformer layers with a model dimension of 5120 and a feedforward dimension of 20480. The model dimension is split into 40 heads, each with a dimension of 128. Rotary Position Embedding ([RoPE](https://arxiv.org/abs/2104.09864)) is applied to 64 dimensions of each head. The model is trained with a tokenization vocabulary of 30003. Polyglot-Ko-12.8B was trained for 167 billion tokens over 301,000 steps on 256 A100 GPUs with the GPT-NeoX framework. It was trained as an autoregressive language model, using cross-entropy loss to maximize the likelihood of predicting the next token.

Polyglot-Ko-12.8B was trained on 863 GB of Korean language data (1.2TB before processing), a large-scale dataset curated by [TUNiB](https://www.tunib.ai/). The data collection process has abided by South Korean laws, and it will not be released for public use.

All Polyglot-Ko models are released under the Apache 2.0 License.

## Organization

[EleutherAI](https://www.eleuther.ai/) is a non-profit artificial intelligence research group. The group was formed in a Discord server in July 2020 to organize a replication of GPT-3. In early 2023, it formally incorporated as the EleutherAI Foundation, a non-profit research institute.  
  
According to its [mission statement](https://www.eleuther.ai/about), EleutherAI seeks to (1) advance research on the interpretability and alignment of foundation models, (2) ensure that the ability to study foundation models is not restricted to a handful of companies, and (3) educate people about the capabilities, limitations, and risks associated with these technologies.
