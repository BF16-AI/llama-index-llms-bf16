# llama-index-llms-bf16

Official [LlamaIndex](https://docs.llamaindex.ai/) LLM adapter for [**bf16.ai**](https://bf16.ai) — 1M-context uncensored open-weight LLMs with strict Zero Data Retention (`ZDR`).

## Installation

```bash
pip install llama-index-llms-bf16
```

## Quick Start

```python
from llama_index.llms.bf16 import BF16

llm = BF16(model="deepseek/deepseek-v4.1-flash-uncensored")
print(llm.complete("Summarize how 1M context helps whole-repo RAG."))
```

Set `BF16_API_KEY` (or pass `api_key=...`). Supports `context_window=1048576` and native tool calling out of the box.

## Links

- Website: https://bf16.ai
- Docs: https://bf16.ai/docs
- Live Models & Pricing: https://bf16.ai/models
- Open-Source `$50` API Grants: https://bf16.ai/open-source
