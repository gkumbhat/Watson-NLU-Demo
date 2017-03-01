"""
noteable alchemyapi app setup
"""


from flask import Flask, g
import os

# Set up app with debugging
app = Flask(__name__)
