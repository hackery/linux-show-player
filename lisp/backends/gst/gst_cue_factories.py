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

from ast import literal_eval

from lisp.backends.gst.gst_media import GstMedia
from lisp.cues.cue_factory import CueFactory
from lisp.cues.media_cue import MediaCue
from lisp.utils.configuration import config


def gst_media(pipeline=None):
    media = GstMedia()

    if pipeline is not None:
        media.pipe = pipeline

    return MediaCue(media)


def uri_audio(uri=None):
    cue = gst_media(pipeline=compose_pipeline('URIInput'))

    if uri is not None:
        cue.media.element('URIInput').uri = uri

    return cue


def capture_audio():
    return gst_media(pipeline=compose_pipeline('AutoSrc'))


def compose_pipeline(input_element):
    return (input_element,) +\
           tuple(config['Gst']['Pipeline'].replace(' ', '').split(','))


def register_factories():
    CueFactory.register_factory('MediaCue', gst_media)
    CueFactory.register_factory('URIAudioCue', uri_audio)
    CueFactory.register_factory('CaptureAudioCue', capture_audio)
