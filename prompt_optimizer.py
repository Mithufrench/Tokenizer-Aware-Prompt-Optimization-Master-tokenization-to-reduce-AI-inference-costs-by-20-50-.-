#!/usr/bin/env python3
"""
Advanced Prompt Optimizer
Demonstrates tokenizer-aware techniques
Author: Mohammad Saiful Islam
"""

import tiktoken
from typing import Dict, Tuple

def optimize_prompt(prompt: str, model: str = "gpt-4o") -> Tuple[str, Dict]:
    """Apply basic tokenizer-aware optimizations."""
    encoding = tiktoken.encoding_for_model(model)
    
    # Simple optimizations
    optimized = prompt.strip()
    optimized = " ".join(optimized.split())  # Remove extra whitespace
    
    # Replace verbose phrases with dense equivalents (example rules)
    replacements = {
        "provide a comprehensive analysis of": "analyze",
        "underlying factors contributing to the phenomenon of": "causes of",
        "suggest meaningful solutions": "suggest solutions",
    }
    
    for old, new in replacements.items():
        optimized = optimized.replace(old, new)
    
    original_tokens = len(encoding.encode(prompt))
    optimized_tokens = len(encoding.encode(optimized))
    
    stats = {
        "original_tokens": original_tokens,
        "optimized_tokens": optimized_tokens,
        "savings_percent": round((original_tokens - optimized_tokens) / original_tokens * 100, 1)
    }
    
    return optimized, stats

if __name__ == "__main__":
    test_prompt = """Please provide a comprehensive analysis of the underlying factors contributing to the phenomenon of climate change and suggest meaningful solutions for individuals and governments."""
    
    optimized, stats = optimize_prompt(test_prompt)
    
    print("Original:", test_prompt)
    print("\nOptimized:", optimized)
    print("\nStats:", stats)
    print(f"\nToken Savings: {stats['savings_percent']}%")