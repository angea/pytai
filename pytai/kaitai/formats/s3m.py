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
import collections
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class S3m(KaitaiStruct):
    """Scream Tracker 3 module is a tracker music file format that, as all
    tracker music, bundles both sound samples and instructions on which
    notes to play. It originates from a Scream Tracker 3 music editor
    (1994) by Future Crew, derived from original Scream Tracker 2 (.stm)
    module format.
    
    Instrument descriptions in S3M format allow to use either digital
    samples or setup and control AdLib (OPL2) synth.
    
    Music is organized in so called `patterns`. "Pattern" is a generally
    a 64-row long table, which instructs which notes to play on which
    time measure. "Patterns" are played one-by-one in a sequence
    determined by `orders`, which is essentially an array of pattern IDs
    - this way it's possible to reuse certain patterns more than once
    for repetitive musical phrases.
    
    .. seealso::
       Source - http://hackipedia.org/browse.cgi/File%20formats/Music%20tracker/S3M%2c%20ScreamTracker%203/Scream%20Tracker%203.20%20by%20Future%20Crew.txt
    """
    SEQ_FIELDS = ["song_name", "magic1", "file_type", "reserved1", "num_orders", "num_instruments", "num_patterns", "flags", "version", "samples_format", "magic2", "global_volume", "initial_speed", "initial_tempo", "is_stereo", "master_volume", "ultra_click_removal", "has_custom_pan", "reserved2", "ofs_special", "channels", "orders", "instruments", "patterns", "channel_pans"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['song_name']['start'] = self._io.pos()
        self.song_name = KaitaiStream.bytes_terminate(self._io.read_bytes(28), 0, False)
        self._debug['song_name']['end'] = self._io.pos()
        self._debug['magic1']['start'] = self._io.pos()
        self.magic1 = self._io.read_bytes(1)
        self._debug['magic1']['end'] = self._io.pos()
        if not self.magic1 == b"\x1A":
            raise kaitaistruct.ValidationNotEqualError(b"\x1A", self.magic1, self._io, u"/seq/1")
        self._debug['file_type']['start'] = self._io.pos()
        self.file_type = self._io.read_u1()
        self._debug['file_type']['end'] = self._io.pos()
        self._debug['reserved1']['start'] = self._io.pos()
        self.reserved1 = self._io.read_bytes(2)
        self._debug['reserved1']['end'] = self._io.pos()
        self._debug['num_orders']['start'] = self._io.pos()
        self.num_orders = self._io.read_u2le()
        self._debug['num_orders']['end'] = self._io.pos()
        self._debug['num_instruments']['start'] = self._io.pos()
        self.num_instruments = self._io.read_u2le()
        self._debug['num_instruments']['end'] = self._io.pos()
        self._debug['num_patterns']['start'] = self._io.pos()
        self.num_patterns = self._io.read_u2le()
        self._debug['num_patterns']['end'] = self._io.pos()
        self._debug['flags']['start'] = self._io.pos()
        self.flags = self._io.read_u2le()
        self._debug['flags']['end'] = self._io.pos()
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u2le()
        self._debug['version']['end'] = self._io.pos()
        self._debug['samples_format']['start'] = self._io.pos()
        self.samples_format = self._io.read_u2le()
        self._debug['samples_format']['end'] = self._io.pos()
        self._debug['magic2']['start'] = self._io.pos()
        self.magic2 = self._io.read_bytes(4)
        self._debug['magic2']['end'] = self._io.pos()
        if not self.magic2 == b"\x53\x43\x52\x4D":
            raise kaitaistruct.ValidationNotEqualError(b"\x53\x43\x52\x4D", self.magic2, self._io, u"/seq/10")
        self._debug['global_volume']['start'] = self._io.pos()
        self.global_volume = self._io.read_u1()
        self._debug['global_volume']['end'] = self._io.pos()
        self._debug['initial_speed']['start'] = self._io.pos()
        self.initial_speed = self._io.read_u1()
        self._debug['initial_speed']['end'] = self._io.pos()
        self._debug['initial_tempo']['start'] = self._io.pos()
        self.initial_tempo = self._io.read_u1()
        self._debug['initial_tempo']['end'] = self._io.pos()
        self._debug['is_stereo']['start'] = self._io.pos()
        self.is_stereo = self._io.read_bits_int_be(1) != 0
        self._debug['is_stereo']['end'] = self._io.pos()
        self._debug['master_volume']['start'] = self._io.pos()
        self.master_volume = self._io.read_bits_int_be(7)
        self._debug['master_volume']['end'] = self._io.pos()
        self._io.align_to_byte()
        self._debug['ultra_click_removal']['start'] = self._io.pos()
        self.ultra_click_removal = self._io.read_u1()
        self._debug['ultra_click_removal']['end'] = self._io.pos()
        self._debug['has_custom_pan']['start'] = self._io.pos()
        self.has_custom_pan = self._io.read_u1()
        self._debug['has_custom_pan']['end'] = self._io.pos()
        self._debug['reserved2']['start'] = self._io.pos()
        self.reserved2 = self._io.read_bytes(8)
        self._debug['reserved2']['end'] = self._io.pos()
        self._debug['ofs_special']['start'] = self._io.pos()
        self.ofs_special = self._io.read_u2le()
        self._debug['ofs_special']['end'] = self._io.pos()
        self._debug['channels']['start'] = self._io.pos()
        self.channels = [None] * (32)
        for i in range(32):
            if not 'arr' in self._debug['channels']:
                self._debug['channels']['arr'] = []
            self._debug['channels']['arr'].append({'start': self._io.pos()})
            _t_channels = S3m.Channel(self._io, self, self._root)
            _t_channels._read()
            self.channels[i] = _t_channels
            self._debug['channels']['arr'][i]['end'] = self._io.pos()

        self._debug['channels']['end'] = self._io.pos()
        self._debug['orders']['start'] = self._io.pos()
        self.orders = self._io.read_bytes(self.num_orders)
        self._debug['orders']['end'] = self._io.pos()
        self._debug['instruments']['start'] = self._io.pos()
        self.instruments = [None] * (self.num_instruments)
        for i in range(self.num_instruments):
            if not 'arr' in self._debug['instruments']:
                self._debug['instruments']['arr'] = []
            self._debug['instruments']['arr'].append({'start': self._io.pos()})
            _t_instruments = S3m.InstrumentPtr(self._io, self, self._root)
            _t_instruments._read()
            self.instruments[i] = _t_instruments
            self._debug['instruments']['arr'][i]['end'] = self._io.pos()

        self._debug['instruments']['end'] = self._io.pos()
        self._debug['patterns']['start'] = self._io.pos()
        self.patterns = [None] * (self.num_patterns)
        for i in range(self.num_patterns):
            if not 'arr' in self._debug['patterns']:
                self._debug['patterns']['arr'] = []
            self._debug['patterns']['arr'].append({'start': self._io.pos()})
            _t_patterns = S3m.PatternPtr(self._io, self, self._root)
            _t_patterns._read()
            self.patterns[i] = _t_patterns
            self._debug['patterns']['arr'][i]['end'] = self._io.pos()

        self._debug['patterns']['end'] = self._io.pos()
        if self.has_custom_pan == 252:
            self._debug['channel_pans']['start'] = self._io.pos()
            self.channel_pans = [None] * (32)
            for i in range(32):
                if not 'arr' in self._debug['channel_pans']:
                    self._debug['channel_pans']['arr'] = []
                self._debug['channel_pans']['arr'].append({'start': self._io.pos()})
                _t_channel_pans = S3m.ChannelPan(self._io, self, self._root)
                _t_channel_pans._read()
                self.channel_pans[i] = _t_channel_pans
                self._debug['channel_pans']['arr'][i]['end'] = self._io.pos()

            self._debug['channel_pans']['end'] = self._io.pos()


    class ChannelPan(KaitaiStruct):
        SEQ_FIELDS = ["reserved1", "has_custom_pan", "reserved2", "pan"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bits_int_be(2)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['has_custom_pan']['start'] = self._io.pos()
            self.has_custom_pan = self._io.read_bits_int_be(1) != 0
            self._debug['has_custom_pan']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bits_int_be(1) != 0
            self._debug['reserved2']['end'] = self._io.pos()
            self._debug['pan']['start'] = self._io.pos()
            self.pan = self._io.read_bits_int_be(4)
            self._debug['pan']['end'] = self._io.pos()


    class PatternCell(KaitaiStruct):
        SEQ_FIELDS = ["has_fx", "has_volume", "has_note_and_instrument", "channel_num", "note", "instrument", "volume", "fx_type", "fx_value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['has_fx']['start'] = self._io.pos()
            self.has_fx = self._io.read_bits_int_be(1) != 0
            self._debug['has_fx']['end'] = self._io.pos()
            self._debug['has_volume']['start'] = self._io.pos()
            self.has_volume = self._io.read_bits_int_be(1) != 0
            self._debug['has_volume']['end'] = self._io.pos()
            self._debug['has_note_and_instrument']['start'] = self._io.pos()
            self.has_note_and_instrument = self._io.read_bits_int_be(1) != 0
            self._debug['has_note_and_instrument']['end'] = self._io.pos()
            self._debug['channel_num']['start'] = self._io.pos()
            self.channel_num = self._io.read_bits_int_be(5)
            self._debug['channel_num']['end'] = self._io.pos()
            self._io.align_to_byte()
            if self.has_note_and_instrument:
                self._debug['note']['start'] = self._io.pos()
                self.note = self._io.read_u1()
                self._debug['note']['end'] = self._io.pos()

            if self.has_note_and_instrument:
                self._debug['instrument']['start'] = self._io.pos()
                self.instrument = self._io.read_u1()
                self._debug['instrument']['end'] = self._io.pos()

            if self.has_volume:
                self._debug['volume']['start'] = self._io.pos()
                self.volume = self._io.read_u1()
                self._debug['volume']['end'] = self._io.pos()

            if self.has_fx:
                self._debug['fx_type']['start'] = self._io.pos()
                self.fx_type = self._io.read_u1()
                self._debug['fx_type']['end'] = self._io.pos()

            if self.has_fx:
                self._debug['fx_value']['start'] = self._io.pos()
                self.fx_value = self._io.read_u1()
                self._debug['fx_value']['end'] = self._io.pos()



    class PatternCells(KaitaiStruct):
        SEQ_FIELDS = ["cells"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['cells']['start'] = self._io.pos()
            self.cells = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['cells']:
                    self._debug['cells']['arr'] = []
                self._debug['cells']['arr'].append({'start': self._io.pos()})
                _t_cells = S3m.PatternCell(self._io, self, self._root)
                _t_cells._read()
                self.cells.append(_t_cells)
                self._debug['cells']['arr'][len(self.cells) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['cells']['end'] = self._io.pos()


    class Channel(KaitaiStruct):
        SEQ_FIELDS = ["is_disabled", "ch_type"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['is_disabled']['start'] = self._io.pos()
            self.is_disabled = self._io.read_bits_int_be(1) != 0
            self._debug['is_disabled']['end'] = self._io.pos()
            self._debug['ch_type']['start'] = self._io.pos()
            self.ch_type = self._io.read_bits_int_be(7)
            self._debug['ch_type']['end'] = self._io.pos()


    class SwappedU3(KaitaiStruct):
        """Custom 3-byte integer, stored in mixed endian manner."""
        SEQ_FIELDS = ["hi", "lo"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['hi']['start'] = self._io.pos()
            self.hi = self._io.read_u1()
            self._debug['hi']['end'] = self._io.pos()
            self._debug['lo']['start'] = self._io.pos()
            self.lo = self._io.read_u2le()
            self._debug['lo']['end'] = self._io.pos()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = (self.lo | (self.hi << 16))
            return self._m_value if hasattr(self, '_m_value') else None


    class Pattern(KaitaiStruct):
        SEQ_FIELDS = ["size", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u2le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self._raw_body = self._io.read_bytes((self.size - 2))
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = S3m.PatternCells(_io__raw_body, self, self._root)
            self.body._read()
            self._debug['body']['end'] = self._io.pos()


    class PatternPtr(KaitaiStruct):
        SEQ_FIELDS = ["paraptr"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['paraptr']['start'] = self._io.pos()
            self.paraptr = self._io.read_u2le()
            self._debug['paraptr']['end'] = self._io.pos()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body if hasattr(self, '_m_body') else None

            _pos = self._io.pos()
            self._io.seek((self.paraptr * 16))
            self._debug['_m_body']['start'] = self._io.pos()
            self._m_body = S3m.Pattern(self._io, self, self._root)
            self._m_body._read()
            self._debug['_m_body']['end'] = self._io.pos()
            self._io.seek(_pos)
            return self._m_body if hasattr(self, '_m_body') else None


    class InstrumentPtr(KaitaiStruct):
        SEQ_FIELDS = ["paraptr"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['paraptr']['start'] = self._io.pos()
            self.paraptr = self._io.read_u2le()
            self._debug['paraptr']['end'] = self._io.pos()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body if hasattr(self, '_m_body') else None

            _pos = self._io.pos()
            self._io.seek((self.paraptr * 16))
            self._debug['_m_body']['start'] = self._io.pos()
            self._m_body = S3m.Instrument(self._io, self, self._root)
            self._m_body._read()
            self._debug['_m_body']['end'] = self._io.pos()
            self._io.seek(_pos)
            return self._m_body if hasattr(self, '_m_body') else None


    class Instrument(KaitaiStruct):

        class InstTypes(Enum):
            sample = 1
            melodic = 2
            bass_drum = 3
            snare_drum = 4
            tom = 5
            cymbal = 6
            hihat = 7
        SEQ_FIELDS = ["type", "filename", "body", "tuning_hz", "reserved2", "sample_name", "magic"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(S3m.Instrument.InstTypes, self._io.read_u1())
            self._debug['type']['end'] = self._io.pos()
            self._debug['filename']['start'] = self._io.pos()
            self.filename = KaitaiStream.bytes_terminate(self._io.read_bytes(12), 0, False)
            self._debug['filename']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.type
            if _on == S3m.Instrument.InstTypes.sample:
                self.body = S3m.Instrument.Sampled(self._io, self, self._root)
                self.body._read()
            else:
                self.body = S3m.Instrument.Adlib(self._io, self, self._root)
                self.body._read()
            self._debug['body']['end'] = self._io.pos()
            self._debug['tuning_hz']['start'] = self._io.pos()
            self.tuning_hz = self._io.read_u4le()
            self._debug['tuning_hz']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(12)
            self._debug['reserved2']['end'] = self._io.pos()
            self._debug['sample_name']['start'] = self._io.pos()
            self.sample_name = KaitaiStream.bytes_terminate(self._io.read_bytes(28), 0, False)
            self._debug['sample_name']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x53\x43\x52\x53":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x43\x52\x53", self.magic, self._io, u"/types/instrument/seq/6")

        class Sampled(KaitaiStruct):
            SEQ_FIELDS = ["paraptr_sample", "len_sample", "loop_begin", "loop_end", "default_volume", "reserved1", "is_packed", "flags"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['paraptr_sample']['start'] = self._io.pos()
                self.paraptr_sample = S3m.SwappedU3(self._io, self, self._root)
                self.paraptr_sample._read()
                self._debug['paraptr_sample']['end'] = self._io.pos()
                self._debug['len_sample']['start'] = self._io.pos()
                self.len_sample = self._io.read_u4le()
                self._debug['len_sample']['end'] = self._io.pos()
                self._debug['loop_begin']['start'] = self._io.pos()
                self.loop_begin = self._io.read_u4le()
                self._debug['loop_begin']['end'] = self._io.pos()
                self._debug['loop_end']['start'] = self._io.pos()
                self.loop_end = self._io.read_u4le()
                self._debug['loop_end']['end'] = self._io.pos()
                self._debug['default_volume']['start'] = self._io.pos()
                self.default_volume = self._io.read_u1()
                self._debug['default_volume']['end'] = self._io.pos()
                self._debug['reserved1']['start'] = self._io.pos()
                self.reserved1 = self._io.read_u1()
                self._debug['reserved1']['end'] = self._io.pos()
                self._debug['is_packed']['start'] = self._io.pos()
                self.is_packed = self._io.read_u1()
                self._debug['is_packed']['end'] = self._io.pos()
                self._debug['flags']['start'] = self._io.pos()
                self.flags = self._io.read_u1()
                self._debug['flags']['end'] = self._io.pos()

            @property
            def sample(self):
                if hasattr(self, '_m_sample'):
                    return self._m_sample if hasattr(self, '_m_sample') else None

                _pos = self._io.pos()
                self._io.seek((self.paraptr_sample.value * 16))
                self._debug['_m_sample']['start'] = self._io.pos()
                self._m_sample = self._io.read_bytes(self.len_sample)
                self._debug['_m_sample']['end'] = self._io.pos()
                self._io.seek(_pos)
                return self._m_sample if hasattr(self, '_m_sample') else None


        class Adlib(KaitaiStruct):
            SEQ_FIELDS = ["reserved1", "_unnamed1"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['reserved1']['start'] = self._io.pos()
                self.reserved1 = self._io.read_bytes(3)
                self._debug['reserved1']['end'] = self._io.pos()
                if not self.reserved1 == b"\x00\x00\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00", self.reserved1, self._io, u"/types/instrument/types/adlib/seq/0")
                self._debug['_unnamed1']['start'] = self._io.pos()
                self._unnamed1 = self._io.read_bytes(16)
                self._debug['_unnamed1']['end'] = self._io.pos()




