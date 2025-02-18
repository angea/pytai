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

class BtrfsStream(KaitaiStruct):
    """Btrfs is a copy on write file system based on B-trees focusing on fault tolerance, repair and easy
    administration. Btrfs is intended to address the lack of pooling, snapshots, checksums, and
    integral multi-device spanning in Linux file systems.
    Given any pair of subvolumes (or snapshots), Btrfs can generate a binary diff between them by
    using the `btrfs send` command that can be replayed later by using `btrfs receive`, possibly on a
    different Btrfs file system. The `btrfs send` command creates a set of data modifications required
    for converting one subvolume into another.
    This spec can be used to disassemble the binary diff created by the `btrfs send` command.
    If you want a text representation you may want to checkout `btrfs receive --dump` instead.
    
    .. seealso::
       Source - https://btrfs.wiki.kernel.org/index.php/Design_notes_on_Send/Receive
    """

    class Command(Enum):
        unspec = 0
        subvol = 1
        snapshot = 2
        mkfile = 3
        mkdir = 4
        mknod = 5
        mkfifo = 6
        mksock = 7
        symlink = 8
        rename = 9
        link = 10
        unlink = 11
        rmdir = 12
        set_xattr = 13
        remove_xattr = 14
        write = 15
        clone = 16
        truncate = 17
        chmod = 18
        chown = 19
        utimes = 20
        end = 21
        update_extent = 22

    class Attribute(Enum):
        unspec = 0
        uuid = 1
        ctransid = 2
        ino = 3
        size = 4
        mode = 5
        uid = 6
        gid = 7
        rdev = 8
        ctime = 9
        mtime = 10
        atime = 11
        otime = 12
        xattr_name = 13
        xattr_data = 14
        path = 15
        path_to = 16
        path_link = 17
        file_offset = 18
        data = 19
        clone_uuid = 20
        clone_ctransid = 21
        clone_path = 22
        clone_offset = 23
        clone_len = 24
    SEQ_FIELDS = ["header", "commands"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = BtrfsStream.SendStreamHeader(self._io, self, self._root)
        self.header._read()
        self._debug['header']['end'] = self._io.pos()
        self._debug['commands']['start'] = self._io.pos()
        self.commands = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['commands']:
                self._debug['commands']['arr'] = []
            self._debug['commands']['arr'].append({'start': self._io.pos()})
            _t_commands = BtrfsStream.SendCommand(self._io, self, self._root)
            _t_commands._read()
            self.commands.append(_t_commands)
            self._debug['commands']['arr'][len(self.commands) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['commands']['end'] = self._io.pos()

    class SendStreamHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(13)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x62\x74\x72\x66\x73\x2D\x73\x74\x72\x65\x61\x6D\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x62\x74\x72\x66\x73\x2D\x73\x74\x72\x65\x61\x6D\x00", self.magic, self._io, u"/types/send_stream_header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()


    class SendCommand(KaitaiStruct):
        SEQ_FIELDS = ["len_data", "type", "checksum", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(BtrfsStream.Command, self._io.read_u2le())
            self._debug['type']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_bytes(4)
            self._debug['checksum']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self._raw_data = self._io.read_bytes(self.len_data)
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = BtrfsStream.SendCommand.Tlvs(_io__raw_data, self, self._root)
            self.data._read()
            self._debug['data']['end'] = self._io.pos()

        class Tlv(KaitaiStruct):
            SEQ_FIELDS = ["type", "length", "value"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['type']['start'] = self._io.pos()
                self.type = KaitaiStream.resolve_enum(BtrfsStream.Attribute, self._io.read_u2le())
                self._debug['type']['end'] = self._io.pos()
                self._debug['length']['start'] = self._io.pos()
                self.length = self._io.read_u2le()
                self._debug['length']['end'] = self._io.pos()
                self._debug['value']['start'] = self._io.pos()
                _on = self.type
                if _on == BtrfsStream.Attribute.ctransid:
                    self.value = self._io.read_u8le()
                elif _on == BtrfsStream.Attribute.size:
                    self.value = self._io.read_u8le()
                elif _on == BtrfsStream.Attribute.clone_uuid:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.Uuid(_io__raw_value, self, self._root)
                    self.value._read()
                elif _on == BtrfsStream.Attribute.file_offset:
                    self.value = self._io.read_u8le()
                elif _on == BtrfsStream.Attribute.otime:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.Timespec(_io__raw_value, self, self._root)
                    self.value._read()
                elif _on == BtrfsStream.Attribute.uid:
                    self.value = self._io.read_u8le()
                elif _on == BtrfsStream.Attribute.atime:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.Timespec(_io__raw_value, self, self._root)
                    self.value._read()
                elif _on == BtrfsStream.Attribute.ctime:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.Timespec(_io__raw_value, self, self._root)
                    self.value._read()
                elif _on == BtrfsStream.Attribute.uuid:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.Uuid(_io__raw_value, self, self._root)
                    self.value._read()
                elif _on == BtrfsStream.Attribute.clone_len:
                    self.value = self._io.read_u8le()
                elif _on == BtrfsStream.Attribute.xattr_name:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.String(_io__raw_value, self, self._root)
                    self.value._read()
                elif _on == BtrfsStream.Attribute.clone_ctransid:
                    self.value = self._io.read_u8le()
                elif _on == BtrfsStream.Attribute.mode:
                    self.value = self._io.read_u8le()
                elif _on == BtrfsStream.Attribute.mtime:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.Timespec(_io__raw_value, self, self._root)
                    self.value._read()
                elif _on == BtrfsStream.Attribute.path_link:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.String(_io__raw_value, self, self._root)
                    self.value._read()
                elif _on == BtrfsStream.Attribute.rdev:
                    self.value = self._io.read_u8le()
                elif _on == BtrfsStream.Attribute.path_to:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.String(_io__raw_value, self, self._root)
                    self.value._read()
                elif _on == BtrfsStream.Attribute.path:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.String(_io__raw_value, self, self._root)
                    self.value._read()
                elif _on == BtrfsStream.Attribute.clone_offset:
                    self.value = self._io.read_u8le()
                elif _on == BtrfsStream.Attribute.gid:
                    self.value = self._io.read_u8le()
                elif _on == BtrfsStream.Attribute.clone_path:
                    self._raw_value = self._io.read_bytes(self.length)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = BtrfsStream.SendCommand.String(_io__raw_value, self, self._root)
                    self.value._read()
                else:
                    self.value = self._io.read_bytes(self.length)
                self._debug['value']['end'] = self._io.pos()


        class Uuid(KaitaiStruct):
            SEQ_FIELDS = ["uuid"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['uuid']['start'] = self._io.pos()
                self.uuid = self._io.read_bytes(16)
                self._debug['uuid']['end'] = self._io.pos()


        class Tlvs(KaitaiStruct):
            SEQ_FIELDS = ["tlv"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['tlv']['start'] = self._io.pos()
                self.tlv = []
                i = 0
                while not self._io.is_eof():
                    if not 'arr' in self._debug['tlv']:
                        self._debug['tlv']['arr'] = []
                    self._debug['tlv']['arr'].append({'start': self._io.pos()})
                    _t_tlv = BtrfsStream.SendCommand.Tlv(self._io, self, self._root)
                    _t_tlv._read()
                    self.tlv.append(_t_tlv)
                    self._debug['tlv']['arr'][len(self.tlv) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['tlv']['end'] = self._io.pos()


        class String(KaitaiStruct):
            SEQ_FIELDS = ["string"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['string']['start'] = self._io.pos()
                self.string = (self._io.read_bytes_full()).decode(u"UTF-8")
                self._debug['string']['end'] = self._io.pos()


        class Timespec(KaitaiStruct):
            SEQ_FIELDS = ["ts_sec", "ts_nsec"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['ts_sec']['start'] = self._io.pos()
                self.ts_sec = self._io.read_s8le()
                self._debug['ts_sec']['end'] = self._io.pos()
                self._debug['ts_nsec']['start'] = self._io.pos()
                self.ts_nsec = self._io.read_s4le()
                self._debug['ts_nsec']['end'] = self._io.pos()




