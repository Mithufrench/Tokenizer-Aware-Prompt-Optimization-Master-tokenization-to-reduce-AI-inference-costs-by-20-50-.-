#!/usr/bin/env python3
"""
Tokenizer Demo for Tokenizer-Aware Prompt Optimization
Author: Mohammad Saiful Islam
"""

import tiktoken

def count_tokens(text: str, model: str = "gpt-4o") -> int:
    """Count tokens for a given text using tiktoken."""
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)

def compare_prompts(original: str, optimized: str, model: str = "gpt-4o"):
    """Compare token counts between original and optimized prompts."""
    orig_tokens = count_tokens(original, model)
    opt_tokens = count_tokens(optimized, model)
    
    print("=== Prompt Token Comparison ===")
    print(f"Original Prompt Tokens: {orig_tokens}")
    print(f"Optimized Prompt Tokens: {opt_tokens}")
    print(f"Savings: {orig_tokens - opt_tokens} tokens ({((orig_tokens - opt_tokens)/orig_tokens)*100:.1f}%)")
    
    # Show token breakdown (first 20 tokens)
    encoding = tiktoken.encoding_for_model(model)
    print("\nSample Token Breakdown (Original):")
    print(encoding.encode(original)[:20])

if __name__ == "__main__":
    # Example usage
    original = """Please provide a comprehensive analysis of the underlying factors contributing to the phenomenon of climate change and suggest meaningful solutions."""
    
    optimized = """Analyze main causes of climate change and suggest practical solutions."""
    
    compare_prompts(original, optimized)
    
    print("\n💡 Tip: Always test with the exact tokenizer of your target model!")