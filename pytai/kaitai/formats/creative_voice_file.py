# Creative Commons Legal Code
#
# CC0 1.0 Universal
#
#     CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
#     LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
#     ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
#     INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
#     REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
#     PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
#     THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
#     HEREUNDER.
#
# Statement of Purpose
#
# The laws of most jurisdictions throughout the world automatically confer
# exclusive Copyright and Related Rights (defined below) upon the creator
# and subsequent owner(s) (each and all, an "owner") of an original work of
# authorship and/or a database (each, a "Work").
#
# Certain owners wish to permanently relinquish those rights to a Work for
# the purpose of contributing to a commons of creative, cultural and
# scientific works ("Commons") that the public can reliably and without fear
# of later claims of infringement build upon, modify, incorporate in other
# works, reuse and redistribute as freely as possible in any form whatsoever
# and for any purposes, including without limitation commercial purposes.
# These owners may contribute to the Commons to promote the ideal of a free
# culture and the further production of creative, cultural and scientific
# works, or to gain reputation or greater distribution for their Work in
# part through the use and efforts of others.
#
# For these and/or other purposes and motivations, and without any
# expectation of additional consideration or compensation, the person
# associating CC0 with a Work (the "Affirmer"), to the extent that he or she
# is an owner of Copyright and Related Rights in the Work, voluntarily
# elects to apply CC0 to the Work and publicly distribute the Work under its
# terms, with knowledge of his or her Copyright and Related Rights in the
# Work and the meaning and intended legal effect of CC0 on those rights.
#
# 1. Copyright and Related Rights. A Work made available under CC0 may be
# protected by copyright and related or neighboring rights ("Copyright and
# Related Rights"). Copyright and Related Rights include, but are not
# limited to, the following:
#
#   i. the right to reproduce, adapt, distribute, perform, display,
#      communicate, and translate a Work;
#  ii. moral rights retained by the original author(s) and/or performer(s);
# iii. publicity and privacy rights pertaining to a person's image or
#      likeness depicted in a Work;
#  iv. rights protecting against unfair competition in regards to a Work,
#      subject to the limitations in paragraph 4(a), below;
#   v. rights protecting the extraction, dissemination, use and reuse of data
#      in a Work;
#  vi. database rights (such as those arising under Directive 96/9/EC of the
#      European Parliament and of the Council of 11 March 1996 on the legal
#      protection of databases, and under any national implementation
#      thereof, including any amended or successor version of such
#      directive); and
# vii. other similar, equivalent or corresponding rights throughout the
#      world based on applicable law or treaty, and any national
#      implementations thereof.
#
# 2. Waiver. To the greatest extent permitted by, but not in contravention
# of, applicable law, Affirmer hereby overtly, fully, permanently,
# irrevocably and unconditionally waives, abandons, and surrenders all of
# Affirmer's Copyright and Related Rights and associated claims and causes
# of action, whether now known or unknown (including existing as well as
# future claims and causes of action), in the Work (i) in all territories
# worldwide, (ii) for the maximum duration provided by applicable law or
# treaty (including future time extensions), (iii) in any current or future
# medium and for any number of copies, and (iv) for any purpose whatsoever,
# including without limitation commercial, advertising or promotional
# purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
# member of the public at large and to the detriment of Affirmer's heirs and
# successors, fully intending that such Waiver shall not be subject to
# revocation, rescission, cancellation, termination, or any other legal or
# equitable action to disrupt the quiet enjoyment of the Work by the public
# as contemplated by Affirmer's express Statement of Purpose.
#
# 3. Public License Fallback. Should any part of the Waiver for any reason
# be judged legally invalid or ineffective under applicable law, then the
# Waiver shall be preserved to the maximum extent permitted taking into
# account Affirmer's express Statement of Purpose. In addition, to the
# extent the Waiver is so judged Affirmer hereby grants to each affected
# person a royalty-free, non transferable, non sublicensable, non exclusive,
# irrevocable and unconditional license to exercise Affirmer's Copyright and
# Related Rights in the Work (i) in all territories worldwide, (ii) for the
# maximum duration provided by applicable law or treaty (including future
# time extensions), (iii) in any current or future medium and for any number
# of copies, and (iv) for any purpose whatsoever, including without
# limitation commercial, advertising or promotional purposes (the
# "License"). The License shall be deemed effective as of the date CC0 was
# applied by Affirmer to the Work. Should any part of the License for any
# reason be judged legally invalid or ineffective under applicable law, such
# partial invalidity or ineffectiveness shall not invalidate the remainder
# of the License, and in such case Affirmer hereby affirms that he or she
# will not (i) exercise any of his or her remaining Copyright and Related
# Rights in the Work or (ii) assert any associated claims and causes of
# action with respect to the Work, in either case contrary to Affirmer's
# express Statement of Purpose.
#
# 4. Limitations and Disclaimers.
#
#  a. No trademark or patent rights held by Affirmer are waived, abandoned,
#     surrendered, licensed or otherwise affected by this document.
#  b. Affirmer offers the Work as-is and makes no representations or
#     warranties of any kind concerning the Work, express, implied,
#     statutory or otherwise, including without limitation warranties of
#     title, merchantability, fitness for a particular purpose, non
#     infringement, or the absence of latent or other defects, accuracy, or
#     the present or absence of errors, whether or not discoverable, all to
#     the greatest extent permissible under applicable law.
#  c. Affirmer disclaims responsibility for clearing rights of other persons
#     that may apply to the Work or any use thereof, including without
#     limitation any person's Copyright and Related Rights in the Work.
#     Further, Affirmer disclaims responsibility for obtaining any necessary
#     consents, permissions or other rights required for any use of the
#     Work.
#  d. Affirmer understands and acknowledges that Creative Commons is not a
#     party to this document and has no duty or obligation with respect to
#     this CC0 or use of the Work.

