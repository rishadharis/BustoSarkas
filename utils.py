import os
import streamlit as st
from typing import Any, Optional

def get_config(key: str, default: Optional[Any] = None) -> Any:
    """
    Retrieve configuration value from environment variables or Streamlit secrets.
    Prioritizes environment variables (os.getenv).
    Falls back to streamlit.secrets if not found in env.
    Returns default if not found in either.
    """
    # 1. Try environment variable
    value = os.getenv(key)
    if value is not None:
        return value
    
    # 2. Try Streamlit secrets
    try:
        # Streamlit secrets might be nested or flat, simple access for now
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        # st.secrets might define error if not initialized or properly configured
        pass
    
    # 3. Return default
    return default
