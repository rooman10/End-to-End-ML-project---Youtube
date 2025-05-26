#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 26 14:57:35 2025

@author: harshadahake
"""

from src.projectDefault.config.configuration import ConfigurationManager
from src.projectDefault.components.model_evaluation import ModelEvaluation
from src.projectDefault.logging import logger

STAGE_NAME = "Model Evaluation"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config = model_evaluation_config)
        model_evaluation.save_result()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise(e)