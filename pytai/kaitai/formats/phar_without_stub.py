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

import php_serialized_value
class PharWithoutStub(KaitaiStruct):
    """A phar (PHP archive) file. The phar format is a custom archive format
    from the PHP ecosystem that is used to package a complete PHP library
    or application into a single self-contained archive.
    All phar archives start with an executable PHP stub, which can be used to
    allow executing or including phar files as if they were regular PHP scripts.
    PHP 5.3 and later include the phar extension, which adds native support for
    reading and manipulating phar files.
    
    The phar format was originally developed as part of the PEAR library
    PHP_Archive, first released in 2005. Later, a native PHP extension
    named "phar" was developed, which was first released on PECL in 2007,
    and is included with PHP 5.3 and later. The phar extension has effectively
    superseded the PHP_Archive library, which has not been updated since 2010.
    The phar extension is also no longer released independently on PECL;
    it is now developed and released as part of PHP itself.
    
    Because of current limitations in Kaitai Struct
    (seekaitai-io/kaitai_struct#158 and kaitai-io/kaitai_struct#538),
    the executable PHP stub that precedes the rest of the archive is not handled
    by this spec. Before parsing a phar using this spec, the stub must be
    removed manually.
    
    A phar's stub is terminated by the special token `__HALT_COMPILER();`
    (which may be followed by at most one space, the PHP tag end `?>`,
    and an optional line terminator). The stub termination sequence is
    immediately followed by the remaining parts of the phar format,
    as described in this spec.
    
    The phar stub usually contains code that loads the phar and runs
    a contained PHP file, but this is not required. A minimal valid phar stub
    is `<?php __HALT_COMPILER();` - such a stub makes it impossible to execute
    the phar directly, but still allows loading or manipulating it using the
    phar extension.
    
    Note: The phar format does not specify any encoding for text fields
    (stub, alias name, and all file names), so these fields may contain arbitrary
    binary data. The actual text encoding used in a specific phar file usually
    depends on the application that created the phar, and on the
    standard encoding of the system on which the phar was created.
    
    .. seealso::
       Source - https://www.php.net/manual/en/phar.fileformat.php
    
    
    .. seealso::
       Source - https://github.com/php/php-src/tree/master/ext/phar
    
    
    .. seealso::
       Source - https://svn.php.net/viewvc/pecl/phar/
    
    
    .. seealso::
       Source - https://svn.php.net/viewvc/pear/packages/PHP_Archive/
    """

    class SignatureType(Enum):
        md5 = 1
        sha1 = 2
        sha256 = 4
        sha512 = 8
        openssl = 16
    SEQ_FIELDS = ["manifest", "files", "signature"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['manifest']['start'] = self._io.pos()
        self.manifest = PharWithoutStub.Manifest(self._io, self, self._root)
        self.manifest._read()
        self._debug['manifest']['end'] = self._io.pos()
        self._debug['files']['start'] = self._io.pos()
        self.files = [None] * (self.manifest.num_files)
        for i in range(self.manifest.num_files):
            if not 'arr' in self._debug['files']:
                self._debug['files']['arr'] = []
            self._debug['files']['arr'].append({'start': self._io.pos()})
            self.files[i] = self._io.read_bytes(self.manifest.file_entries[i].len_data_compressed)
            self._debug['files']['arr'][i]['end'] = self._io.pos()

        self._debug['files']['end'] = self._io.pos()
        if self.manifest.flags.has_signature:
            self._debug['signature']['start'] = self._io.pos()
            self._raw_signature = self._io.read_bytes_full()
            _io__raw_signature = KaitaiStream(BytesIO(self._raw_signature))
            self.signature = PharWithoutStub.Signature(_io__raw_signature, self, self._root)
            self.signature._read()
            self._debug['signature']['end'] = self._io.pos()


    class SerializedValue(KaitaiStruct):
        SEQ_FIELDS = ["raw"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['raw']['start'] = self._io.pos()
            self.raw = self._io.read_bytes_full()
            self._debug['raw']['end'] = self._io.pos()

        @property
        def parsed(self):
            """The serialized value, parsed as a structure."""
            if hasattr(self, '_m_parsed'):
                return self._m_parsed if hasattr(self, '_m_parsed') else None

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_parsed']['start'] = self._io.pos()
            self._m_parsed = php_serialized_value.PhpSerializedValue(self._io)
            self._m_parsed._read()
            self._debug['_m_parsed']['end'] = self._io.pos()
            self._io.seek(_pos)
            return self._m_parsed if hasattr(self, '_m_parsed') else None


    class Signature(KaitaiStruct):
        SEQ_FIELDS = ["data", "type", "magic"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(((self._io.size() - self._io.pos()) - 8))
            self._debug['data']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(PharWithoutStub.SignatureType, self._io.read_u4le())
            self._debug['type']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x47\x42\x4D\x42":
                raise kaitaistruct.ValidationNotEqualError(b"\x47\x42\x4D\x42", self.magic, self._io, u"/types/signature/seq/2")


    class FileFlags(KaitaiStruct):
        SEQ_FIELDS = ["value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_u4le()
            self._debug['value']['end'] = self._io.pos()

        @property
        def permissions(self):
            """The file's permission bits."""
            if hasattr(self, '_m_permissions'):
                return self._m_permissions if hasattr(self, '_m_permissions') else None

            self._m_permissions = (self.value & 511)
            return self._m_permissions if hasattr(self, '_m_permissions') else None

        @property
        def zlib_compressed(self):
            """Whether this file's data is stored using zlib compression."""
            if hasattr(self, '_m_zlib_compressed'):
                return self._m_zlib_compressed if hasattr(self, '_m_zlib_compressed') else None

            self._m_zlib_compressed = (self.value & 4096) != 0
            return self._m_zlib_compressed if hasattr(self, '_m_zlib_compressed') else None

        @property
        def bzip2_compressed(self):
            """Whether this file's data is stored using bzip2 compression."""
            if hasattr(self, '_m_bzip2_compressed'):
                return self._m_bzip2_compressed if hasattr(self, '_m_bzip2_compressed') else None

            self._m_bzip2_compressed = (self.value & 8192) != 0
            return self._m_bzip2_compressed if hasattr(self, '_m_bzip2_compressed') else None


    class ApiVersion(KaitaiStruct):
        """A phar API version number. This version number is meant to indicate
        which features are used in a specific phar, so that tools reading
        the phar can easily check that they support all necessary features.
        
        The following API versions exist so far:
        
        * 0.5, 0.6, 0.7, 0.7.1: The first official API versions. At this point,
          the phar format was only used by the PHP_Archive library, and the
          API version numbers were identical to the PHP_Archive versions that
          supported them. Development of the native phar extension started around
          API version 0.7. These API versions could only be queried using the
          `PHP_Archive::APIversion()` method, but were not stored physically
          in archives. These API versions are not supported by this spec.
        * 0.8.0: Used by PHP_Archive 0.8.0 (released 2006-07-18) and
          later development versions of the phar extension. This is the first
          version number to be physically stored in archives. This API version
          is not supported by this spec.
        * 0.9.0: Used by later development/early beta versions of the
          phar extension. Also temporarily used by PHP_Archive 0.9.0
          (released 2006-12-15), but reverted back to API version 0.8.0 in
          PHP_Archive 0.9.1 (released 2007-01-05).
        * 1.0.0: Supported since PHP_Archive 0.10.0 (released 2007-05-29)
          and phar extension 1.0.0 (released 2007-03-28). This is the first
          stable, forwards-compatible and documented version of the format.
        * 1.1.0: Supported since PHP_Archive 0.12.0 (released 2015-07-06)
          and phar extension 1.1.0 (released 2007-04-12). Adds SHA-256 and
          SHA-512 signature types.
        * 1.1.1: Supported since phar extension 2.0.0 (released 2009-07-29 and
          included with PHP 5.3 and later). (PHP_Archive 0.12.0 also supports
          all features from API verison 1.1.1, but it reports API version 1.1.0.)
          Adds the OpenSSL signature type and support for storing
          empty directories.
        """
        SEQ_FIELDS = ["release", "major", "minor", "unused"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['release']['start'] = self._io.pos()
            self.release = self._io.read_bits_int_be(4)
            self._debug['release']['end'] = self._io.pos()
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_bits_int_be(4)
            self._debug['major']['end'] = self._io.pos()
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_bits_int_be(4)
            self._debug['minor']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bits_int_be(4)
            self._debug['unused']['end'] = self._io.pos()


    class GlobalFlags(KaitaiStruct):
        SEQ_FIELDS = ["value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_u4le()
            self._debug['value']['end'] = self._io.pos()

        @property
        def any_zlib_compressed(self):
            """Whether any of the files in this phar are stored using
            zlib compression.
            """
            if hasattr(self, '_m_any_zlib_compressed'):
                return self._m_any_zlib_compressed if hasattr(self, '_m_any_zlib_compressed') else None

            self._m_any_zlib_compressed = (self.value & 4096) != 0
            return self._m_any_zlib_compressed if hasattr(self, '_m_any_zlib_compressed') else None

        @property
        def any_bzip2_compressed(self):
            """Whether any of the files in this phar are stored using
            bzip2 compression.
            """
            if hasattr(self, '_m_any_bzip2_compressed'):
                return self._m_any_bzip2_compressed if hasattr(self, '_m_any_bzip2_compressed') else None

            self._m_any_bzip2_compressed = (self.value & 8192) != 0
            return self._m_any_bzip2_compressed if hasattr(self, '_m_any_bzip2_compressed') else None

        @property
        def has_signature(self):
            """Whether this phar contains a signature."""
            if hasattr(self, '_m_has_signature'):
                return self._m_has_signature if hasattr(self, '_m_has_signature') else None

            self._m_has_signature = (self.value & 65536) != 0
            return self._m_has_signature if hasattr(self, '_m_has_signature') else None


    class Manifest(KaitaiStruct):
        SEQ_FIELDS = ["len_manifest", "num_files", "api_version", "flags", "len_alias", "alias", "len_metadata", "metadata", "file_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_manifest']['start'] = self._io.pos()
            self.len_manifest = self._io.read_u4le()
            self._debug['len_manifest']['end'] = self._io.pos()
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u4le()
            self._debug['num_files']['end'] = self._io.pos()
            self._debug['api_version']['start'] = self._io.pos()
            self.api_version = PharWithoutStub.ApiVersion(self._io, self, self._root)
            self.api_version._read()
            self._debug['api_version']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = PharWithoutStub.GlobalFlags(self._io, self, self._root)
            self.flags._read()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['len_alias']['start'] = self._io.pos()
            self.len_alias = self._io.read_u4le()
            self._debug['len_alias']['end'] = self._io.pos()
            self._debug['alias']['start'] = self._io.pos()
            self.alias = self._io.read_bytes(self.len_alias)
            self._debug['alias']['end'] = self._io.pos()
            self._debug['len_metadata']['start'] = self._io.pos()
            self.len_metadata = self._io.read_u4le()
            self._debug['len_metadata']['end'] = self._io.pos()
            if self.len_metadata != 0:
                self._debug['metadata']['start'] = self._io.pos()
                self._raw_metadata = self._io.read_bytes(self.len_metadata)
                _io__raw_metadata = KaitaiStream(BytesIO(self._raw_metadata))
                self.metadata = PharWithoutStub.SerializedValue(_io__raw_metadata, self, self._root)
                self.metadata._read()
                self._debug['metadata']['end'] = self._io.pos()

            self._debug['file_entries']['start'] = self._io.pos()
            self.file_entries = [None] * (self.num_files)
            for i in range(self.num_files):
                if not 'arr' in self._debug['file_entries']:
                    self._debug['file_entries']['arr'] = []
                self._debug['file_entries']['arr'].append({'start': self._io.pos()})
                _t_file_entries = PharWithoutStub.FileEntry(self._io, self, self._root)
                _t_file_entries._read()
                self.file_entries[i] = _t_file_entries
                self._debug['file_entries']['arr'][i]['end'] = self._io.pos()

            self._debug['file_entries']['end'] = self._io.pos()


    class FileEntry(KaitaiStruct):
        SEQ_FIELDS = ["len_filename", "filename", "len_data_uncompressed", "timestamp", "len_data_compressed", "crc32", "flags", "len_metadata", "metadata"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_filename']['start'] = self._io.pos()
            self.len_filename = self._io.read_u4le()
            self._debug['len_filename']['end'] = self._io.pos()
            self._debug['filename']['start'] = self._io.pos()
            self.filename = self._io.read_bytes(self.len_filename)
            self._debug['filename']['end'] = self._io.pos()
            self._debug['len_data_uncompressed']['start'] = self._io.pos()
            self.len_data_uncompressed = self._io.read_u4le()
            self._debug['len_data_uncompressed']['end'] = self._io.pos()
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = self._io.read_u4le()
            self._debug['timestamp']['end'] = self._io.pos()
            self._debug['len_data_compressed']['start'] = self._io.pos()
            self.len_data_compressed = self._io.read_u4le()
            self._debug['len_data_compressed']['end'] = self._io.pos()
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = PharWithoutStub.FileFlags(self._io, self, self._root)
            self.flags._read()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['len_metadata']['start'] = self._io.pos()
            self.len_metadata = self._io.read_u4le()
            self._debug['len_metadata']['end'] = self._io.pos()
            if self.len_metadata != 0:
                self._debug['metadata']['start'] = self._io.pos()
                self._raw_metadata = self._io.read_bytes(self.len_metadata)
                _io__raw_metadata = KaitaiStream(BytesIO(self._raw_metadata))
                self.metadata = PharWithoutStub.SerializedValue(_io__raw_metadata, self, self._root)
                self.metadata._read()
                self._debug['metadata']['end'] = self._io.pos()




