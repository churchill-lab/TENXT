# -*- coding: utf-8 -*-

"""Top-level package for PoolClass"""
import os

__author__ = 'Kwangbom \"KB\" Choi, Ph.D.'
__email__ = 'kb.choi@jax.org'
__version__ = '0.1.0'
__logo__ = """
 ___   ___   ___   _     __    _      __    __   __  
| |_) / / \ / / \ | |   / /`  | |    / /\  ( (` ( (` 
|_|   \_\_/ \_\_/ |_|__ \_\_, |_|__ /_/--\ _)_) _)_) 
                                              v""" + __version__
__all__ = ['.']

_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_data(path):
    return os.path.join(_ROOT, 'external', path)