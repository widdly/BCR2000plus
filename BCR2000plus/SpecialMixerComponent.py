from __future__ import absolute_import, print_function, unicode_literals
from _Framework.MixerComponent import MixerComponent
from .SpecialChannelStripComponent import SpecialChannelStripComponent
class SpecialMixerComponent(MixerComponent):
    u' Special mixer class that uses return tracks alongside midi and audio tracks '
    __module__ = __name__

    def __init__(self, num_tracks):
        MixerComponent.__init__(self, num_tracks)



    def tracks_to_use(self):
        return tuple(self.song().visible_tracks) + tuple(self.song().return_tracks)



    def _create_strip(self):
        return SpecialChannelStripComponent()

