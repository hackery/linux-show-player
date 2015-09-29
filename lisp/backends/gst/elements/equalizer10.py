# -*- coding: utf-8 -*-
#
# This file is part of Linux Show Player
#
# Copyright 2012-2015 Francesco Ceruti <ceppofrancy@gmail.com>
#
# Linux Show Player is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Linux Show Player is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Linux Show Player.  If not, see <http://www.gnu.org/licenses/>.

from lisp.backends.base.media_element import ElementType, MediaType
from lisp.backends.gst.gst_element import GstMediaElement, GstProperty
from lisp.backends.gst.gi_repository import Gst


class Equalizer10(GstMediaElement):
    ElementType = ElementType.Plugin
    MediaType = MediaType.Audio
    Name = "Equalizer-10bands"

    band0 = GstProperty('equalizer', default=0)
    band1 = GstProperty('equalizer', default=0)
    band2 = GstProperty('equalizer', default=0)
    band3 = GstProperty('equalizer', default=0)
    band4 = GstProperty('equalizer', default=0)
    band5 = GstProperty('equalizer', default=0)
    band6 = GstProperty('equalizer', default=0)
    band7 = GstProperty('equalizer', default=0)
    band8 = GstProperty('equalizer', default=0)
    band9 = GstProperty('equalizer', default=0)

    def __init__(self, pipe):
        super().__init__()

        self.equalizer = Gst.ElementFactory.make("equalizer-10bands", None)
        self.audio_converter = Gst.ElementFactory.make("audioconvert", None)

        pipe.add(self.equalizer)
        pipe.add(self.audio_converter)

        self.equalizer.link(self.audio_converter)

    def sink(self):
        return self.equalizer

    def src(self):
        return self.audio_converter