# This file was compiled from a KSY format file downloaded from:
# https://github.com/kaitai-io/kaitai_struct_formats


# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class CreativeVoiceFile(KaitaiStruct):
    """Creative Voice File is a container file format for digital audio
    wave data. Initial revisions were able to support only unsigned
    8-bit PCM and ADPCM data, later versions were revised to add support
    for 16-bit PCM and a-law / u-law formats.
    
    This format was actively used in 1990s, around the advent of
    Creative's sound cards (Sound Blaster family). It was a popular
    choice for a digital sound container in lots of games and multimedia
    software due to simplicity and availability of Creative's recording
    / editing tools.
    
    .. seealso::
       Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice
    """

    class BlockTypes(Enum):
        terminator = 0
        sound_data = 1
        sound_data_cont = 2
        silence = 3
        marker = 4
        text = 5
        repeat_start = 6
        repeat_end = 7
        extra_info = 8
        sound_data_new = 9

    class Codecs(Enum):
        pcm_8bit_unsigned = 0
        adpcm_4bit = 1
        adpcm_2_6bit = 2
        adpcm_2_bit = 3
        pcm_16bit_signed = 4
        alaw = 6
        ulaw = 7
        adpcm_4_to_16bit = 512
    SEQ_FIELDS = ["magic", "header_size", "version", "checksum", "blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(20)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x43\x72\x65\x61\x74\x69\x76\x65\x20\x56\x6F\x69\x63\x65\x20\x46\x69\x6C\x65\x1A":
            raise kaitaistruct.ValidationNotEqualError(b"\x43\x72\x65\x61\x74\x69\x76\x65\x20\x56\x6F\x69\x63\x65\x20\x46\x69\x6C\x65\x1A", self.magic, self._io, u"/seq/0")
        self._debug['header_size']['start'] = self._io.pos()
        self.header_size = self._io.read_u2le()
        self._debug['header_size']['end'] = self._io.pos()
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u2le()
        self._debug['version']['end'] = self._io.pos()
        self._debug['checksum']['start'] = self._io.pos()
        self.checksum = self._io.read_u2le()
        self._debug['checksum']['end'] = self._io.pos()
        self._debug['blocks']['start'] = self._io.pos()
        self.blocks = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['blocks']:
                self._debug['blocks']['arr'] = []
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            _t_blocks = CreativeVoiceFile.Block(self._io, self, self._root)
            _t_blocks._read()
            self.blocks.append(_t_blocks)
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['blocks']['end'] = self._io.pos()

    class BlockMarker(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x04:_Marker
        """
        SEQ_FIELDS = ["marker_id"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['marker_id']['start'] = self._io.pos()
            self.marker_id = self._io.read_u2le()
            self._debug['marker_id']['end'] = self._io.pos()


    class BlockSilence(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x03:_Silence
        """
        SEQ_FIELDS = ["duration_samples", "freq_div"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['duration_samples']['start'] = self._io.pos()
            self.duration_samples = self._io.read_u2le()
            self._debug['duration_samples']['end'] = self._io.pos()
            self._debug['freq_div']['start'] = self._io.pos()
            self.freq_div = self._io.read_u1()
            self._debug['freq_div']['end'] = self._io.pos()

        @property
        def sample_rate(self):
            if hasattr(self, '_m_sample_rate'):
                return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None

            self._m_sample_rate = (1000000.0 / (256 - self.freq_div))
            return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None

        @property
        def duration_sec(self):
            """Duration of silence, in seconds."""
            if hasattr(self, '_m_duration_sec'):
                return self._m_duration_sec if hasattr(self, '_m_duration_sec') else None

            self._m_duration_sec = (self.duration_samples / self.sample_rate)
            return self._m_duration_sec if hasattr(self, '_m_duration_sec') else None


    class BlockSoundDataNew(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x09:_Sound_data_.28New_format.29
        """
        SEQ_FIELDS = ["sample_rate", "bits_per_sample", "num_channels", "codec", "reserved", "wave"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['sample_rate']['start'] = self._io.pos()
            self.sample_rate = self._io.read_u4le()
            self._debug['sample_rate']['end'] = self._io.pos()
            self._debug['bits_per_sample']['start'] = self._io.pos()
            self.bits_per_sample = self._io.read_u1()
            self._debug['bits_per_sample']['end'] = self._io.pos()
            self._debug['num_channels']['start'] = self._io.pos()
            self.num_channels = self._io.read_u1()
            self._debug['num_channels']['end'] = self._io.pos()
            self._debug['codec']['start'] = self._io.pos()
            self.codec = KaitaiStream.resolve_enum(CreativeVoiceFile.Codecs, self._io.read_u2le())
            self._debug['codec']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(4)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['wave']['start'] = self._io.pos()
            self.wave = self._io.read_bytes_full()
            self._debug['wave']['end'] = self._io.pos()


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["block_type", "body_size1", "body_size2", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['block_type']['start'] = self._io.pos()
            self.block_type = KaitaiStream.resolve_enum(CreativeVoiceFile.BlockTypes, self._io.read_u1())
            self._debug['block_type']['end'] = self._io.pos()
            if self.block_type != CreativeVoiceFile.BlockTypes.terminator:
                self._debug['body_size1']['start'] = self._io.pos()
                self.body_size1 = self._io.read_u2le()
                self._debug['body_size1']['end'] = self._io.pos()

            if self.block_type != CreativeVoiceFile.BlockTypes.terminator:
                self._debug['body_size2']['start'] = self._io.pos()
                self.body_size2 = self._io.read_u1()
                self._debug['body_size2']['end'] = self._io.pos()

            if self.block_type != CreativeVoiceFile.BlockTypes.terminator:
                self._debug['body']['start'] = self._io.pos()
                _on = self.block_type
                if _on == CreativeVoiceFile.BlockTypes.sound_data_new:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockSoundDataNew(_io__raw_body, self, self._root)
                    self.body._read()
                elif _on == CreativeVoiceFile.BlockTypes.repeat_start:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockRepeatStart(_io__raw_body, self, self._root)
                    self.body._read()
                elif _on == CreativeVoiceFile.BlockTypes.marker:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockMarker(_io__raw_body, self, self._root)
                    self.body._read()
                elif _on == CreativeVoiceFile.BlockTypes.sound_data:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockSoundData(_io__raw_body, self, self._root)
                    self.body._read()
                elif _on == CreativeVoiceFile.BlockTypes.extra_info:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockExtraInfo(_io__raw_body, self, self._root)
                    self.body._read()
                elif _on == CreativeVoiceFile.BlockTypes.silence:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockSilence(_io__raw_body, self, self._root)
                    self.body._read()
                else:
                    self.body = self._io.read_bytes(self.body_size)
                self._debug['body']['end'] = self._io.pos()


        @property
        def body_size(self):
            """body_size is a 24-bit little-endian integer, so we're
            emulating that by adding two standard-sized integers
            (body_size1 and body_size2).
            """
            if hasattr(self, '_m_body_size'):
                return self._m_body_size if hasattr(self, '_m_body_size') else None

            if self.block_type != CreativeVoiceFile.BlockTypes.terminator:
                self._m_body_size = (self.body_size1 + (self.body_size2 << 16))

            return self._m_body_size if hasattr(self, '_m_body_size') else None


    class BlockRepeatStart(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x06:_Repeat_start
        """
        SEQ_FIELDS = ["repeat_count_1"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['repeat_count_1']['start'] = self._io.pos()
            self.repeat_count_1 = self._io.read_u2le()
            self._debug['repeat_count_1']['end'] = self._io.pos()


    class BlockSoundData(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x01:_Sound_data
        """
        SEQ_FIELDS = ["freq_div", "codec", "wave"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['freq_div']['start'] = self._io.pos()
            self.freq_div = self._io.read_u1()
            self._debug['freq_div']['end'] = self._io.pos()
            self._debug['codec']['start'] = self._io.pos()
            self.codec = KaitaiStream.resolve_enum(CreativeVoiceFile.Codecs, self._io.read_u1())
            self._debug['codec']['end'] = self._io.pos()
            self._debug['wave']['start'] = self._io.pos()
            self.wave = self._io.read_bytes_full()
            self._debug['wave']['end'] = self._io.pos()

        @property
        def sample_rate(self):
            if hasattr(self, '_m_sample_rate'):
                return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None

            self._m_sample_rate = (1000000.0 / (256 - self.freq_div))
            return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None


    class BlockExtraInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x08:_Extra_info
        """
        SEQ_FIELDS = ["freq_div", "codec", "num_channels_1"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['freq_div']['start'] = self._io.pos()
            self.freq_div = self._io.read_u2le()
            self._debug['freq_div']['end'] = self._io.pos()
            self._debug['codec']['start'] = self._io.pos()
            self.codec = KaitaiStream.resolve_enum(CreativeVoiceFile.Codecs, self._io.read_u1())
            self._debug['codec']['end'] = self._io.pos()
            self._debug['num_channels_1']['start'] = self._io.pos()
            self.num_channels_1 = self._io.read_u1()
            self._debug['num_channels_1']['end'] = self._io.pos()

        @property
        def num_channels(self):
            """Number of channels (1 = mono, 2 = stereo)."""
            if hasattr(self, '_m_num_channels'):
                return self._m_num_channels if hasattr(self, '_m_num_channels') else None

            self._m_num_channels = (self.num_channels_1 + 1)
            return self._m_num_channels if hasattr(self, '_m_num_channels') else None

        @property
        def sample_rate(self):
            if hasattr(self, '_m_sample_rate'):
                return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None

            self._m_sample_rate = (256000000.0 / (self.num_channels * (65536 - self.freq_div)))
            return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None



