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

class PythonPyc27(KaitaiStruct):
    """Python interpreter runs .py files in 2 step process: first, it
    produces bytecode, which it then executes. Translation of .py source
    into bytecode is time-consuming, so Python dumps compiled bytecode
    into .pyc files, to be reused from cache at later time if possible.
    
    .pyc file is essentially a raw dump of `py_object` (see `body`) with
    a simple header prepended.
    """

    class Version(Enum):
        v15 = 20121
        v16 = 50428
        v20 = 50823
        v21 = 60202
        v22 = 60717
        v23_a0 = 62011
        v23_a0b = 62021
        v24_a0 = 62041
        v24_a3 = 62051
        v24_b1 = 62061
        v25_a0 = 62071
        v25_a0b = 62081
        v25_a0c = 62091
        v25_a0d = 62092
        v25_b3 = 62101
        v25_b3b = 62111
        v25_c1 = 62121
        v25_c2 = 62131
        v26_a0 = 62151
        v26_a1 = 62161
        v27_a0 = 62171
        v27_a0b = 62181
        v27_a0c = 62191
        v27_a0d = 62201
        v27_a0e = 62211
    SEQ_FIELDS = ["version_magic", "crlf", "modification_timestamp", "body"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['version_magic']['start'] = self._io.pos()
        self.version_magic = KaitaiStream.resolve_enum(PythonPyc27.Version, self._io.read_u2le())
        self._debug['version_magic']['end'] = self._io.pos()
        self._debug['crlf']['start'] = self._io.pos()
        self.crlf = self._io.read_u2le()
        self._debug['crlf']['end'] = self._io.pos()
        self._debug['modification_timestamp']['start'] = self._io.pos()
        self.modification_timestamp = self._io.read_u4le()
        self._debug['modification_timestamp']['end'] = self._io.pos()
        self._debug['body']['start'] = self._io.pos()
        self.body = PythonPyc27.PyObject(self._io, self, self._root)
        self.body._read()
        self._debug['body']['end'] = self._io.pos()

    class CodeObject(KaitaiStruct):

        class FlagsEnum(Enum):
            has_args = 4
            has_kwargs = 8
            generator = 32
        SEQ_FIELDS = ["arg_count", "local_count", "stack_size", "flags", "code", "consts", "names", "var_names", "free_vars", "cell_vars", "filename", "name", "first_line_no", "lnotab"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['arg_count']['start'] = self._io.pos()
            self.arg_count = self._io.read_u4le()
            self._debug['arg_count']['end'] = self._io.pos()
            self._debug['local_count']['start'] = self._io.pos()
            self.local_count = self._io.read_u4le()
            self._debug['local_count']['end'] = self._io.pos()
            self._debug['stack_size']['start'] = self._io.pos()
            self.stack_size = self._io.read_u4le()
            self._debug['stack_size']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(PythonPyc27.CodeObject.FlagsEnum, self._io.read_u4le())
            self._debug['flags']['end'] = self._io.pos()
            self._debug['code']['start'] = self._io.pos()
            self.code = PythonPyc27.Assembly(self._io, self, self._root)
            self.code._read()
            self._debug['code']['end'] = self._io.pos()
            self._debug['consts']['start'] = self._io.pos()
            self.consts = PythonPyc27.PyObject(self._io, self, self._root)
            self.consts._read()
            self._debug['consts']['end'] = self._io.pos()
            self._debug['names']['start'] = self._io.pos()
            self.names = PythonPyc27.PyObject(self._io, self, self._root)
            self.names._read()
            self._debug['names']['end'] = self._io.pos()
            self._debug['var_names']['start'] = self._io.pos()
            self.var_names = PythonPyc27.PyObject(self._io, self, self._root)
            self.var_names._read()
            self._debug['var_names']['end'] = self._io.pos()
            self._debug['free_vars']['start'] = self._io.pos()
            self.free_vars = PythonPyc27.PyObject(self._io, self, self._root)
            self.free_vars._read()
            self._debug['free_vars']['end'] = self._io.pos()
            self._debug['cell_vars']['start'] = self._io.pos()
            self.cell_vars = PythonPyc27.PyObject(self._io, self, self._root)
            self.cell_vars._read()
            self._debug['cell_vars']['end'] = self._io.pos()
            self._debug['filename']['start'] = self._io.pos()
            self.filename = PythonPyc27.PyObject(self._io, self, self._root)
            self.filename._read()
            self._debug['filename']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = PythonPyc27.PyObject(self._io, self, self._root)
            self.name._read()
            self._debug['name']['end'] = self._io.pos()
            self._debug['first_line_no']['start'] = self._io.pos()
            self.first_line_no = self._io.read_u4le()
            self._debug['first_line_no']['end'] = self._io.pos()
            self._debug['lnotab']['start'] = self._io.pos()
            self.lnotab = PythonPyc27.PyObject(self._io, self, self._root)
            self.lnotab._read()
            self._debug['lnotab']['end'] = self._io.pos()


    class Assembly(KaitaiStruct):
        SEQ_FIELDS = ["string_magic", "length", "items"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['string_magic']['start'] = self._io.pos()
            self.string_magic = self._io.read_bytes(1)
            self._debug['string_magic']['end'] = self._io.pos()
            if not self.string_magic == b"\x73":
                raise kaitaistruct.ValidationNotEqualError(b"\x73", self.string_magic, self._io, u"/types/assembly/seq/0")
            self._debug['length']['start'] = self._io.pos()
            self.length = self._io.read_u4le()
            self._debug['length']['end'] = self._io.pos()
            self._debug['items']['start'] = self._io.pos()
            self._raw_items = self._io.read_bytes(self.length)
            _io__raw_items = KaitaiStream(BytesIO(self._raw_items))
            self.items = PythonPyc27.OpArgs(_io__raw_items, self, self._root)
            self.items._read()
            self._debug['items']['end'] = self._io.pos()


    class OpArg(KaitaiStruct):

        class OpCodeEnum(Enum):
            stop_code = 0
            pop_top = 1
            rot_two = 2
            rot_three = 3
            dup_top = 4
            rot_four = 5
            nop = 9
            unary_positive = 10
            unary_negative = 11
            unary_not = 12
            unary_convert = 13
            unary_invert = 15
            binary_power = 19
            binary_multiply = 20
            binary_divide = 21
            binary_modulo = 22
            binary_add = 23
            binary_subtract = 24
            binary_subscr = 25
            binary_floor_divide = 26
            binary_true_divide = 27
            inplace_floor_divide = 28
            inplace_true_divide = 29
            slice_0 = 30
            slice_1 = 31
            slice_2 = 32
            slice_3 = 33
            store_slice_0 = 40
            store_slice_1 = 41
            store_slice_2 = 42
            store_slice_3 = 43
            delete_slice_0 = 50
            delete_slice_1 = 51
            delete_slice_2 = 52
            delete_slice_3 = 53
            store_map = 54
            inplace_add = 55
            inplace_subtract = 56
            inplace_multiply = 57
            inplace_divide = 58
            inplace_modulo = 59
            store_subscr = 60
            delete_subscr = 61
            binary_lshift = 62
            binary_rshift = 63
            binary_and = 64
            binary_xor = 65
            binary_or = 66
            inplace_power = 67
            get_iter = 68
            print_expr = 70
            print_item = 71
            print_newline = 72
            print_item_to = 73
            print_newline_to = 74
            inplace_lshift = 75
            inplace_rshift = 76
            inplace_and = 77
            inplace_xor = 78
            inplace_or = 79
            break_loop = 80
            with_cleanup = 81
            load_locals = 82
            return_value = 83
            import_star = 84
            exec_stmt = 85
            yield_value = 86
            pop_block = 87
            end_finally = 88
            build_class = 89
            store_name = 90
            delete_name = 91
            unpack_sequence = 92
            for_iter = 93
            list_append = 94
            store_attr = 95
            delete_attr = 96
            store_global = 97
            delete_global = 98
            dup_topx = 99
            load_const = 100
            load_name = 101
            build_tuple = 102
            build_list = 103
            build_set = 104
            build_map = 105
            load_attr = 106
            compare_op = 107
            import_name = 108
            import_from = 109
            jump_forward = 110
            jump_if_false_or_pop = 111
            jump_if_true_or_pop = 112
            jump_absolute = 113
            pop_jump_if_false = 114
            pop_jump_if_true = 115
            load_global = 116
            continue_loop = 119
            setup_loop = 120
            setup_except = 121
            setup_finally = 122
            load_fast = 124
            store_fast = 125
            delete_fast = 126
            raise_varargs = 130
            call_function = 131
            make_function = 132
            build_slice = 133
            make_closure = 134
            load_closure = 135
            load_deref = 136
            store_deref = 137
            call_function_var = 140
            call_function_kw = 141
            call_function_var_kw = 142
            setup_with = 143
            extended_arg = 145
            set_add = 146
            map_add = 147
        SEQ_FIELDS = ["op_code", "arg"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['op_code']['start'] = self._io.pos()
            self.op_code = KaitaiStream.resolve_enum(PythonPyc27.OpArg.OpCodeEnum, self._io.read_u1())
            self._debug['op_code']['end'] = self._io.pos()
            if self.op_code.value >= PythonPyc27.OpArg.OpCodeEnum.store_name.value:
                self._debug['arg']['start'] = self._io.pos()
                self.arg = self._io.read_u2le()
                self._debug['arg']['end'] = self._io.pos()



    class PyObject(KaitaiStruct):

        class ObjectType(Enum):
            tuple = 40
            py_false = 70
            none = 78
            string_ref = 82
            py_true = 84
            code_object = 99
            int = 105
            string = 115
            interned = 116
            unicode_string = 117
        SEQ_FIELDS = ["type", "value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(PythonPyc27.PyObject.ObjectType, self._io.read_u1())
            self._debug['type']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            _on = self.type
            if _on == PythonPyc27.PyObject.ObjectType.string:
                self.value = PythonPyc27.PyObject.PyString(self._io, self, self._root)
                self.value._read()
            elif _on == PythonPyc27.PyObject.ObjectType.tuple:
                self.value = PythonPyc27.PyObject.Tuple(self._io, self, self._root)
                self.value._read()
            elif _on == PythonPyc27.PyObject.ObjectType.int:
                self.value = self._io.read_u4le()
            elif _on == PythonPyc27.PyObject.ObjectType.py_true:
                self.value = PythonPyc27.PyObject.PyTrue(self._io, self, self._root)
                self.value._read()
            elif _on == PythonPyc27.PyObject.ObjectType.py_false:
                self.value = PythonPyc27.PyObject.PyFalse(self._io, self, self._root)
                self.value._read()
            elif _on == PythonPyc27.PyObject.ObjectType.none:
                self.value = PythonPyc27.PyObject.PyNone(self._io, self, self._root)
                self.value._read()
            elif _on == PythonPyc27.PyObject.ObjectType.string_ref:
                self.value = PythonPyc27.PyObject.StringRef(self._io, self, self._root)
                self.value._read()
            elif _on == PythonPyc27.PyObject.ObjectType.code_object:
                self.value = PythonPyc27.CodeObject(self._io, self, self._root)
                self.value._read()
            elif _on == PythonPyc27.PyObject.ObjectType.interned:
                self.value = PythonPyc27.PyObject.InternedString(self._io, self, self._root)
                self.value._read()
            self._debug['value']['end'] = self._io.pos()

        class PyNone(KaitaiStruct):
            SEQ_FIELDS = []
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                pass


        class PyFalse(KaitaiStruct):
            SEQ_FIELDS = []
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                pass


        class StringRef(KaitaiStruct):
            SEQ_FIELDS = ["interned_list_index"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['interned_list_index']['start'] = self._io.pos()
                self.interned_list_index = self._io.read_u4le()
                self._debug['interned_list_index']['end'] = self._io.pos()


        class PyTrue(KaitaiStruct):
            SEQ_FIELDS = []
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                pass


        class Tuple(KaitaiStruct):
            SEQ_FIELDS = ["count", "items"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['count']['start'] = self._io.pos()
                self.count = self._io.read_u4le()
                self._debug['count']['end'] = self._io.pos()
                self._debug['items']['start'] = self._io.pos()
                self.items = [None] * (self.count)
                for i in range(self.count):
                    if not 'arr' in self._debug['items']:
                        self._debug['items']['arr'] = []
                    self._debug['items']['arr'].append({'start': self._io.pos()})
                    _t_items = PythonPyc27.PyObject(self._io, self, self._root)
                    _t_items._read()
                    self.items[i] = _t_items
                    self._debug['items']['arr'][i]['end'] = self._io.pos()

                self._debug['items']['end'] = self._io.pos()


        class UnicodeString(KaitaiStruct):
            SEQ_FIELDS = ["length", "data"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['length']['start'] = self._io.pos()
                self.length = self._io.read_u4le()
                self._debug['length']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                self.data = (self._io.read_bytes(self.length)).decode(u"utf-8")
                self._debug['data']['end'] = self._io.pos()


        class InternedString(KaitaiStruct):
            SEQ_FIELDS = ["length", "data"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['length']['start'] = self._io.pos()
                self.length = self._io.read_u4le()
                self._debug['length']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                self.data = (self._io.read_bytes(self.length)).decode(u"utf-8")
                self._debug['data']['end'] = self._io.pos()


        class PyString(KaitaiStruct):
            SEQ_FIELDS = ["length", "data"]
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._debug = collections.defaultdict(dict)

            def _read(self):
                self._debug['length']['start'] = self._io.pos()
                self.length = self._io.read_u4le()
                self._debug['length']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                self.data = self._io.read_bytes(self.length)
                self._debug['data']['end'] = self._io.pos()



    class OpArgs(KaitaiStruct):
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
                _t_items = PythonPyc27.OpArg(self._io, self, self._root)
                _t_items._read()
                self.items.append(_t_items)
                self._debug['items']['arr'][len(self.items) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['items']['end'] = self._io.pos()



