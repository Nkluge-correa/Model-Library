# InstructGPT

## Model Details

- Name: [InstructGPT](https://arxiv.org/abs/2203.02155) 📚
- Model Size: 175B
- Dataset: Prompt/completion pairs submitted to the OpenAI API
- Input/Output Format: Text
- Research Field: Deep Learning, Reinforcement Learning, Natural Language Processing
- Contains an Impact Assessment: Yes
- Associated Risks: Disinformation, Algorithmic Discrimination, Social Engineering, Malware Development, Environmental Impacts, Technological Unemployment, Intelectual Fraud
- Date of Publication: 3/4/2022
- Organization: [OpenAI Inc.](https://openai.com/) (Non-profit)
- Country/Origin: United States of America
- License: Proprietary License
- Publication: [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155)

## Description

[InstructGPT](https://arxiv.org/abs/2203.02155) is a fined-tuned version of OpenAI's [GPT-3](https://arxiv.org/abs/2005.14165), achieved via a mix of supervised fine-tuning and reinforcement learning from human feedback. While GPT-3 was trained via causal language modeling, that is, to predict the next token in a sequence of tokens, InstructGPT was trained to model (minimize cross-entropy loss) the distribution of its fine-tuning dataset, comprised of human demonstrations of appropriate instruction-following behavior, and later to maximize the cumulative reward of a learning signal that serves as a proxy for human evaluations.

In general, this process can be divided into three steps: (1) Prompt/compilation pairs are collected (using human contractors to create them) and used to fine-tune the base model (GPT-3). (2) After fine-tuning, the model generates several outputs per sample (prompt). Crowdsourced human evaluators then score each output. This scoring is then used to train a reward model. (3) The reward model is then used to update the fine-tuned model again via [proximal policy optimization](https://openai.com/blog/openai-baselines-ppo/).

The final result of this process is InstructGPT, which comes in three different sizes (1.3B, 6B, and 175B parameters), fine-tuned from the Babbage, Curie, and Davinci versions of GPT-3 (currently deprecated). InstructGPT represents a significant advance towards alignment when compared to other LLMs, being capable of creating fewer imitative falsehoods, making up facts less frequently, and generating more acceptable outputs. InstructGPT can be said to be a predecessor of more capable/aligned models, like [ChatGPT](https://openai.com/blog/chatgpt/).

## Organization

[OpenAI](https://openai.com/) is an American artificial intelligence research laboratory consisting of the non-profit OpenAI, Inc. and its for-profit subsidiary corporation OpenAI, L.P, founded in 2015 by Ilya Sutskever, Greg Brockman, Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, Jessica Livingston, John Schulman, Pamela Vagata, and Wojciech Zaremba. Their mission "_is to ensure that General Artificial Intelligence benefits all of humanity_."  
  
The organization maintains an active research and development agenda in AI Safety. In "_[Our approach to AI safety](https://openai.com/blog/our-approach-to-ai-safety)_", OpenAI states that it is committed to keeping Artificial Intelligence safe and broadly beneficial.
