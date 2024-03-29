# WebGPT

## Model Details

- Name: [WebGPT](https://arxiv.org/abs/2112.09332) 📚
- Model Size: 175B
- Dataset: A collection of demonstrations and comparisons made by freelance contractors from [Upwork](https://www.upwork.com) and [Surge AI](https://www.surgehq.ai)
- Input/Output Format: Text
- Research Field: Reinforcement Learning, Natural Language Processing
- Contains an Impact Assessment: Yes
- Associated Risks: Disinformation, Algorithmic Discrimination, Social Engineering, Environmental Impacts, Technological Unemployment
- Date of Publication: 12/17/2021
- Organization: [OpenAI Inc.](https://openai.com/) (Non-profit)
- Country/Origin: United States of America
- License: Proprietary License
- Publication: [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332)

## Description

[WebGPT](https://openai.com/research/webgpt) is a fine-tuned version of [GPT-3](https://arxiv.org/abs/2005.14165). While GPT-3 tends to hallucinate information when performing tasks requiring real-world knowledge, WebGPT was trained to search the web via a text-based web browser and generate responses via the retrieved information.
  
The model was tuned through a combination of imitation learning and behavior cloning (using human experts as a reference signal), reinforcement learning from human feedback, and rejection sampling, where a reward model trained by human feedback was used to sample the best responses generated by the model. The comparisons evaluated by WebGPT can be found in [this repository](https://huggingface.co/datasets/openai/webgpt_comparisons).
  
WebGPT was evaluated against benchmarks such as [ELI5](https://arxiv.org/abs/1907.09190) and [TruthfulQA](https://arxiv.org/abs/2109.07958), demonstrating superior performance to its foundation in matters of response preferability and factual groundness.

## Organization

[OpenAI](https://openai.com/) is an American artificial intelligence research laboratory consisting of the non-profit OpenAI, Inc. and its for-profit subsidiary corporation OpenAI, L.P, founded in 2015 by Ilya Sutskever, Greg Brockman, Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, Jessica Livingston, John Schulman, Pamela Vagata, and Wojciech Zaremba. Their mission "_is to ensure that General Artificial Intelligence benefits all of humanity_."  
  
The organization maintains an active research and development agenda in AI Safety. In "_[Our approach to AI safety](https://openai.com/blog/our-approach-to-ai-safety)_", OpenAI states that it is committed to keeping Artificial Intelligence safe and broadly beneficial.
