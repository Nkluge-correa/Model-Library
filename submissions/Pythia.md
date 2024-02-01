# Pythia

## Model Details

- Name: [Pythia](https://huggingface.co/EleutherAI/pythia-12b) 📚
- Model Size: 12B
- Dataset: [The Pile](https://pile.eleuther.ai/)
- Input/Output Format: Text
- Research Field: Deep Learning, Natural Language Processing
- Contains an Impact Assessment: Yes
- Associated Risks: ☣️ Disinformation, Algorithmic Discrimination, Social Engineering, Environmental Impacts ☣️
- Date of Publication: 4/3/2023
- Organization: [EleutherAI](https://www.eleuther.ai) (Non-profit)
- Country/Origin: United States of America
- License: Apache 2.0 License
- Publication: [Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling](https://arxiv.org/abs/2304.01373)

## Description

[Pythia](https://huggingface.co/EleutherAI/pythia-12b) is a collection of models developed to facilitate interpretability research, trained on sizes 70M, 160M, 410M, 1B, 1.4B, 2.8B, 6.9B, and 12B. For each size, there are two models: one trained on the Pile, and one trained on the Pile after the dataset has been globally deduplicated. All 8 model sizes are trained on the same data, in the same order. EleutherAI also provides 154 intermediate checkpoints per model, hosted on Hugging Face as branches.

The Pythia model suite was deliberately designed to promote scientific research on large language models, especially interpretability research. Despite not centering downstream performance as a design goal, Pythia models [match or exceed](https://huggingface.co/EleutherAI/pythia-12b#evaluations)  the performance of similar and same-sized models, such as those in the OPT and GPT-Neo suites.

All Pythia models are released under the Apache 2.0 License.

## Organization

[EleutherAI](https://www.eleuther.ai/) is a non-profit artificial intelligence research group. The group was formed in a Discord server in July 2020 to organize a replication of GPT-3. In early 2023, it formally incorporated as the EleutherAI Foundation, a non-profit research institute.  
  
According to its [mission statement](https://www.eleuther.ai/about), EleutherAI seeks to (1) advance research on the interpretability and alignment of foundation models, (2) ensure that the ability to study foundation models is not restricted to a handful of companies, and (3) educate people about the capabilities, limitations, and risks associated with these technologies.

