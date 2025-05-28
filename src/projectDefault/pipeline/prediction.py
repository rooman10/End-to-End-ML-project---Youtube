#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 26 15:24:12 2025

@author: harshadahake
"""

import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
    
    def predict(self, data):
        prediction = self.model.predict(data)
        
        return prediction
    