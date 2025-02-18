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

class Warcraft2Pud(KaitaiStruct):
    """Warcraft II game engine uses this format for map files. External
    maps can be edited by official Warcraft II map editor and saved in
    .pud files. Maps supplied with the game (i.e. single player
    campaign) follow the same format, but are instead embedded inside
    the game container files.
    
    There are two major versions: 0x11 (original one) and 0x13 (roughly
    corresponds to v1.33 of the game engine, although some of the
    features got limited support in v1.3).
    
    File consists of a sequence of typed sections.
    
    .. seealso::
       Source - http://cade.datamax.bg/war2x/pudspec.html
    """

    class Controller(Enum):
        computer = 1
        passive_computer = 2
        nobody = 3
        computer = 4
        human = 5
        rescue_passive = 6
        rescue_active = 7

    class TerrainType(Enum):
        forest = 0
        winter = 1
        wasteland = 2
        swamp = 3

    class UnitType(Enum):
        infantry = 0
        grunt = 1
        peasant = 2
        peon = 3
        ballista = 4
        catapult = 5
        knight = 6
        ogre = 7
        archer = 8
        axethrower = 9
        mage = 10
        death_knight = 11
        paladin = 12
        ogre_mage = 13
        dwarves = 14
        goblin_sapper = 15
        attack_peasant = 16
        attack_peon = 17
        ranger = 18
        berserker = 19
        alleria = 20
        teron_gorefiend = 21
        kurdan_and_sky_ree = 22
        dentarg = 23
        khadgar = 24
        grom_hellscream = 25
        human_tanker = 26
        orc_tanker = 27
        human_transport = 28
        orc_transport = 29
        elven_destroyer = 30
        troll_destroyer = 31
        battleship = 32
        juggernaught = 33
        deathwing = 35
        gnomish_submarine = 38
        giant_turtle = 39
        gnomish_flying_machine = 40
        goblin_zepplin = 41
        gryphon_rider = 42
        dragon = 43
        turalyon = 44
        eye_of_kilrogg = 45
        danath = 46
        khorgath_bladefist = 47
        cho_gall = 49
        lothar = 50
        gul_dan = 51
        uther_lightbringer = 52
        zuljin = 53
        skeleton = 55
        daemon = 56
        critter = 57
        farm = 58
        pig_farm = 59
        human_barracks = 60
        orc_barracks = 61
        church = 62
        altar_of_storms = 63
        human_scout_tower = 64
        orc_scout_tower = 65
        stables = 66
        ogre_mound = 67
        gnomish_inventor = 68
        goblin_alchemist = 69
        gryphon_aviary = 70
        dragon_roost = 71
        human_shipyard = 72
        orc_shipyard = 73
        town_hall = 74
        great_hall = 75
        elven_lumber_mill = 76
        troll_lumber_mill = 77
        human_foundry = 78
        orc_foundry = 79
        mage_tower = 80
        temple_of_the_damned = 81
        human_blacksmith = 82
        orc_blacksmith = 83
        human_refinery = 84
        orc_refinery = 85
        human_oil_well = 86
        orc_oil_well = 87
        keep = 88
        stronghold = 89
        castle = 90
        fortress = 91
        gold_mine = 92
        oil_patch = 93
        human_start = 94
        orc_start = 95
        human_guard_tower = 96
        orc_guard_tower = 97
        human_cannon_tower = 98
        orc_cannon_tower = 99
        circle_of_power = 100
        dark_portal = 101
        runestone = 102
        human_wall = 103
        orc_wall = 104
    SEQ_FIELDS = ["sections"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['sections']['start'] = self._io.pos()
        self.sections = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['sections']:
                self._debug['sections']['arr'] = []
            self._debug['sections']['arr'].append({'start': self._io.pos()})
            _t_sections = Warcraft2Pud.Section(self._io, self, self._root)
            _t_sections._read()
            self.sections.append(_t_sections)
            self._debug['sections']['arr'][len(self.sections) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['sections']['end'] = self._io.pos()

    class SectionStartingResource(KaitaiStruct):
        SEQ_FIELDS = ["resources_by_player"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['resources_by_player']['start'] = self._io.pos()
            self.resources_by_player = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['resources_by_player']:
                    self._debug['resources_by_player']['arr'] = []
                self._debug['resources_by_player']['arr'].append({'start': self._io.pos()})
                self.resources_by_player.append(self._io.read_u2le())
                self._debug['resources_by_player']['arr'][len(self.resources_by_player) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['resources_by_player']['end'] = self._io.pos()


    class SectionEra(KaitaiStruct):
        """Section that specifies terrain type for this map."""
        SEQ_FIELDS = ["terrain"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['terrain']['start'] = self._io.pos()
            self.terrain = KaitaiStream.resolve_enum(Warcraft2Pud.TerrainType, self._io.read_u2le())
            self._debug['terrain']['end'] = self._io.pos()


    class SectionVer(KaitaiStruct):
        """Section that specifies format version."""
        SEQ_FIELDS = ["version"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u2le()
            self._debug['version']['end'] = self._io.pos()


    class SectionDim(KaitaiStruct):
        SEQ_FIELDS = ["x", "y"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_u2le()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_u2le()
            self._debug['y']['end'] = self._io.pos()


    class SectionType(KaitaiStruct):
        """Section that confirms that this file is a "map file" by certain
        magic string and supplies a tag that could be used in
        multiplayer to check that all player use the same version of the
        map.
        """
        SEQ_FIELDS = ["magic", "unused", "id_tag"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(10)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x57\x41\x52\x32\x20\x4D\x41\x50\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x57\x41\x52\x32\x20\x4D\x41\x50\x00\x00", self.magic, self._io, u"/types/section_type/seq/0")
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bytes(2)
            self._debug['unused']['end'] = self._io.pos()
            self._debug['id_tag']['start'] = self._io.pos()
            self.id_tag = self._io.read_u4le()
            self._debug['id_tag']['end'] = self._io.pos()


    class SectionUnit(KaitaiStruct):
        SEQ_FIELDS = ["units"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['units']['start'] = self._io.pos()
            self.units = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['units']:
                    self._debug['units']['arr'] = []
                self._debug['units']['arr'].append({'start': self._io.pos()})
                _t_units = Warcraft2Pud.Unit(self._io, self, self._root)
                _t_units._read()
                self.units.append(_t_units)
                self._debug['units']['arr'][len(self.units) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['units']['end'] = self._io.pos()


    class Section(KaitaiStruct):
        SEQ_FIELDS = ["name", "size", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.name
            if _on == u"SLBR":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionStartingResource(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"ERAX":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionEra(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"OWNR":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionOwnr(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"ERA ":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionEra(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"SGLD":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionStartingResource(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"VER ":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionVer(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"SOIL":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionStartingResource(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"UNIT":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionUnit(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"DIM ":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionDim(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == u"TYPE":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionType(_io__raw_body, self, self._root)
                self.body._read()
            else:
                self.body = self._io.read_bytes(self.size)
            self._debug['body']['end'] = self._io.pos()


    class SectionOwnr(KaitaiStruct):
        """Section that specifies who controls each player."""
        SEQ_FIELDS = ["controller_by_player"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['controller_by_player']['start'] = self._io.pos()
            self.controller_by_player = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['controller_by_player']:
                    self._debug['controller_by_player']['arr'] = []
                self._debug['controller_by_player']['arr'].append({'start': self._io.pos()})
                self.controller_by_player.append(KaitaiStream.resolve_enum(Warcraft2Pud.Controller, self._io.read_u1()))
                self._debug['controller_by_player']['arr'][len(self.controller_by_player) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['controller_by_player']['end'] = self._io.pos()


    class Unit(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "u_type", "owner", "options"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_u2le()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_u2le()
            self._debug['y']['end'] = self._io.pos()
            self._debug['u_type']['start'] = self._io.pos()
            self.u_type = KaitaiStream.resolve_enum(Warcraft2Pud.UnitType, self._io.read_u1())
            self._debug['u_type']['end'] = self._io.pos()
            self._debug['owner']['start'] = self._io.pos()
            self.owner = self._io.read_u1()
            self._debug['owner']['end'] = self._io.pos()
            self._debug['options']['start'] = self._io.pos()
            self.options = self._io.read_u2le()
            self._debug['options']['end'] = self._io.pos()

        @property
        def resource(self):
            if hasattr(self, '_m_resource'):
                return self._m_resource if hasattr(self, '_m_resource') else None

            if  ((self.u_type == Warcraft2Pud.UnitType.gold_mine) or (self.u_type == Warcraft2Pud.UnitType.human_oil_well) or (self.u_type == Warcraft2Pud.UnitType.orc_oil_well) or (self.u_type == Warcraft2Pud.UnitType.oil_patch)) :
                self._m_resource = (self.options * 2500)

            return self._m_resource if hasattr(self, '_m_resource') else None



