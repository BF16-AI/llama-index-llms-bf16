from llama_index.llms.bf16 import BF16, BF16_BASE_URL


def test_bf16_defaults(monkeypatch):
    monkeypatch.setenv("BF16_API_KEY", "sk-bf16-li-test")
    llm = BF16()
    assert llm.model == "deepseek/deepseek-v4.1-flash-uncensored"
    assert llm.api_base == BF16_BASE_URL
    assert llm.context_window == 1048576
    assert llm.is_chat_model is True
    assert llm.is_function_calling_model is True
