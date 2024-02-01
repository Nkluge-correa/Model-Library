# GPT-NeoX

## Model Details

- Name: [GPT-NeoX](https://huggingface.co/EleutherAI/gpt-neox-20b) 📚
- Model Size: 20B
- Dataset: [The Pile](https://pile.eleuther.ai/)
- Input/Output Format: Text
- Research Field: Deep Learning, Natural Language Processing
- Contains an Impact Assessment: Yes
- Associated Risks: Disinformation, Algorithmic Discrimination, Social Engineering, Environmental Impacts
- Date of Publication: 4/14/2022
- Organization: [EleutherAI](https://www.eleuther.ai) (Non-profit)
- Country/Origin: United States of America
- License: Apache 2.0 License
- Publication: [GPT-NeoX-20B: An Open-Source Autoregressive Language Model](https://arxiv.org/abs/2204.06745)

## Description

GPT-Neo is a series of large language autoregressive models, from [125M](https://huggingface.co/EleutherAI/gpt-neo-125m) to [20B parameter](https://huggingface.co/EleutherAI/gpt-neox-20b), trained on the Pile, openly available to the public through a permissive license. The GPT-Neo series is EleutherAI's replication of the GPT-3 architecture, while GPT-NeoX is the 20B parameter version. At the time of submission, GPT-NeoX was the largest dense autoregressive model with publicly available weights.

EleutherAI used model parallelism to train GPT-NeoX on a single machine with multiple GPUs, using a combination of techniques such as gradient checkpointing, pipeline parallelism, and mixed precision training to train efficiently. Instead of the learned positional embeddings used in GPT models, the GPT-Neo series uses [rotary embeddings](https://arxiv.org/abs/2104.09864). The final result is GPT-NeoX, which achieves state-of-the-art results on several benchmarks such as LAMBADA, SuperGLUE, and Pile-MNLI.

All GPT-Neo models are open-sourced and licensed under the Apache 2.0 license.

## Organization

[EleutherAI](https://www.eleuther.ai/) is a non-profit artificial intelligence research group. The group was formed in a Discord server in July 2020 to organize a replication of GPT-3. In early 2023, it formally incorporated as the EleutherAI Foundation, a non-profit research institute.

According to its [mission statement](https://www.eleuther.ai/about), EleutherAI seeks to (1) advance research on the interpretability and alignment of foundation models, (2) ensure that the ability to study foundation models is not restricted to a handful of companies, and (3) educate people about the capabilities, limitations, and risks associated with these technologies.
