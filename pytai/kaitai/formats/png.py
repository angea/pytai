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
import zlib


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Png(KaitaiStruct):
    """Test files for APNG can be found at the following locations:
    
      * <https://philip.html5.org/tests/apng/tests.html>
      * <http://littlesvr.ca/apng/>
    """

    class PhysUnit(Enum):
        unknown = 0
        meter = 1

    class BlendOpValues(Enum):
        source = 0
        over = 1

    class CompressionMethods(Enum):
        zlib = 0

    class DisposeOpValues(Enum):
        none = 0
        background = 1
        previous = 2

    class ColorType(Enum):
        greyscale = 0
        truecolor = 2
        indexed = 3
        greyscale_alpha = 4
        truecolor_alpha = 6
    SEQ_FIELDS = ["magic", "ihdr_len", "ihdr_type", "ihdr", "ihdr_crc", "chunks"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(8)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A":
            raise kaitaistruct.ValidationNotEqualError(b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A", self.magic, self._io, u"/seq/0")
        self._debug['ihdr_len']['start'] = self._io.pos()
        self.ihdr_len = self._io.read_u4be()
        self._debug['ihdr_len']['end'] = self._io.pos()
        if not self.ihdr_len == 13:
            raise kaitaistruct.ValidationNotEqualError(13, self.ihdr_len, self._io, u"/seq/1")
        self._debug['ihdr_type']['start'] = self._io.pos()
        self.ihdr_type = self._io.read_bytes(4)
        self._debug['ihdr_type']['end'] = self._io.pos()
        if not self.ihdr_type == b"\x49\x48\x44\x52":
            raise kaitaistruct.ValidationNotEqualError(b"\x49\x48\x44\x52", self.ihdr_type, self._io, u"/seq/2")
        self._debug['ihdr']['start'] = self._io.pos()
        self.ihdr = Png.IhdrChunk(self._io, self, self._root)
        self.ihdr._read()
        self._debug['ihdr']['end'] = self._io.pos()
        self._debug['ihdr_crc']['start'] = self._io.pos()
        self.ihdr_crc = self._io.read_bytes(4)
        self._debug['ihdr_crc']['end'] = self._io.pos()
        self._debug['chunks']['start'] = self._io.pos()
        self.chunks = []
        i = 0
        while True:
            if not 'arr' in self._debug['chunks']:
                self._debug['chunks']['arr'] = []
            self._debug['chunks']['arr'].append({'start': self._io.pos()})
            _t_chunks = Png.Chunk(self._io, self, self._root)
            _t_chunks._read()
            _ = _t_chunks
            self.chunks.append(_)
            self._debug['chunks']['arr'][len(self.chunks) - 1]['end'] = self._io.pos()
            if  ((_.type == u"IEND") or (self._io.is_eof())) :
                break
            i += 1
        self._debug['chunks']['end'] = self._io.pos()

    class Rgb(KaitaiStruct):
        SEQ_FIELDS = ["r", "g", "b"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['r']['start'] = self._io.pos()
            self.r = self._io.read_u1()
            self._debug['r']['end'] = self._io.pos()
            self._debug['g']['start'] = self._io.pos()
            self.g = self._io.read_u1()
            self._debug['g']['end'] = self._io.pos()
            self._debug['b']['start'] = self._io.pos()
            self.b = self._io.read_u1()
            self._debug['b']['end'] = self._io.pos()


    class Chunk(KaitaiStruct):
        SEQ_FIELDS = ["len", "type", "body", "crc"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4be()
            self._debug['len']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = (self._io.read_bytes(4)).decode(u"UTF-8")
            self._debug['type']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.type
            if _on == u"iTXt":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.InternationalTextChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"gAMA":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.GamaChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"tIME":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.TimeChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"PLTE":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.PlteChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"bKGD":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.BkgdChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"pHYs":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.PhysChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"fdAT":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.FrameDataChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"tEXt":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.TextChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"cHRM":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.ChrmChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"acTL":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.AnimationControlChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"sRGB":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.SrgbChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"zTXt":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.CompressedTextChunk(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"fcTL":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.FrameControlChunk(_io__raw_body, self, self._root)
                self.body._read()
            else:
                self.body = self._io.read_bytes(self.len)
            self._debug['body']['end'] = self._io.pos()
            self._debug['crc']['start'] = self._io.pos()
            self.crc = self._io.read_bytes(4)
            self._debug['crc']['end'] = self._io.pos()


    class BkgdIndexed(KaitaiStruct):
        """Background chunk for images with indexed palette."""
        SEQ_FIELDS = ["palette_index"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['palette_index']['start'] = self._io.pos()
            self.palette_index = self._io.read_u1()
            self._debug['palette_index']['end'] = self._io.pos()


    class Point(KaitaiStruct):
        SEQ_FIELDS = ["x_int", "y_int"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x_int']['start'] = self._io.pos()
            self.x_int = self._io.read_u4be()
            self._debug['x_int']['end'] = self._io.pos()
            self._debug['y_int']['start'] = self._io.pos()
            self.y_int = self._io.read_u4be()
            self._debug['y_int']['end'] = self._io.pos()

        @property
        def x(self):
            if hasattr(self, '_m_x'):
                return self._m_x if hasattr(self, '_m_x') else None

            self._m_x = (self.x_int / 100000.0)
            return self._m_x if hasattr(self, '_m_x') else None

        @property
        def y(self):
            if hasattr(self, '_m_y'):
                return self._m_y if hasattr(self, '_m_y') else None

            self._m_y = (self.y_int / 100000.0)
            return self._m_y if hasattr(self, '_m_y') else None


    class BkgdGreyscale(KaitaiStruct):
        """Background chunk for greyscale images."""
        SEQ_FIELDS = ["value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_u2be()
            self._debug['value']['end'] = self._io.pos()


    class ChrmChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11cHRM
        """
        SEQ_FIELDS = ["white_point", "red", "green", "blue"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['white_point']['start'] = self._io.pos()
            self.white_point = Png.Point(self._io, self, self._root)
            self.white_point._read()
            self._debug['white_point']['end'] = self._io.pos()
            self._debug['red']['start'] = self._io.pos()
            self.red = Png.Point(self._io, self, self._root)
            self.red._read()
            self._debug['red']['end'] = self._io.pos()
            self._debug['green']['start'] = self._io.pos()
            self.green = Png.Point(self._io, self, self._root)
            self.green._read()
            self._debug['green']['end'] = self._io.pos()
            self._debug['blue']['start'] = self._io.pos()
            self.blue = Png.Point(self._io, self, self._root)
            self.blue._read()
            self._debug['blue']['end'] = self._io.pos()


    class IhdrChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11IHDR
        """
        SEQ_FIELDS = ["width", "height", "bit_depth", "color_type", "compression_method", "filter_method", "interlace_method"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4be()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4be()
            self._debug['height']['end'] = self._io.pos()
            self._debug['bit_depth']['start'] = self._io.pos()
            self.bit_depth = self._io.read_u1()
            self._debug['bit_depth']['end'] = self._io.pos()
            self._debug['color_type']['start'] = self._io.pos()
            self.color_type = KaitaiStream.resolve_enum(Png.ColorType, self._io.read_u1())
            self._debug['color_type']['end'] = self._io.pos()
            self._debug['compression_method']['start'] = self._io.pos()
            self.compression_method = self._io.read_u1()
            self._debug['compression_method']['end'] = self._io.pos()
            self._debug['filter_method']['start'] = self._io.pos()
            self.filter_method = self._io.read_u1()
            self._debug['filter_method']['end'] = self._io.pos()
            self._debug['interlace_method']['start'] = self._io.pos()
            self.interlace_method = self._io.read_u1()
            self._debug['interlace_method']['end'] = self._io.pos()


    class PlteChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11PLTE
        """
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self.entries = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['entries']:
                    self._debug['entries']['arr'] = []
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                _t_entries = Png.Rgb(self._io, self, self._root)
                _t_entries._read()
                self.entries.append(_t_entries)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class SrgbChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11sRGB
        """

        class Intent(Enum):
            perceptual = 0
            relative_colorimetric = 1
            saturation = 2
            absolute_colorimetric = 3
        SEQ_FIELDS = ["render_intent"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['render_intent']['start'] = self._io.pos()
            self.render_intent = KaitaiStream.resolve_enum(Png.SrgbChunk.Intent, self._io.read_u1())
            self._debug['render_intent']['end'] = self._io.pos()


    class CompressedTextChunk(KaitaiStruct):
        """Compressed text chunk effectively allows to store key-value
        string pairs in PNG container, compressing "value" part (which
        can be quite lengthy) with zlib compression.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11zTXt
        """
        SEQ_FIELDS = ["keyword", "compression_method", "text_datastream"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['keyword']['start'] = self._io.pos()
            self.keyword = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['keyword']['end'] = self._io.pos()
            self._debug['compression_method']['start'] = self._io.pos()
            self.compression_method = KaitaiStream.resolve_enum(Png.CompressionMethods, self._io.read_u1())
            self._debug['compression_method']['end'] = self._io.pos()
            self._debug['text_datastream']['start'] = self._io.pos()
            self._raw_text_datastream = self._io.read_bytes_full()
            self.text_datastream = zlib.decompress(self._raw_text_datastream)
            self._debug['text_datastream']['end'] = self._io.pos()


    class FrameDataChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.mozilla.org/APNG_Specification#.60fdAT.60:_The_Frame_Data_Chunk
        """
        SEQ_FIELDS = ["sequence_number", "frame_data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['sequence_number']['start'] = self._io.pos()
            self.sequence_number = self._io.read_u4be()
            self._debug['sequence_number']['end'] = self._io.pos()
            self._debug['frame_data']['start'] = self._io.pos()
            self.frame_data = self._io.read_bytes_full()
            self._debug['frame_data']['end'] = self._io.pos()


    class BkgdTruecolor(KaitaiStruct):
        """Background chunk for truecolor images."""
        SEQ_FIELDS = ["red", "green", "blue"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['red']['start'] = self._io.pos()
            self.red = self._io.read_u2be()
            self._debug['red']['end'] = self._io.pos()
            self._debug['green']['start'] = self._io.pos()
            self.green = self._io.read_u2be()
            self._debug['green']['end'] = self._io.pos()
            self._debug['blue']['start'] = self._io.pos()
            self.blue = self._io.read_u2be()
            self._debug['blue']['end'] = self._io.pos()


    class GamaChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11gAMA
        """
        SEQ_FIELDS = ["gamma_int"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['gamma_int']['start'] = self._io.pos()
            self.gamma_int = self._io.read_u4be()
            self._debug['gamma_int']['end'] = self._io.pos()

        @property
        def gamma_ratio(self):
            if hasattr(self, '_m_gamma_ratio'):
                return self._m_gamma_ratio if hasattr(self, '_m_gamma_ratio') else None

            self._m_gamma_ratio = (100000.0 / self.gamma_int)
            return self._m_gamma_ratio if hasattr(self, '_m_gamma_ratio') else None


    class BkgdChunk(KaitaiStruct):
        """Background chunk stores default background color to display this
        image against. Contents depend on `color_type` of the image.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11bKGD
        """
        SEQ_FIELDS = ["bkgd"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bkgd']['start'] = self._io.pos()
            _on = self._root.ihdr.color_type
            if _on == Png.ColorType.indexed:
                self.bkgd = Png.BkgdIndexed(self._io, self, self._root)
                self.bkgd._read()
            elif _on == Png.ColorType.truecolor_alpha:
                self.bkgd = Png.BkgdTruecolor(self._io, self, self._root)
                self.bkgd._read()
            elif _on == Png.ColorType.greyscale_alpha:
                self.bkgd = Png.BkgdGreyscale(self._io, self, self._root)
                self.bkgd._read()
            elif _on == Png.ColorType.truecolor:
                self.bkgd = Png.BkgdTruecolor(self._io, self, self._root)
                self.bkgd._read()
            elif _on == Png.ColorType.greyscale:
                self.bkgd = Png.BkgdGreyscale(self._io, self, self._root)
                self.bkgd._read()
            self._debug['bkgd']['end'] = self._io.pos()


    class PhysChunk(KaitaiStruct):
        """"Physical size" chunk stores data that allows to translate
        logical pixels into physical units (meters, etc) and vice-versa.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11pHYs
        """
        SEQ_FIELDS = ["pixels_per_unit_x", "pixels_per_unit_y", "unit"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['pixels_per_unit_x']['start'] = self._io.pos()
            self.pixels_per_unit_x = self._io.read_u4be()
            self._debug['pixels_per_unit_x']['end'] = self._io.pos()
            self._debug['pixels_per_unit_y']['start'] = self._io.pos()
            self.pixels_per_unit_y = self._io.read_u4be()
            self._debug['pixels_per_unit_y']['end'] = self._io.pos()
            self._debug['unit']['start'] = self._io.pos()
            self.unit = KaitaiStream.resolve_enum(Png.PhysUnit, self._io.read_u1())
            self._debug['unit']['end'] = self._io.pos()


    class FrameControlChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.mozilla.org/APNG_Specification#.60fcTL.60:_The_Frame_Control_Chunk
        """
        SEQ_FIELDS = ["sequence_number", "width", "height", "x_offset", "y_offset", "delay_num", "delay_den", "dispose_op", "blend_op"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['sequence_number']['start'] = self._io.pos()
            self.sequence_number = self._io.read_u4be()
            self._debug['sequence_number']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4be()
            self._debug['width']['end'] = self._io.pos()
            if not self.width >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.width, self._io, u"/types/frame_control_chunk/seq/1")
            if not self.width <= self._root.ihdr.width:
                raise kaitaistruct.ValidationGreaterThanError(self._root.ihdr.width, self.width, self._io, u"/types/frame_control_chunk/seq/1")
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4be()
            self._debug['height']['end'] = self._io.pos()
            if not self.height >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.height, self._io, u"/types/frame_control_chunk/seq/2")
            if not self.height <= self._root.ihdr.height:
                raise kaitaistruct.ValidationGreaterThanError(self._root.ihdr.height, self.height, self._io, u"/types/frame_control_chunk/seq/2")
            self._debug['x_offset']['start'] = self._io.pos()
            self.x_offset = self._io.read_u4be()
            self._debug['x_offset']['end'] = self._io.pos()
            if not self.x_offset <= (self._root.ihdr.width - self.width):
                raise kaitaistruct.ValidationGreaterThanError((self._root.ihdr.width - self.width), self.x_offset, self._io, u"/types/frame_control_chunk/seq/3")
            self._debug['y_offset']['start'] = self._io.pos()
            self.y_offset = self._io.read_u4be()
            self._debug['y_offset']['end'] = self._io.pos()
            if not self.y_offset <= (self._root.ihdr.height - self.height):
                raise kaitaistruct.ValidationGreaterThanError((self._root.ihdr.height - self.height), self.y_offset, self._io, u"/types/frame_control_chunk/seq/4")
            self._debug['delay_num']['start'] = self._io.pos()
            self.delay_num = self._io.read_u2be()
            self._debug['delay_num']['end'] = self._io.pos()
            self._debug['delay_den']['start'] = self._io.pos()
            self.delay_den = self._io.read_u2be()
            self._debug['delay_den']['end'] = self._io.pos()
            self._debug['dispose_op']['start'] = self._io.pos()
            self.dispose_op = KaitaiStream.resolve_enum(Png.DisposeOpValues, self._io.read_u1())
            self._debug['dispose_op']['end'] = self._io.pos()
            self._debug['blend_op']['start'] = self._io.pos()
            self.blend_op = KaitaiStream.resolve_enum(Png.BlendOpValues, self._io.read_u1())
            self._debug['blend_op']['end'] = self._io.pos()

        @property
        def delay(self):
            """Time to display this frame, in seconds."""
            if hasattr(self, '_m_delay'):
                return self._m_delay if hasattr(self, '_m_delay') else None

            self._m_delay = (self.delay_num / (100.0 if self.delay_den == 0 else self.delay_den))
            return self._m_delay if hasattr(self, '_m_delay') else None


    class InternationalTextChunk(KaitaiStruct):
        """International text chunk effectively allows to store key-value string pairs in
        PNG container. Both "key" (keyword) and "value" (text) parts are
        given in pre-defined subset of iso8859-1 without control
        characters.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11iTXt
        """
        SEQ_FIELDS = ["keyword", "compression_flag", "compression_method", "language_tag", "translated_keyword", "text"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['keyword']['start'] = self._io.pos()
            self.keyword = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['keyword']['end'] = self._io.pos()
            self._debug['compression_flag']['start'] = self._io.pos()
            self.compression_flag = self._io.read_u1()
            self._debug['compression_flag']['end'] = self._io.pos()
            self._debug['compression_method']['start'] = self._io.pos()
            self.compression_method = KaitaiStream.resolve_enum(Png.CompressionMethods, self._io.read_u1())
            self._debug['compression_method']['end'] = self._io.pos()
            self._debug['language_tag']['start'] = self._io.pos()
            self.language_tag = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['language_tag']['end'] = self._io.pos()
            self._debug['translated_keyword']['start'] = self._io.pos()
            self.translated_keyword = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['translated_keyword']['end'] = self._io.pos()
            self._debug['text']['start'] = self._io.pos()
            self.text = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._debug['text']['end'] = self._io.pos()


    class TextChunk(KaitaiStruct):
        """Text chunk effectively allows to store key-value string pairs in
        PNG container. Both "key" (keyword) and "value" (text) parts are
        given in pre-defined subset of iso8859-1 without control
        characters.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11tEXt
        """
        SEQ_FIELDS = ["keyword", "text"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['keyword']['start'] = self._io.pos()
            self.keyword = (self._io.read_bytes_term(0, False, True, True)).decode(u"iso8859-1")
            self._debug['keyword']['end'] = self._io.pos()
            self._debug['text']['start'] = self._io.pos()
            self.text = (self._io.read_bytes_full()).decode(u"iso8859-1")
            self._debug['text']['end'] = self._io.pos()


    class AnimationControlChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.mozilla.org/APNG_Specification#.60acTL.60:_The_Animation_Control_Chunk
        """
        SEQ_FIELDS = ["num_frames", "num_plays"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_frames']['start'] = self._io.pos()
            self.num_frames = self._io.read_u4be()
            self._debug['num_frames']['end'] = self._io.pos()
            self._debug['num_plays']['start'] = self._io.pos()
            self.num_plays = self._io.read_u4be()
            self._debug['num_plays']['end'] = self._io.pos()


    class TimeChunk(KaitaiStruct):
        """Time chunk stores time stamp of last modification of this image,
        up to 1 second precision in UTC timezone.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11tIME
        """
        SEQ_FIELDS = ["year", "month", "day", "hour", "minute", "second"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['year']['start'] = self._io.pos()
            self.year = self._io.read_u2be()
            self._debug['year']['end'] = self._io.pos()
            self._debug['month']['start'] = self._io.pos()
            self.month = self._io.read_u1()
            self._debug['month']['end'] = self._io.pos()
            self._debug['day']['start'] = self._io.pos()
            self.day = self._io.read_u1()
            self._debug['day']['end'] = self._io.pos()
            self._debug['hour']['start'] = self._io.pos()
            self.hour = self._io.read_u1()
            self._debug['hour']['end'] = self._io.pos()
            self._debug['minute']['start'] = self._io.pos()
            self.minute = self._io.read_u1()
            self._debug['minute']['end'] = self._io.pos()
            self._debug['second']['start'] = self._io.pos()
            self.second = self._io.read_u1()
            self._debug['second']['end'] = self._io.pos()



