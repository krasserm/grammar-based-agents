## Llama-2 agent with grammar-based sampling of function calls

This repository contains the results of my experiments implementing a function calling interface for a Llama-2 chat model 
with [LangChain](https://github.com/langchain-ai/langchain). I used the [grammar-based sampling](https://github.com/ggerganov/llama.cpp/pull/1773)
feature of [llama.cpp](https://github.com/ggerganov/llama.cpp) to ensure that function calls generated by the model follow 
a user-defined schema. The resulting interface is similar to the [ChatOpenAI](https://python.langchain.com/docs/integrations/chat/openai) 
function calling interface and can be used with LangChain's [agent framework](https://python.langchain.com/docs/modules/agents/).

Llama-2 is known to have some zero-shot tool usage capabilities but they are limited. In its current state, the 
implementation is a simple prototype for demonstrating grammar-based sampling in LangChain agents. It is general 
enough to be used with many other language models supported by llama.cpp, after some tweaks to the prompt templates.

## Usage examples

See [example.ipynb](example.ipynb) for usage examples and a more detailed description

## Getting started

### Download model

```shell
mkdir models
wget https://huggingface.co/TheBloke/Llama-2-70B-Chat-GGUF/resolve/main/llama-2-70b-chat.Q4_0.gguf?download=true -O models/llama-2-70b-chat.Q4_0.gguf
```

### Docker image

Either build a [CUDA-enabled llama.cpp Docker image](https://github.com/ggerganov/llama.cpp/blob/master/README.md#docker-with-cuda)
yourself (`full-cuda` variant) or use the pre-build [ghcr.io/krasserm/llama.cpp:full-cuda](https://github.com/krasserm/grammar-based-agents/pkgs/container/llama.cpp)
Docker image as done in the next section.

### Launch server

```shell
docker run --gpus all --rm -p 8080:8080 -v $(realpath models):/models ghcr.io/krasserm/llama.cpp:full-cuda \
  --server -m /models/llama-2-70b-chat.Q4_0.gguf --n-gpu-layers 83 --host 0.0.0.0 --port 8080
```

Depending on available GPU memory you may want to decrease the `--n-gpu-layers` argument.

### Create environment

```shell
conda env create -f environment.yml
conda activate grammar-based-agents
```

### Run examples

```shell
jupyter notebook
```

and then select `example.ipynb`.