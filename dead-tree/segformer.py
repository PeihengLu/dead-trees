"""
 training and inference script for segformer
"""
# huggingface transformers
from transformers import SegformerConfig, SegformerForImageSegmentation
import torch

# yaml config parser
import yaml

