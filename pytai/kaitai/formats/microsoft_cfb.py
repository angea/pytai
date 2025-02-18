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

class MicrosoftCfb(KaitaiStruct):
    SEQ_FIELDS = ["header"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = MicrosoftCfb.CfbHeader(self._io, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()

    class CfbHeader(KaitaiStruct):
        SEQ_FIELDS = ["signature", "clsid", "version_minor", "version_major", "byte_order", "sector_shift", "mini_sector_shift", "reserved1", "size_dir", "size_fat", "ofs_dir", "transaction_seq", "mini_stream_cutoff_size", "ofs_mini_fat", "size_mini_fat", "ofs_difat", "size_difat", "difat"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(8)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1":
                raise kaitaistruct.ValidationNotEqualError(b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1", self.signature, self._io, u"/types/cfb_header/seq/0")
            self._debug['clsid']['start'] = self._io.pos()
            self.clsid = self._io.read_bytes(16)
            self._debug['clsid']['end'] = self._io.pos()
            if not self.clsid == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.clsid, self._io, u"/types/cfb_header/seq/1")
            self._debug['version_minor']['start'] = self._io.pos()
            self.version_minor = self._io.read_u2le()
            self._debug['version_minor']['end'] = self._io.pos()
            self._debug['version_major']['start'] = self._io.pos()
            self.version_major = self._io.read_u2le()
            self._debug['version_major']['end'] = self._io.pos()
            self._debug['byte_order']['start'] = self._io.pos()
            self.byte_order = self._io.read_bytes(2)
            self._debug['byte_order']['end'] = self._io.pos()
            if not self.byte_order == b"\xFE\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFE\xFF", self.byte_order, self._io, u"/types/cfb_header/seq/4")
            self._debug['sector_shift']['start'] = self._io.pos()
            self.sector_shift = self._io.read_u2le()
            self._debug['sector_shift']['end'] = self._io.pos()
            self._debug['mini_sector_shift']['start'] = self._io.pos()
            self.mini_sector_shift = self._io.read_u2le()
            self._debug['mini_sector_shift']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bytes(6)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['size_dir']['start'] = self._io.pos()
            self.size_dir = self._io.read_s4le()
            self._debug['size_dir']['end'] = self._io.pos()
            self._debug['size_fat']['start'] = self._io.pos()
            self.size_fat = self._io.read_s4le()
            self._debug['size_fat']['end'] = self._io.pos()
            self._debug['ofs_dir']['start'] = self._io.pos()
            self.ofs_dir = self._io.read_s4le()
            self._debug['ofs_dir']['end'] = self._io.pos()
            self._debug['transaction_seq']['start'] = self._io.pos()
            self.transaction_seq = self._io.read_s4le()
            self._debug['transaction_seq']['end'] = self._io.pos()
            self._debug['mini_stream_cutoff_size']['start'] = self._io.pos()
            self.mini_stream_cutoff_size = self._io.read_s4le()
            self._debug['mini_stream_cutoff_size']['end'] = self._io.pos()
            self._debug['ofs_mini_fat']['start'] = self._io.pos()
            self.ofs_mini_fat = self._io.read_s4le()
            self._debug['ofs_mini_fat']['end'] = self._io.pos()
            self._debug['size_mini_fat']['start'] = self._io.pos()
            self.size_mini_fat = self._io.read_s4le()
            self._debug['size_mini_fat']['end'] = self._io.pos()
            self._debug['ofs_difat']['start'] = self._io.pos()
            self.ofs_difat = self._io.read_s4le()
            self._debug['ofs_difat']['end'] = self._io.pos()
            self._debug['size_difat']['start'] = self._io.pos()
            self.size_difat = self._io.read_s4le()
            self._debug['size_difat']['end'] = self._io.pos()
            self._debug['difat']['start'] = self._io.pos()
            self.difat = [None] * (109)
            for i in range(109):
                if not 'arr' in self._debug['difat']:
                    self._debug['difat']['arr'] = []
                self._debug['difat']['arr'].append({'start': self._io.pos()})
                self.difat[i] = self._io.read_s4le()
                self._debug['difat']['arr'][i]['end'] = self._io.pos()

            self._debug['difat']['end'] = self._io.pos()


    class FatEntries(KaitaiStruct):
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
                self.entries.append(self._io.read_s4le())
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


    class DirEntry(KaitaiStruct):

        class ObjType(Enum):
            unknown = 0
            storage = 1
            stream = 2
            root_storage = 5

        class RbColor(Enum):
            red = 0
            black = 1
        SEQ_FIELDS = ["name", "name_len", "object_type", "color_flag", "left_sibling_id", "right_sibling_id", "child_id", "clsid", "state", "time_create", "time_mod", "ofs", "size"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(64)).decode(u"UTF-16LE")
            self._debug['name']['end'] = self._io.pos()
            self._debug['name_len']['start'] = self._io.pos()
            self.name_len = self._io.read_u2le()
            self._debug['name_len']['end'] = self._io.pos()
            self._debug['object_type']['start'] = self._io.pos()
            self.object_type = KaitaiStream.resolve_enum(MicrosoftCfb.DirEntry.ObjType, self._io.read_u1())
            self._debug['object_type']['end'] = self._io.pos()
            self._debug['color_flag']['start'] = self._io.pos()
            self.color_flag = KaitaiStream.resolve_enum(MicrosoftCfb.DirEntry.RbColor, self._io.read_u1())
            self._debug['color_flag']['end'] = self._io.pos()
            self._debug['left_sibling_id']['start'] = self._io.pos()
            self.left_sibling_id = self._io.read_s4le()
            self._debug['left_sibling_id']['end'] = self._io.pos()
            self._debug['right_sibling_id']['start'] = self._io.pos()
            self.right_sibling_id = self._io.read_s4le()
            self._debug['right_sibling_id']['end'] = self._io.pos()
            self._debug['child_id']['start'] = self._io.pos()
            self.child_id = self._io.read_s4le()
            self._debug['child_id']['end'] = self._io.pos()
            self._debug['clsid']['start'] = self._io.pos()
            self.clsid = self._io.read_bytes(16)
            self._debug['clsid']['end'] = self._io.pos()
            self._debug['state']['start'] = self._io.pos()
            self.state = self._io.read_u4le()
            self._debug['state']['end'] = self._io.pos()
            self._debug['time_create']['start'] = self._io.pos()
            self.time_create = self._io.read_u8le()
            self._debug['time_create']['end'] = self._io.pos()
            self._debug['time_mod']['start'] = self._io.pos()
            self.time_mod = self._io.read_u8le()
            self._debug['time_mod']['end'] = self._io.pos()
            self._debug['ofs']['start'] = self._io.pos()
            self.ofs = self._io.read_s4le()
            self._debug['ofs']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u8le()
            self._debug['size']['end'] = self._io.pos()

        @property
        def mini_stream(self):
            if hasattr(self, '_m_mini_stream'):
                return self._m_mini_stream if hasattr(self, '_m_mini_stream') else None

            if self.object_type == MicrosoftCfb.DirEntry.ObjType.root_storage:
                io = self._root._io
                _pos = io.pos()
                io.seek(((self.ofs + 1) * self._root.sector_size))
                self._debug['_m_mini_stream']['start'] = io.pos()
                self._m_mini_stream = io.read_bytes(self.size)
                self._debug['_m_mini_stream']['end'] = io.pos()
                io.seek(_pos)

            return self._m_mini_stream if hasattr(self, '_m_mini_stream') else None

        @property
        def child(self):
            if hasattr(self, '_m_child'):
                return self._m_child if hasattr(self, '_m_child') else None

            if self.child_id != -1:
                io = self._root._io
                _pos = io.pos()
                io.seek((((self._root.header.ofs_dir + 1) * self._root.sector_size) + (self.child_id * 128)))
                self._debug['_m_child']['start'] = io.pos()
                self._m_child = MicrosoftCfb.DirEntry(io, self, self._root)
                self._m_child._read()
                self._debug['_m_child']['end'] = io.pos()
                io.seek(_pos)

            return self._m_child if hasattr(self, '_m_child') else None

        @property
        def left_sibling(self):
            if hasattr(self, '_m_left_sibling'):
                return self._m_left_sibling if hasattr(self, '_m_left_sibling') else None

            if self.left_sibling_id != -1:
                io = self._root._io
                _pos = io.pos()
                io.seek((((self._root.header.ofs_dir + 1) * self._root.sector_size) + (self.left_sibling_id * 128)))
                self._debug['_m_left_sibling']['start'] = io.pos()
                self._m_left_sibling = MicrosoftCfb.DirEntry(io, self, self._root)
                self._m_left_sibling._read()
                self._debug['_m_left_sibling']['end'] = io.pos()
                io.seek(_pos)

            return self._m_left_sibling if hasattr(self, '_m_left_sibling') else None

        @property
        def right_sibling(self):
            if hasattr(self, '_m_right_sibling'):
                return self._m_right_sibling if hasattr(self, '_m_right_sibling') else None

            if self.right_sibling_id != -1:
                io = self._root._io
                _pos = io.pos()
                io.seek((((self._root.header.ofs_dir + 1) * self._root.sector_size) + (self.right_sibling_id * 128)))
                self._debug['_m_right_sibling']['start'] = io.pos()
                self._m_right_sibling = MicrosoftCfb.DirEntry(io, self, self._root)
                self._m_right_sibling._read()
                self._debug['_m_right_sibling']['end'] = io.pos()
                io.seek(_pos)

            return self._m_right_sibling if hasattr(self, '_m_right_sibling') else None


    @property
    def sector_size(self):
        if hasattr(self, '_m_sector_size'):
            return self._m_sector_size if hasattr(self, '_m_sector_size') else None

        self._m_sector_size = (1 << self.header.sector_shift)
        return self._m_sector_size if hasattr(self, '_m_sector_size') else None

    @property
    def fat(self):
        if hasattr(self, '_m_fat'):
            return self._m_fat if hasattr(self, '_m_fat') else None

        _pos = self._io.pos()
        self._io.seek(self.sector_size)
        self._debug['_m_fat']['start'] = self._io.pos()
        self._raw__m_fat = self._io.read_bytes((self.header.size_fat * self.sector_size))
        _io__raw__m_fat = KaitaiStream(BytesIO(self._raw__m_fat))
        self._m_fat = MicrosoftCfb.FatEntries(_io__raw__m_fat, self, self._root)
        self._m_fat._read()
        self._debug['_m_fat']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_fat if hasattr(self, '_m_fat') else None

    @property
    def dir(self):
        if hasattr(self, '_m_dir'):
            return self._m_dir if hasattr(self, '_m_dir') else None

        _pos = self._io.pos()
        self._io.seek(((self.header.ofs_dir + 1) * self.sector_size))
        self._debug['_m_dir']['start'] = self._io.pos()
        self._m_dir = MicrosoftCfb.DirEntry(self._io, self, self._root)
        self._m_dir._read()
        self._debug['_m_dir']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_dir if hasattr(self, '_m_dir') else None


