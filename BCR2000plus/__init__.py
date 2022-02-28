from __future__ import absolute_import, print_function, unicode_literals
from .BCR2000plus import BCR2000plus
import Live 

def create_instance(c_instance):
    u' Creates and returns the BCR2000plus script '
    return BCR2000plus(c_instance)

