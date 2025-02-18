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

class WindowsMinidump(KaitaiStruct):
    """Windows MiniDump (MDMP) file provides a concise way to store process
    core dumps, which is useful for debugging. Given its small size,
    modularity, some cross-platform features and native support in some
    debuggers, it is particularly useful for crash reporting, and is
    used for that purpose in Windows and Google Chrome projects.
    
    The file itself is a container, which contains a number of typed
    "streams", which contain some data according to its type attribute.
    
    .. seealso::
       Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_header
    """

    class StreamTypes(Enum):
        unused = 0
        reserved_0 = 1
        reserved_1 = 2
        thread_list = 3
        module_list = 4
        memory_list = 5
        exception = 6
        system_info = 7
        thread_ex_list = 8
        memory_64_list = 9
        comment_a = 10
        comment_w = 11
        handle_data = 12
        function_table = 13
        unloaded_module_list = 14
        misc_info = 15
        memory_info_list = 16
        thread_info_list = 17
        handle_operation_list = 18
        token = 19
        java_script_data = 20
        system_memory_info = 21
        process_vm_vounters = 22
        ipt_trace = 23
        thread_names = 24
        ce_null = 32768
        ce_system_info = 32769
        ce_exception = 32770
        ce_module_list = 32771
        ce_process_list = 32772
        ce_thread_list = 32773
        ce_thread_context_list = 32774
        ce_thread_call_stack_list = 32775
        ce_memory_virtual_list = 32776
        ce_memory_physical_list = 32777
        ce_bucket_parameters = 32778
        ce_process_module_map = 32779
        ce_diagnosis_list = 32780
        md_crashpad_info_stream = 1129316353
        md_raw_breakpad_info = 1197932545
        md_raw_assertion_info = 1197932546
        md_linux_cpu_info = 1197932547
        md_linux_proc_status = 1197932548
        md_linux_lsb_release = 1197932549
        md_linux_cmd_line = 1197932550
        md_linux_environ = 1197932551
        md_linux_auxv = 1197932552
        md_linux_maps = 1197932553
        md_linux_dso_debug = 1197932554
    SEQ_FIELDS = ["magic1", "magic2", "version", "num_streams", "ofs_streams", "checksum", "timestamp", "flags"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['magic1']['start'] = self._io.pos()
        self.magic1 = self._io.read_bytes(4)
        self._debug['magic1']['end'] = self._io.pos()
        if not self.magic1 == b"\x4D\x44\x4D\x50":
            raise kaitaistruct.ValidationNotEqualError(b"\x4D\x44\x4D\x50", self.magic1, self._io, u"/seq/0")
        self._debug['magic2']['start'] = self._io.pos()
        self.magic2 = self._io.read_bytes(2)
        self._debug['magic2']['end'] = self._io.pos()
        if not self.magic2 == b"\x93\xA7":
            raise kaitaistruct.ValidationNotEqualError(b"\x93\xA7", self.magic2, self._io, u"/seq/1")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u2le()
        self._debug['version']['end'] = self._io.pos()
        self._debug['num_streams']['start'] = self._io.pos()
        self.num_streams = self._io.read_u4le()
        self._debug['num_streams']['end'] = self._io.pos()
        self._debug['ofs_streams']['start'] = self._io.pos()
        self.ofs_streams = self._io.read_u4le()
        self._debug['ofs_streams']['end'] = self._io.pos()
        self._debug['checksum']['start'] = self._io.pos()
        self.checksum = self._io.read_u4le()
        self._debug['checksum']['end'] = self._io.pos()
        self._debug['timestamp']['start'] = self._io.pos()
        self.timestamp = self._io.read_u4le()
        self._debug['timestamp']['end'] = self._io.pos()
        self._debug['flags']['start'] = self._io.pos()
        self.flags = self._io.read_u8le()
        self._debug['flags']['end'] = self._io.pos()

    class ThreadList(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_thread_list
        """
        SEQ_FIELDS = ["num_threads", "threads"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_threads']['start'] = self._io.pos()
            self.num_threads = self._io.read_u4le()
            self._debug['num_threads']['end'] = self._io.pos()
            self._debug['threads']['start'] = self._io.pos()
            self.threads = [None] * (self.num_threads)
            for i in range(self.num_threads):
                if not 'arr' in self._debug['threads']:
                    self._debug['threads']['arr'] = []
                self._debug['threads']['arr'].append({'start': self._io.pos()})
                _t_threads = WindowsMinidump.Thread(self._io, self, self._root)
                _t_threads._read()
                self.threads[i] = _t_threads
                self._debug['threads']['arr'][i]['end'] = self._io.pos()

            self._debug['threads']['end'] = self._io.pos()


    class LocationDescriptor(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_location_descriptor
        """
        SEQ_FIELDS = ["len_data", "ofs_data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4le()
            self._debug['ofs_data']['end'] = self._io.pos()

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data if hasattr(self, '_m_data') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_data)
            self._debug['_m_data']['start'] = io.pos()
            self._m_data = io.read_bytes(self.len_data)
            self._debug['_m_data']['end'] = io.pos()
            io.seek(_pos)
            return self._m_data if hasattr(self, '_m_data') else None


    class MinidumpString(KaitaiStruct):
        """Specific string serialization scheme used in MiniDump format is
        actually a simple 32-bit length-prefixed UTF-16 string.
        
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_string
        """
        SEQ_FIELDS = ["len_str", "str"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_str']['start'] = self._io.pos()
            self.len_str = self._io.read_u4le()
            self._debug['len_str']['end'] = self._io.pos()
            self._debug['str']['start'] = self._io.pos()
            self.str = (self._io.read_bytes(self.len_str)).decode(u"UTF-16LE")
            self._debug['str']['end'] = self._io.pos()


    class SystemInfo(KaitaiStruct):
        """"System info" stream provides basic information about the
        hardware and operating system which produces this dump.
        
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_system_info
        """

        class CpuArchs(Enum):
            intel = 0
            arm = 5
            ia64 = 6
            amd64 = 9
            unknown = 65535
        SEQ_FIELDS = ["cpu_arch", "cpu_level", "cpu_revision", "num_cpus", "os_type", "os_ver_major", "os_ver_minor", "os_build", "os_platform", "ofs_service_pack", "os_suite_mask", "reserved2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['cpu_arch']['start'] = self._io.pos()
            self.cpu_arch = KaitaiStream.resolve_enum(WindowsMinidump.SystemInfo.CpuArchs, self._io.read_u2le())
            self._debug['cpu_arch']['end'] = self._io.pos()
            self._debug['cpu_level']['start'] = self._io.pos()
            self.cpu_level = self._io.read_u2le()
            self._debug['cpu_level']['end'] = self._io.pos()
            self._debug['cpu_revision']['start'] = self._io.pos()
            self.cpu_revision = self._io.read_u2le()
            self._debug['cpu_revision']['end'] = self._io.pos()
            self._debug['num_cpus']['start'] = self._io.pos()
            self.num_cpus = self._io.read_u1()
            self._debug['num_cpus']['end'] = self._io.pos()
            self._debug['os_type']['start'] = self._io.pos()
            self.os_type = self._io.read_u1()
            self._debug['os_type']['end'] = self._io.pos()
            self._debug['os_ver_major']['start'] = self._io.pos()
            self.os_ver_major = self._io.read_u4le()
            self._debug['os_ver_major']['end'] = self._io.pos()
            self._debug['os_ver_minor']['start'] = self._io.pos()
            self.os_ver_minor = self._io.read_u4le()
            self._debug['os_ver_minor']['end'] = self._io.pos()
            self._debug['os_build']['start'] = self._io.pos()
            self.os_build = self._io.read_u4le()
            self._debug['os_build']['end'] = self._io.pos()
            self._debug['os_platform']['start'] = self._io.pos()
            self.os_platform = self._io.read_u4le()
            self._debug['os_platform']['end'] = self._io.pos()
            self._debug['ofs_service_pack']['start'] = self._io.pos()
            self.ofs_service_pack = self._io.read_u4le()
            self._debug['ofs_service_pack']['end'] = self._io.pos()
            self._debug['os_suite_mask']['start'] = self._io.pos()
            self.os_suite_mask = self._io.read_u2le()
            self._debug['os_suite_mask']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_u2le()
            self._debug['reserved2']['end'] = self._io.pos()

        @property
        def service_pack(self):
            if hasattr(self, '_m_service_pack'):
                return self._m_service_pack if hasattr(self, '_m_service_pack') else None

            if self.ofs_service_pack > 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_service_pack)
                self._debug['_m_service_pack']['start'] = io.pos()
                self._m_service_pack = WindowsMinidump.MinidumpString(io, self, self._root)
                self._m_service_pack._read()
                self._debug['_m_service_pack']['end'] = io.pos()
                io.seek(_pos)

            return self._m_service_pack if hasattr(self, '_m_service_pack') else None


    class ExceptionRecord(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_exception
        """
        SEQ_FIELDS = ["code", "flags", "inner_exception", "addr", "num_params", "reserved", "params"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['code']['start'] = self._io.pos()
            self.code = self._io.read_u4le()
            self._debug['code']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['inner_exception']['start'] = self._io.pos()
            self.inner_exception = self._io.read_u8le()
            self._debug['inner_exception']['end'] = self._io.pos()
            self._debug['addr']['start'] = self._io.pos()
            self.addr = self._io.read_u8le()
            self._debug['addr']['end'] = self._io.pos()
            self._debug['num_params']['start'] = self._io.pos()
            self.num_params = self._io.read_u4le()
            self._debug['num_params']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u4le()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['params']['start'] = self._io.pos()
            self.params = [None] * (15)
            for i in range(15):
                if not 'arr' in self._debug['params']:
                    self._debug['params']['arr'] = []
                self._debug['params']['arr'].append({'start': self._io.pos()})
                self.params[i] = self._io.read_u8le()
                self._debug['params']['arr'][i]['end'] = self._io.pos()

            self._debug['params']['end'] = self._io.pos()


    class MiscInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_misc_info
        """
        SEQ_FIELDS = ["len_info", "flags1", "process_id", "process_create_time", "process_user_time", "process_kernel_time", "cpu_max_mhz", "cpu_cur_mhz", "cpu_limit_mhz", "cpu_max_idle_state", "cpu_cur_idle_state"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['len_info']['start'] = self._io.pos()
            self.len_info = self._io.read_u4le()
            self._debug['len_info']['end'] = self._io.pos()
            self._debug['flags1']['start'] = self._io.pos()
            self.flags1 = self._io.read_u4le()
            self._debug['flags1']['end'] = self._io.pos()
            self._debug['process_id']['start'] = self._io.pos()
            self.process_id = self._io.read_u4le()
            self._debug['process_id']['end'] = self._io.pos()
            self._debug['process_create_time']['start'] = self._io.pos()
            self.process_create_time = self._io.read_u4le()
            self._debug['process_create_time']['end'] = self._io.pos()
            self._debug['process_user_time']['start'] = self._io.pos()
            self.process_user_time = self._io.read_u4le()
            self._debug['process_user_time']['end'] = self._io.pos()
            self._debug['process_kernel_time']['start'] = self._io.pos()
            self.process_kernel_time = self._io.read_u4le()
            self._debug['process_kernel_time']['end'] = self._io.pos()
            self._debug['cpu_max_mhz']['start'] = self._io.pos()
            self.cpu_max_mhz = self._io.read_u4le()
            self._debug['cpu_max_mhz']['end'] = self._io.pos()
            self._debug['cpu_cur_mhz']['start'] = self._io.pos()
            self.cpu_cur_mhz = self._io.read_u4le()
            self._debug['cpu_cur_mhz']['end'] = self._io.pos()
            self._debug['cpu_limit_mhz']['start'] = self._io.pos()
            self.cpu_limit_mhz = self._io.read_u4le()
            self._debug['cpu_limit_mhz']['end'] = self._io.pos()
            self._debug['cpu_max_idle_state']['start'] = self._io.pos()
            self.cpu_max_idle_state = self._io.read_u4le()
            self._debug['cpu_max_idle_state']['end'] = self._io.pos()
            self._debug['cpu_cur_idle_state']['start'] = self._io.pos()
            self.cpu_cur_idle_state = self._io.read_u4le()
            self._debug['cpu_cur_idle_state']['end'] = self._io.pos()


    class Dir(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_directory
        """
        SEQ_FIELDS = ["stream_type", "len_data", "ofs_data"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['stream_type']['start'] = self._io.pos()
            self.stream_type = KaitaiStream.resolve_enum(WindowsMinidump.StreamTypes, self._io.read_u4le())
            self._debug['stream_type']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4le()
            self._debug['ofs_data']['end'] = self._io.pos()

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data if hasattr(self, '_m_data') else None

            _pos = self._io.pos()
            self._io.seek(self.ofs_data)
            self._debug['_m_data']['start'] = self._io.pos()
            _on = self.stream_type
            if _on == WindowsMinidump.StreamTypes.memory_list:
                self._raw__m_data = self._io.read_bytes(self.len_data)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = WindowsMinidump.MemoryList(_io__raw__m_data, self, self._root)
                self._m_data._read()
            elif _on == WindowsMinidump.StreamTypes.misc_info:
                self._raw__m_data = self._io.read_bytes(self.len_data)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = WindowsMinidump.MiscInfo(_io__raw__m_data, self, self._root)
                self._m_data._read()
            elif _on == WindowsMinidump.StreamTypes.thread_list:
                self._raw__m_data = self._io.read_bytes(self.len_data)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = WindowsMinidump.ThreadList(_io__raw__m_data, self, self._root)
                self._m_data._read()
            elif _on == WindowsMinidump.StreamTypes.exception:
                self._raw__m_data = self._io.read_bytes(self.len_data)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = WindowsMinidump.ExceptionStream(_io__raw__m_data, self, self._root)
                self._m_data._read()
            elif _on == WindowsMinidump.StreamTypes.system_info:
                self._raw__m_data = self._io.read_bytes(self.len_data)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = WindowsMinidump.SystemInfo(_io__raw__m_data, self, self._root)
                self._m_data._read()
            else:
                self._m_data = self._io.read_bytes(self.len_data)
            self._debug['_m_data']['end'] = self._io.pos()
            self._io.seek(_pos)
            return self._m_data if hasattr(self, '_m_data') else None


    class Thread(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_thread
        """
        SEQ_FIELDS = ["thread_id", "suspend_count", "priority_class", "priority", "teb", "stack", "thread_context"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['thread_id']['start'] = self._io.pos()
            self.thread_id = self._io.read_u4le()
            self._debug['thread_id']['end'] = self._io.pos()
            self._debug['suspend_count']['start'] = self._io.pos()
            self.suspend_count = self._io.read_u4le()
            self._debug['suspend_count']['end'] = self._io.pos()
            self._debug['priority_class']['start'] = self._io.pos()
            self.priority_class = self._io.read_u4le()
            self._debug['priority_class']['end'] = self._io.pos()
            self._debug['priority']['start'] = self._io.pos()
            self.priority = self._io.read_u4le()
            self._debug['priority']['end'] = self._io.pos()
            self._debug['teb']['start'] = self._io.pos()
            self.teb = self._io.read_u8le()
            self._debug['teb']['end'] = self._io.pos()
            self._debug['stack']['start'] = self._io.pos()
            self.stack = WindowsMinidump.MemoryDescriptor(self._io, self, self._root)
            self.stack._read()
            self._debug['stack']['end'] = self._io.pos()
            self._debug['thread_context']['start'] = self._io.pos()
            self.thread_context = WindowsMinidump.LocationDescriptor(self._io, self, self._root)
            self.thread_context._read()
            self._debug['thread_context']['end'] = self._io.pos()


    class MemoryList(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_memory64_list
        """
        SEQ_FIELDS = ["num_mem_ranges", "mem_ranges"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['num_mem_ranges']['start'] = self._io.pos()
            self.num_mem_ranges = self._io.read_u4le()
            self._debug['num_mem_ranges']['end'] = self._io.pos()
            self._debug['mem_ranges']['start'] = self._io.pos()
            self.mem_ranges = [None] * (self.num_mem_ranges)
            for i in range(self.num_mem_ranges):
                if not 'arr' in self._debug['mem_ranges']:
                    self._debug['mem_ranges']['arr'] = []
                self._debug['mem_ranges']['arr'].append({'start': self._io.pos()})
                _t_mem_ranges = WindowsMinidump.MemoryDescriptor(self._io, self, self._root)
                _t_mem_ranges._read()
                self.mem_ranges[i] = _t_mem_ranges
                self._debug['mem_ranges']['arr'][i]['end'] = self._io.pos()

            self._debug['mem_ranges']['end'] = self._io.pos()


    class MemoryDescriptor(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_memory_descriptor
        """
        SEQ_FIELDS = ["addr_memory_range", "memory"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['addr_memory_range']['start'] = self._io.pos()
            self.addr_memory_range = self._io.read_u8le()
            self._debug['addr_memory_range']['end'] = self._io.pos()
            self._debug['memory']['start'] = self._io.pos()
            self.memory = WindowsMinidump.LocationDescriptor(self._io, self, self._root)
            self.memory._read()
            self._debug['memory']['end'] = self._io.pos()


    class ExceptionStream(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_exception_stream
        """
        SEQ_FIELDS = ["thread_id", "reserved", "exception_rec", "thread_context"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['thread_id']['start'] = self._io.pos()
            self.thread_id = self._io.read_u4le()
            self._debug['thread_id']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u4le()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['exception_rec']['start'] = self._io.pos()
            self.exception_rec = WindowsMinidump.ExceptionRecord(self._io, self, self._root)
            self.exception_rec._read()
            self._debug['exception_rec']['end'] = self._io.pos()
            self._debug['thread_context']['start'] = self._io.pos()
            self.thread_context = WindowsMinidump.LocationDescriptor(self._io, self, self._root)
            self.thread_context._read()
            self._debug['thread_context']['end'] = self._io.pos()


    @property
    def streams(self):
        if hasattr(self, '_m_streams'):
            return self._m_streams if hasattr(self, '_m_streams') else None

        _pos = self._io.pos()
        self._io.seek(self.ofs_streams)
        self._debug['_m_streams']['start'] = self._io.pos()
        self._m_streams = [None] * (self.num_streams)
        for i in range(self.num_streams):
            if not 'arr' in self._debug['_m_streams']:
                self._debug['_m_streams']['arr'] = []
            self._debug['_m_streams']['arr'].append({'start': self._io.pos()})
            _t__m_streams = WindowsMinidump.Dir(self._io, self, self._root)
            _t__m_streams._read()
            self._m_streams[i] = _t__m_streams
            self._debug['_m_streams']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_streams']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_streams if hasattr(self, '_m_streams') else None


