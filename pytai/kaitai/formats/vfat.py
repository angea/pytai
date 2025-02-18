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


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

import dos_datetime
class Vfat(KaitaiStruct):
    """
    .. seealso::
       Source - https://download.microsoft.com/download/0/8/4/084c452b-b772-4fe5-89bb-a0cbf082286a/fatgen103.doc
    """
    SEQ_FIELDS = ["boot_sector"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['boot_sector']['start'] = self._io.pos()
        self.boot_sector = Vfat.BootSector(self._io, self, self._root)
        self.boot_sector._read()
        self._debug['boot_sector']['end'] = self._io.pos()

    class ExtBiosParamBlockFat32(KaitaiStruct):
        """Extended BIOS Parameter Block for FAT32."""
        SEQ_FIELDS = ["ls_per_fat", "has_active_fat", "reserved1", "active_fat_id", "reserved2", "fat_version", "root_dir_start_clus", "ls_fs_info", "boot_sectors_copy_start_ls", "reserved3", "phys_drive_num", "reserved4", "ext_boot_sign", "volume_id", "partition_volume_label", "fs_type_str"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['ls_per_fat']['start'] = self._io.pos()
            self.ls_per_fat = self._io.read_u4le()
            self._debug['ls_per_fat']['end'] = self._io.pos()
            self._debug['has_active_fat']['start'] = self._io.pos()
            self.has_active_fat = self._io.read_bits_int_le(1) != 0
            self._debug['has_active_fat']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bits_int_le(3)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['active_fat_id']['start'] = self._io.pos()
            self.active_fat_id = self._io.read_bits_int_le(4)
            self._debug['active_fat_id']['end'] = self._io.pos()
            self._io.align_to_byte()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(1)
            self._debug['reserved2']['end'] = self._io.pos()
            if not self.reserved2 == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.reserved2, self._io, u"/types/ext_bios_param_block_fat32/seq/4")
            self._debug['fat_version']['start'] = self._io.pos()
            self.fat_version = self._io.read_u2le()
            self._debug['fat_version']['end'] = self._io.pos()
            self._debug['root_dir_start_clus']['start'] = self._io.pos()
            self.root_dir_start_clus = self._io.read_u4le()
            self._debug['root_dir_start_clus']['end'] = self._io.pos()
            self._debug['ls_fs_info']['start'] = self._io.pos()
            self.ls_fs_info = self._io.read_u2le()
            self._debug['ls_fs_info']['end'] = self._io.pos()
            self._debug['boot_sectors_copy_start_ls']['start'] = self._io.pos()
            self.boot_sectors_copy_start_ls = self._io.read_u2le()
            self._debug['boot_sectors_copy_start_ls']['end'] = self._io.pos()
            self._debug['reserved3']['start'] = self._io.pos()
            self.reserved3 = self._io.read_bytes(12)
            self._debug['reserved3']['end'] = self._io.pos()
            self._debug['phys_drive_num']['start'] = self._io.pos()
            self.phys_drive_num = self._io.read_u1()
            self._debug['phys_drive_num']['end'] = self._io.pos()
            self._debug['reserved4']['start'] = self._io.pos()
            self.reserved4 = self._io.read_u1()
            self._debug['reserved4']['end'] = self._io.pos()
            self._debug['ext_boot_sign']['start'] = self._io.pos()
            self.ext_boot_sign = self._io.read_u1()
            self._debug['ext_boot_sign']['end'] = self._io.pos()
            self._debug['volume_id']['start'] = self._io.pos()
            self.volume_id = self._io.read_bytes(4)
            self._debug['volume_id']['end'] = self._io.pos()
            self._debug['partition_volume_label']['start'] = self._io.pos()
            self.partition_volume_label = (KaitaiStream.bytes_strip_right(self._io.read_bytes(11), 32)).decode(u"ASCII")
            self._debug['partition_volume_label']['end'] = self._io.pos()
            self._debug['fs_type_str']['start'] = self._io.pos()
            self.fs_type_str = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32)).decode(u"ASCII")
            self._debug['fs_type_str']['end'] = self._io.pos()


    class BootSector(KaitaiStruct):
        SEQ_FIELDS = ["jmp_instruction", "oem_name", "bpb", "ebpb_fat16", "ebpb_fat32"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['jmp_instruction']['start'] = self._io.pos()
            self.jmp_instruction = self._io.read_bytes(3)
            self._debug['jmp_instruction']['end'] = self._io.pos()
            self._debug['oem_name']['start'] = self._io.pos()
            self.oem_name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32)).decode(u"ASCII")
            self._debug['oem_name']['end'] = self._io.pos()
            self._debug['bpb']['start'] = self._io.pos()
            self.bpb = Vfat.BiosParamBlock(self._io, self, self._root)
            self.bpb._read()
            self._debug['bpb']['end'] = self._io.pos()
            if not (self.is_fat32):
                self._debug['ebpb_fat16']['start'] = self._io.pos()
                self.ebpb_fat16 = Vfat.ExtBiosParamBlockFat16(self._io, self, self._root)
                self.ebpb_fat16._read()
                self._debug['ebpb_fat16']['end'] = self._io.pos()

            if self.is_fat32:
                self._debug['ebpb_fat32']['start'] = self._io.pos()
                self.ebpb_fat32 = Vfat.ExtBiosParamBlockFat32(self._io, self, self._root)
                self.ebpb_fat32._read()
                self._debug['ebpb_fat32']['end'] = self._io.pos()


        @property
        def pos_fats(self):
            """Offset of FATs in bytes from start of filesystem."""
            if hasattr(self, '_m_pos_fats'):
                return self._m_pos_fats if hasattr(self, '_m_pos_fats') else None

            self._m_pos_fats = (self.bpb.bytes_per_ls * self.bpb.num_reserved_ls)
            return self._m_pos_fats if hasattr(self, '_m_pos_fats') else None

        @property
        def ls_per_fat(self):
            if hasattr(self, '_m_ls_per_fat'):
                return self._m_ls_per_fat if hasattr(self, '_m_ls_per_fat') else None

            self._m_ls_per_fat = (self.ebpb_fat32.ls_per_fat if self.is_fat32 else self.bpb.ls_per_fat)
            return self._m_ls_per_fat if hasattr(self, '_m_ls_per_fat') else None

        @property
        def ls_per_root_dir(self):
            """Size of root directory in logical sectors.
            
            .. seealso::
               FAT: General Overview of On-Disk Format, section "FAT Data Structure"
            """
            if hasattr(self, '_m_ls_per_root_dir'):
                return self._m_ls_per_root_dir if hasattr(self, '_m_ls_per_root_dir') else None

            self._m_ls_per_root_dir = (((self.bpb.max_root_dir_rec * 32) + self.bpb.bytes_per_ls) - 1) // self.bpb.bytes_per_ls
            return self._m_ls_per_root_dir if hasattr(self, '_m_ls_per_root_dir') else None

        @property
        def is_fat32(self):
            """Determines if filesystem is FAT32 (true) or FAT12/16 (false)
            by analyzing some preliminary conditions in BPB. Used to
            determine whether we should parse post-BPB data as
            `ext_bios_param_block_fat16` or `ext_bios_param_block_fat32`.
            """
            if hasattr(self, '_m_is_fat32'):
                return self._m_is_fat32 if hasattr(self, '_m_is_fat32') else None

            self._m_is_fat32 = self.bpb.max_root_dir_rec == 0
            return self._m_is_fat32 if hasattr(self, '_m_is_fat32') else None

        @property
        def size_fat(self):
            """Size of one FAT in bytes."""
            if hasattr(self, '_m_size_fat'):
                return self._m_size_fat if hasattr(self, '_m_size_fat') else None

            self._m_size_fat = (self.bpb.bytes_per_ls * self.ls_per_fat)
            return self._m_size_fat if hasattr(self, '_m_size_fat') else None

        @property
        def pos_root_dir(self):
            """Offset of root directory in bytes from start of filesystem."""
            if hasattr(self, '_m_pos_root_dir'):
                return self._m_pos_root_dir if hasattr(self, '_m_pos_root_dir') else None

            self._m_pos_root_dir = (self.bpb.bytes_per_ls * (self.bpb.num_reserved_ls + (self.ls_per_fat * self.bpb.num_fats)))
            return self._m_pos_root_dir if hasattr(self, '_m_pos_root_dir') else None

        @property
        def size_root_dir(self):
            """Size of root directory in bytes."""
            if hasattr(self, '_m_size_root_dir'):
                return self._m_size_root_dir if hasattr(self, '_m_size_root_dir') else None

            self._m_size_root_dir = (self.ls_per_root_dir * self.bpb.bytes_per_ls)
            return self._m_size_root_dir if hasattr(self, '_m_size_root_dir') else None


    class BiosParamBlock(KaitaiStruct):
        SEQ_FIELDS = ["bytes_per_ls", "ls_per_clus", "num_reserved_ls", "num_fats", "max_root_dir_rec", "total_ls_2", "media_code", "ls_per_fat", "ps_per_track", "num_heads", "num_hidden_sectors", "total_ls_4"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['bytes_per_ls']['start'] = self._io.pos()
            self.bytes_per_ls = self._io.read_u2le()
            self._debug['bytes_per_ls']['end'] = self._io.pos()
            self._debug['ls_per_clus']['start'] = self._io.pos()
            self.ls_per_clus = self._io.read_u1()
            self._debug['ls_per_clus']['end'] = self._io.pos()
            self._debug['num_reserved_ls']['start'] = self._io.pos()
            self.num_reserved_ls = self._io.read_u2le()
            self._debug['num_reserved_ls']['end'] = self._io.pos()
            self._debug['num_fats']['start'] = self._io.pos()
            self.num_fats = self._io.read_u1()
            self._debug['num_fats']['end'] = self._io.pos()
            self._debug['max_root_dir_rec']['start'] = self._io.pos()
            self.max_root_dir_rec = self._io.read_u2le()
            self._debug['max_root_dir_rec']['end'] = self._io.pos()
            self._debug['total_ls_2']['start'] = self._io.pos()
            self.total_ls_2 = self._io.read_u2le()
            self._debug['total_ls_2']['end'] = self._io.pos()
            self._debug['media_code']['start'] = self._io.pos()
            self.media_code = self._io.read_u1()
            self._debug['media_code']['end'] = self._io.pos()
            self._debug['ls_per_fat']['start'] = self._io.pos()
            self.ls_per_fat = self._io.read_u2le()
            self._debug['ls_per_fat']['end'] = self._io.pos()
            self._debug['ps_per_track']['start'] = self._io.pos()
            self.ps_per_track = self._io.read_u2le()
            self._debug['ps_per_track']['end'] = self._io.pos()
            self._debug['num_heads']['start'] = self._io.pos()
            self.num_heads = self._io.read_u2le()
            self._debug['num_heads']['end'] = self._io.pos()
            self._debug['num_hidden_sectors']['start'] = self._io.pos()
            self.num_hidden_sectors = self._io.read_u4le()
            self._debug['num_hidden_sectors']['end'] = self._io.pos()
            self._debug['total_ls_4']['start'] = self._io.pos()
            self.total_ls_4 = self._io.read_u4le()
            self._debug['total_ls_4']['end'] = self._io.pos()


    class RootDirectoryRec(KaitaiStruct):
        SEQ_FIELDS = ["file_name", "attrs", "reserved", "last_write_time", "start_clus", "file_size"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['file_name']['start'] = self._io.pos()
            self.file_name = self._io.read_bytes(11)
            self._debug['file_name']['end'] = self._io.pos()
            self._debug['attrs']['start'] = self._io.pos()
            self._raw_attrs = self._io.read_bytes(1)
            _io__raw_attrs = KaitaiStream(BytesIO(self._raw_attrs))
            self.attrs = Vfat.RootDirectoryRec.AttrFlags(_io__raw_attrs, self, self._root)
            self.attrs._read()
            self._debug['attrs']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(10)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['last_write_time']['start'] = self._io.pos()
            self._raw_last_write_time = self._io.read_bytes(4)
            _io__raw_last_write_time = KaitaiStream(BytesIO(self._raw_last_write_time))
            self.last_write_time = dos_datetime.DosDatetime(_io__raw_last_write_time)
            self.last_write_time._read()
            self._debug['last_write_time']['end'] = self._io.pos()
            self._debug['start_clus']['start'] = self._io.pos()
            self.start_clus = self._io.read_u2le()
            self._debug['start_clus']['end'] = self._io.pos()
            self._debug['file_size']['start'] = self._io.pos()
            self.file_size = self._io.read_u4le()
            self._debug['file_size']['end'] = self._io.pos()

        class AttrFlags(KaitaiStruct):
            SEQ_FIELDS = ["read_only", "hidden", "system", "volume_id", "is_directory", "archive", "reserved"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['read_only']['start'] = self._io.pos()
                self.read_only = self._io.read_bits_int_le(1) != 0
                self._debug['read_only']['end'] = self._io.pos()
                self._debug['hidden']['start'] = self._io.pos()
                self.hidden = self._io.read_bits_int_le(1) != 0
                self._debug['hidden']['end'] = self._io.pos()
                self._debug['system']['start'] = self._io.pos()
                self.system = self._io.read_bits_int_le(1) != 0
                self._debug['system']['end'] = self._io.pos()
                self._debug['volume_id']['start'] = self._io.pos()
                self.volume_id = self._io.read_bits_int_le(1) != 0
                self._debug['volume_id']['end'] = self._io.pos()
                self._debug['is_directory']['start'] = self._io.pos()
                self.is_directory = self._io.read_bits_int_le(1) != 0
                self._debug['is_directory']['end'] = self._io.pos()
                self._debug['archive']['start'] = self._io.pos()
                self.archive = self._io.read_bits_int_le(1) != 0
                self._debug['archive']['end'] = self._io.pos()
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_bits_int_le(2)
                self._debug['reserved']['end'] = self._io.pos()

            @property
            def long_name(self):
                if hasattr(self, '_m_long_name'):
                    return self._m_long_name if hasattr(self, '_m_long_name') else None

                self._m_long_name =  ((self.read_only) and (self.hidden) and (self.system) and (self.volume_id)) 
                return self._m_long_name if hasattr(self, '_m_long_name') else None



    class RootDirectory(KaitaiStruct):
        SEQ_FIELDS = ["records"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['records']['start'] = self._io.pos()
            self.records = [None] * (self._root.boot_sector.bpb.max_root_dir_rec)
            for i in range(self._root.boot_sector.bpb.max_root_dir_rec):
                if not 'arr' in self._debug['records']:
                    self._debug['records']['arr'] = []
                self._debug['records']['arr'].append({'start': self._io.pos()})
                _t_records = Vfat.RootDirectoryRec(self._io, self, self._root)
                _t_records._read()
                self.records[i] = _t_records
                self._debug['records']['arr'][i]['end'] = self._io.pos()

            self._debug['records']['end'] = self._io.pos()


    class ExtBiosParamBlockFat16(KaitaiStruct):
        """Extended BIOS Parameter Block (DOS 4.0+, OS/2 1.0+). Used only
        for FAT12 and FAT16.
        """
        SEQ_FIELDS = ["phys_drive_num", "reserved1", "ext_boot_sign", "volume_id", "partition_volume_label", "fs_type_str"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['phys_drive_num']['start'] = self._io.pos()
            self.phys_drive_num = self._io.read_u1()
            self._debug['phys_drive_num']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_u1()
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['ext_boot_sign']['start'] = self._io.pos()
            self.ext_boot_sign = self._io.read_u1()
            self._debug['ext_boot_sign']['end'] = self._io.pos()
            self._debug['volume_id']['start'] = self._io.pos()
            self.volume_id = self._io.read_bytes(4)
            self._debug['volume_id']['end'] = self._io.pos()
            self._debug['partition_volume_label']['start'] = self._io.pos()
            self.partition_volume_label = (KaitaiStream.bytes_strip_right(self._io.read_bytes(11), 32)).decode(u"ASCII")
            self._debug['partition_volume_label']['end'] = self._io.pos()
            self._debug['fs_type_str']['start'] = self._io.pos()
            self.fs_type_str = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32)).decode(u"ASCII")
            self._debug['fs_type_str']['end'] = self._io.pos()


    @property
    def fats(self):
        if hasattr(self, '_m_fats'):
            return self._m_fats if hasattr(self, '_m_fats') else None

        _pos = self._io.pos()
        self._io.seek(self.boot_sector.pos_fats)
        self._debug['_m_fats']['start'] = self._io.pos()
        self._m_fats = [None] * (self.boot_sector.bpb.num_fats)
        for i in range(self.boot_sector.bpb.num_fats):
            if not 'arr' in self._debug['_m_fats']:
                self._debug['_m_fats']['arr'] = []
            self._debug['_m_fats']['arr'].append({'start': self._io.pos()})
            self._m_fats[i] = self._io.read_bytes(self.boot_sector.size_fat)
            self._debug['_m_fats']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_fats']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_fats if hasattr(self, '_m_fats') else None

    @property
    def root_dir(self):
        if hasattr(self, '_m_root_dir'):
            return self._m_root_dir if hasattr(self, '_m_root_dir') else None

        _pos = self._io.pos()
        self._io.seek(self.boot_sector.pos_root_dir)
        self._debug['_m_root_dir']['start'] = self._io.pos()
        self._raw__m_root_dir = self._io.read_bytes(self.boot_sector.size_root_dir)
        _io__raw__m_root_dir = KaitaiStream(BytesIO(self._raw__m_root_dir))
        self._m_root_dir = Vfat.RootDirectory(_io__raw__m_root_dir, self, self._root)
        self._m_root_dir._read()
        self._debug['_m_root_dir']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_root_dir if hasattr(self, '_m_root_dir') else None


