import sys,os
from sign_language_detection.exception import SignException
from sign_language_detection.logger import logging
import sys, os
from sign_language_detection.pipeline.training_pipeline import TrainPipeline
from sign_language_detection.exception import SignException
from sign_language_detection.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin


logging.info("Welcome to the project")