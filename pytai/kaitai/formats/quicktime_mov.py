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

class QuicktimeMov(KaitaiStruct):
    """
    .. seealso::
       Source - https://developer.apple.com/library/content/documentation/QuickTime/QTFF/QTFFChap1/qtff1.html#//apple_ref/doc/uid/TP40000939-CH203-BBCGDDDF
    """

    class AtomType(Enum):
        xtra = 1484026465
        dinf = 1684631142
        dref = 1685218662
        edts = 1701082227
        elst = 1701606260
        free = 1718773093
        ftyp = 1718909296
        hdlr = 1751411826
        iods = 1768907891
        mdat = 1835295092
        mdhd = 1835296868
        mdia = 1835297121
        meta = 1835365473
        minf = 1835626086
        moof = 1836019558
        moov = 1836019574
        mvhd = 1836476516
        smhd = 1936549988
        stbl = 1937007212
        stco = 1937007471
        stsc = 1937011555
        stsd = 1937011556
        stsz = 1937011578
        stts = 1937011827
        tkhd = 1953196132
        traf = 1953653094
        trak = 1953653099
        tref = 1953654118
        udta = 1969517665
        vmhd = 1986881636

    class Brand(Enum):
        x_3g2a = 862401121
        x_3ge6 = 862414134
        x_3ge9 = 862414137
        x_3gf9 = 862414393
        x_3gg6 = 862414646
        x_3gg9 = 862414649
        x_3gh9 = 862414905
        x_3gm9 = 862416185
        x_3gp4 = 862416948
        x_3gp5 = 862416949
        x_3gp6 = 862416950
        x_3gp7 = 862416951
        x_3gp8 = 862416952
        x_3gp9 = 862416953
        x_3gr6 = 862417462
        x_3gr9 = 862417465
        x_3gs6 = 862417718
        x_3gs9 = 862417721
        x_3gt9 = 862417977
        arri = 1095914057
        caep = 1128351056
        cdes = 1128555891
        j2p0 = 1244811312
        j2p1 = 1244811313
        lcag = 1279476039
        m4a = 1295270176
        m4b = 1295270432
        m4p = 1295274016
        m4v = 1295275552
        mfsm = 1296454477
        mgsv = 1296520022
        mppi = 1297109065
        msnv = 1297305174
        ross = 1380930387
        seau = 1397047637
        sebk = 1397047883
        xavc = 1480676931
        avc1 = 1635148593
        bbxm = 1650620525
        caqv = 1667330422
        ccff = 1667458662
        da0a = 1684090977
        da0b = 1684090978
        da1a = 1684091233
        da1b = 1684091234
        da2a = 1684091489
        da2b = 1684091490
        da3a = 1684091745
        da3b = 1684091746
        dash = 1684108136
        dby1 = 1684175153
        dmb1 = 1684890161
        dsms = 1685286259
        dv1a = 1685467489
        dv1b = 1685467490
        dv2a = 1685467745
        dv2b = 1685467746
        dv3a = 1685468001
        dv3b = 1685468002
        dvr1 = 1685484081
        dvt1 = 1685484593
        dxo = 1685614368
        emsg = 1701671783
        ifrm = 1768321645
        isc2 = 1769169714
        iso2 = 1769172786
        iso3 = 1769172787
        iso4 = 1769172788
        iso5 = 1769172789
        iso6 = 1769172790
        isom = 1769172845
        jp2 = 1785737760
        jpm = 1785752864
        jpsi = 1785754473
        jpx = 1785755680
        jpxb = 1785755746
        lmsg = 1819112295
        mj2s = 1835676275
        mjp2 = 1835692082
        mp21 = 1836069425
        mp41 = 1836069937
        mp42 = 1836069938
        mp71 = 1836070705
        msdh = 1836278888
        msix = 1836280184
        niko = 1852402543
        odcf = 1868850022
        opf2 = 1869637170
        opx2 = 1869641778
        pana = 1885433441
        piff = 1885955686
        pnvi = 1886287465
        qt = 1903435808
        risx = 1919513464
        sdv = 1935963680
        senv = 1936027254
        sims = 1936289139
        sisx = 1936290680
        ssss = 1936946035
        uvvu = 1970697845
    SEQ_FIELDS = ["atoms"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['atoms']['start'] = self._io.pos()
        self.atoms = QuicktimeMov.AtomList(self._io, self, self._root)
        self.atoms._read()
        self._debug['atoms']['end'] = self._io.pos()

    class MvhdBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://developer.apple.com/library/content/documentation/QuickTime/QTFF/QTFFChap2/qtff2.html#//apple_ref/doc/uid/TP40000939-CH204-BBCGFGJG
        """
        SEQ_FIELDS = ["version", "flags", "creation_time", "modification_time", "time_scale", "duration", "preferred_rate", "preferred_volume", "reserved1", "matrix", "preview_time", "preview_duration", "poster_time", "selection_time", "selection_duration", "current_time", "next_track_id"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_bytes(3)
            self._debug['flags']['end'] = self._io.pos()
            self._debug['creation_time']['start'] = self._io.pos()
            self.creation_time = self._io.read_u4be()
            self._debug['creation_time']['end'] = self._io.pos()
            self._debug['modification_time']['start'] = self._io.pos()
            self.modification_time = self._io.read_u4be()
            self._debug['modification_time']['end'] = self._io.pos()
            self._debug['time_scale']['start'] = self._io.pos()
            self.time_scale = self._io.read_u4be()
            self._debug['time_scale']['end'] = self._io.pos()
            self._debug['duration']['start'] = self._io.pos()
            self.duration = self._io.read_u4be()
            self._debug['duration']['end'] = self._io.pos()
            self._debug['preferred_rate']['start'] = self._io.pos()
            self.preferred_rate = QuicktimeMov.Fixed32(self._io, self, self._root)
            self.preferred_rate._read()
            self._debug['preferred_rate']['end'] = self._io.pos()
            self._debug['preferred_volume']['start'] = self._io.pos()
            self.preferred_volume = QuicktimeMov.Fixed16(self._io, self, self._root)
            self.preferred_volume._read()
            self._debug['preferred_volume']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bytes(10)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['matrix']['start'] = self._io.pos()
            self.matrix = self._io.read_bytes(36)
            self._debug['matrix']['end'] = self._io.pos()
            self._debug['preview_time']['start'] = self._io.pos()
            self.preview_time = self._io.read_u4be()
            self._debug['preview_time']['end'] = self._io.pos()
            self._debug['preview_duration']['start'] = self._io.pos()
            self.preview_duration = self._io.read_u4be()
            self._debug['preview_duration']['end'] = self._io.pos()
            self._debug['poster_time']['start'] = self._io.pos()
            self.poster_time = self._io.read_u4be()
            self._debug['poster_time']['end'] = self._io.pos()
            self._debug['selection_time']['start'] = self._io.pos()
            self.selection_time = self._io.read_u4be()
            self._debug['selection_time']['end'] = self._io.pos()
            self._debug['selection_duration']['start'] = self._io.pos()
            self.selection_duration = self._io.read_u4be()
            self._debug['selection_duration']['end'] = self._io.pos()
            self._debug['current_time']['start'] = self._io.pos()
            self.current_time = self._io.read_u4be()
            self._debug['current_time']['end'] = self._io.pos()
            self._debug['next_track_id']['start'] = self._io.pos()
            self.next_track_id = self._io.read_u4be()
            self._debug['next_track_id']['end'] = self._io.pos()


    class FtypBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://developer.apple.com/library/content/documentation/QuickTime/QTFF/QTFFChap1/qtff1.html#//apple_ref/doc/uid/TP40000939-CH203-CJBCBIFF
        """
        SEQ_FIELDS = ["major_brand", "minor_version", "compatible_brands"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['major_brand']['start'] = self._io.pos()
            self.major_brand = KaitaiStream.resolve_enum(QuicktimeMov.Brand, self._io.read_u4be())
            self._debug['major_brand']['end'] = self._io.pos()
            self._debug['minor_version']['start'] = self._io.pos()
            self.minor_version = self._io.read_bytes(4)
            self._debug['minor_version']['end'] = self._io.pos()
            self._debug['compatible_brands']['start'] = self._io.pos()
            self.compatible_brands = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['compatible_brands']:
                    self._debug['compatible_brands']['arr'] = []
                self._debug['compatible_brands']['arr'].append({'start': self._io.pos()})
                self.compatible_brands.append(KaitaiStream.resolve_enum(QuicktimeMov.Brand, self._io.read_u4be()))
                self._debug['compatible_brands']['arr'][len(self.compatible_brands) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['compatible_brands']['end'] = self._io.pos()


    class Fixed32(KaitaiStruct):
        """Fixed-point 32-bit number."""
        SEQ_FIELDS = ["int_part", "frac_part"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['int_part']['start'] = self._io.pos()
            self.int_part = self._io.read_s2be()
            self._debug['int_part']['end'] = self._io.pos()
            self._debug['frac_part']['start'] = self._io.pos()
            self.frac_part = self._io.read_u2be()
            self._debug['frac_part']['end'] = self._io.pos()


    class Fixed16(KaitaiStruct):
        """Fixed-point 16-bit number."""
        SEQ_FIELDS = ["int_part", "frac_part"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['int_part']['start'] = self._io.pos()
            self.int_part = self._io.read_s1()
            self._debug['int_part']['end'] = self._io.pos()
            self._debug['frac_part']['start'] = self._io.pos()
            self.frac_part = self._io.read_u1()
            self._debug['frac_part']['end'] = self._io.pos()


    class Atom(KaitaiStruct):
        SEQ_FIELDS = ["len32", "atom_type", "len64", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len32']['start'] = self._io.pos()
            self.len32 = self._io.read_u4be()
            self._debug['len32']['end'] = self._io.pos()
            self._debug['atom_type']['start'] = self._io.pos()
            self.atom_type = KaitaiStream.resolve_enum(QuicktimeMov.AtomType, self._io.read_u4be())
            self._debug['atom_type']['end'] = self._io.pos()
            if self.len32 == 1:
                self._debug['len64']['start'] = self._io.pos()
                self.len64 = self._io.read_u8be()
                self._debug['len64']['end'] = self._io.pos()

            self._debug['body']['start'] = self._io.pos()
            _on = self.atom_type
            if _on == QuicktimeMov.AtomType.moof:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == QuicktimeMov.AtomType.tkhd:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.TkhdBody(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == QuicktimeMov.AtomType.stbl:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == QuicktimeMov.AtomType.traf:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == QuicktimeMov.AtomType.minf:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == QuicktimeMov.AtomType.trak:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == QuicktimeMov.AtomType.moov:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == QuicktimeMov.AtomType.mdia:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == QuicktimeMov.AtomType.dinf:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == QuicktimeMov.AtomType.mvhd:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.MvhdBody(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == QuicktimeMov.AtomType.ftyp:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.FtypBody(_io__raw_body, self, self._root)
                self.body._read()
            else:
                self.body = self._io.read_bytes(self.len)
            self._debug['body']['end'] = self._io.pos()

        @property
        def len(self):
            if hasattr(self, '_m_len'):
                return self._m_len if hasattr(self, '_m_len') else None

            self._m_len = ((self._io.size() - 8) if self.len32 == 0 else ((self.len64 - 16) if self.len32 == 1 else (self.len32 - 8)))
            return self._m_len if hasattr(self, '_m_len') else None


    class TkhdBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://developer.apple.com/library/content/documentation/QuickTime/QTFF/QTFFChap2/qtff2.html#//apple_ref/doc/uid/TP40000939-CH204-25550
        """
        SEQ_FIELDS = ["version", "flags", "creation_time", "modification_time", "track_id", "reserved1", "duration", "reserved2", "layer", "alternative_group", "volume", "reserved3", "matrix", "width", "height"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_bytes(3)
            self._debug['flags']['end'] = self._io.pos()
            self._debug['creation_time']['start'] = self._io.pos()
            self.creation_time = self._io.read_u4be()
            self._debug['creation_time']['end'] = self._io.pos()
            self._debug['modification_time']['start'] = self._io.pos()
            self.modification_time = self._io.read_u4be()
            self._debug['modification_time']['end'] = self._io.pos()
            self._debug['track_id']['start'] = self._io.pos()
            self.track_id = self._io.read_u4be()
            self._debug['track_id']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bytes(4)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['duration']['start'] = self._io.pos()
            self.duration = self._io.read_u4be()
            self._debug['duration']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(8)
            self._debug['reserved2']['end'] = self._io.pos()
            self._debug['layer']['start'] = self._io.pos()
            self.layer = self._io.read_u2be()
            self._debug['layer']['end'] = self._io.pos()
            self._debug['alternative_group']['start'] = self._io.pos()
            self.alternative_group = self._io.read_u2be()
            self._debug['alternative_group']['end'] = self._io.pos()
            self._debug['volume']['start'] = self._io.pos()
            self.volume = self._io.read_u2be()
            self._debug['volume']['end'] = self._io.pos()
            self._debug['reserved3']['start'] = self._io.pos()
            self.reserved3 = self._io.read_u2be()
            self._debug['reserved3']['end'] = self._io.pos()
            self._debug['matrix']['start'] = self._io.pos()
            self.matrix = self._io.read_bytes(36)
            self._debug['matrix']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = QuicktimeMov.Fixed32(self._io, self, self._root)
            self.width._read()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = QuicktimeMov.Fixed32(self._io, self, self._root)
            self.height._read()
            self._debug['height']['end'] = self._io.pos()


    class AtomList(KaitaiStruct):
        SEQ_FIELDS = ["items"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['items']['start'] = self._io.pos()
            self.items = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['items']:
                    self._debug['items']['arr'] = []
                self._debug['items']['arr'].append({'start': self._io.pos()})
                _t_items = QuicktimeMov.Atom(self._io, self, self._root)
                _t_items._read()
                self.items.append(_t_items)
                self._debug['items']['arr'][len(self.items) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['items']['end'] = self._io.pos()



