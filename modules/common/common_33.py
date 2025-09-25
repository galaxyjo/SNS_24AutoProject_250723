# modules/common/common_33.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import pandas as pd
import numpy as np

def some_processing_function(data: pd.DataFrame) -> pd.DataFrame:
    # 예시 처리 함수
    df = data.copy()
    df["processed"] = df.select_dtypes(include=[np.number]).sum(axis=1)
    return df
