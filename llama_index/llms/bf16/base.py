import os
from typing import Any, Optional
from llama_index.llms.openai_like import OpenAILike

BF16_BASE_URL = "https://api.bf16.ai/v1"


class BF16(OpenAILike):
    """LlamaIndex LLM wrapper for https://api.bf16.ai/v1 (1M context + ZDR)."""

    def __init__(
        self,
        model: str = "deepseek/deepseek-v4.1-flash-uncensored",
        api_key: Optional[str] = None,
        api_base: str = BF16_BASE_URL,
        context_window: int = 1048576,
        is_chat_model: bool = True,
        is_function_calling_model: bool = True,
        **kwargs: Any,
    ) -> None:
        resolved_key = api_key or os.environ.get("BF16_API_KEY") or os.environ.get("OPENAI_API_KEY") or "missing-bf16-api-key"
        super().__init__(
            model=model,
            api_key=resolved_key,
            api_base=api_base,
            context_window=context_window,
            is_chat_model=is_chat_model,
            is_function_calling_model=is_function_calling_model,
            **kwargs,
        )
