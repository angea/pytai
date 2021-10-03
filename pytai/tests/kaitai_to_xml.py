"""A utility to output an XML representation of a binary file using Kaitai.

License:
    MIT License

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
from typing import Union, List
from pathlib import Path

import xml.etree.ElementTree as ET
import argparse
import sys

try:
    from .. import model
    from .xml_utils import *
except ImportError:
    if __name__ == "__main__":
        sys.exit(f'This utility needs to be run from the root folder:\npython -m pytai.tests.{Path(sys.argv[0]).stem}')
    else:
        raise


def kaitai_to_xml(parser: "KaitaiParser", path: str) -> ET.ElementTree:
    """Transform a KaitaiStruct object to an XML tree.
    
    Args:
        parser: 
            A KaitaiParser instance matching the parsed file.
        
        path:
            Path to file to be converted to XML via the parser.

    Returns:
        XML representation of the file structure.

    """

    root = ET.Element("root")

    def recurse(parent_object: Union[List["KaitaiStruct"], "KaitaiStruct"], parent_node: ET.Element, is_array: bool, add_offset: int) -> None:
        """Recursive function to built the XML tree.

        Args:
            parent_object:
                A KaitaiStruct from which the child nodes will be extracted (if is_array is False),
                or a list of KaitaiStructs (if is_array is True).

            parent_node:
                An XML node representing the parent of child nodes.

            is_array:
                True if parent_object is a list, false otherwise.

            add_offset:
                Offset to add to start and end offsets.
                Needed since Kaitai sometimes returns relative offsets and sometimes absolute offsets.
        
        """
        if is_array:
            values = parent_object
        else:
            values = parser.get_children(parent_object)

        for child_attr in values:
            
            start_offset = child_attr.start_offset
            end_offset = child_attr.end_offset
            if child_attr.start_offset is not None:
                start_offset += add_offset
                end_offset += add_offset

            current_node = ET.SubElement(parent_node, "node", name = child_attr.name, 
                                            extra_info = parser.get_item_description(child_attr.value), 
                                            start_offset = str(start_offset), 
                                            end_offset = str(end_offset),
                                            is_metavar = str(child_attr.is_metavar))
            recurse(child_attr.value, current_node, child_attr.is_array, start_offset if child_attr.relative_offset else add_offset)


    with parser.parse(path) as parsed_file:
        recurse(parent_object = parsed_file, parent_node = root, is_array = False, add_offset = 0)
    
    return root

def save_kaitai_to_xml(kaitai_format: str, input_path: Union[str, Path], output_path: Union[str, Path]) -> None:
    """Save an XML representation of the given file to the given output path.
    
    Args:
        kaitai_format:
            The Kaitai format used to parse the given file.

        input_path:
            Path to input file to be parsed.

        output_path:
            Path to output file where XML will be saved to.
    """
    m = model.Model()
    format = {"kaitai_format": kaitai_format}
    parser = m.get_parser(**format)
    
    xml_representation = kaitai_to_xml(parser, input_path)
    
    with open(output_path, "w") as o:
        o.write(xml_to_str(xml_representation))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A utility to output an XML representation of a binary file using Kaitai')
    parser.add_argument('-f', '--file', action="store", required = True, help='Path to binary file')
    parser.add_argument('-kf', '--kaitai-format', action="store", required = True, help = "Kaitai format (see list in pytai's usage)")
    parser.add_argument('-o', '--output', action="store", help='Optional: Path to output file (default: Input file\'s path with XML extention)')
    args = parser.parse_args()

    input_path = Path(args.file)
    output_path = args.output
    if output_path is None:
        output_path = input_path.parent / (input_path.stem + ".xml")
    save_kaitai_to_xml(args.kaitai_format, input_path, output_path)
    print(f"Saved to '{output_path}'")
    print(f"If used for validation purposed, please review the output manually since the output relies on the model.")