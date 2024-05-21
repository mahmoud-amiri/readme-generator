from structure_recognizer import StructureRecognizer
from hardware_component import HardwareComponent
from VerilogCommentWriter import VerilogCommentWriter
import pprint
import re

class VerilogAnalyzer:
    def __init__(self, verilog_path):
        self.verilog_path = verilog_path
        self.hardware_component = HardwareComponent()
        self.recognizer = StructureRecognizer(self.hardware_component)

    def read_verilog_code(self):
        with open(self.verilog_path, 'r') as file:
            code_lines = file.readlines()
        return code_lines

    def analyze(self):
        code_lines = self.read_verilog_code()
        self.recognizer.recognize_all_structures(code_lines)

    def print_results(self):
        self.hardware_component.print_component()
        print(f"done")

    def get_component_dict(self):
        return self.hardware_component.get_component()

# Example usage:
verilog_path = "../test/comment_test.v"
output_path = "../test/comment_test_copy.v"

analyzer = VerilogAnalyzer(verilog_path)
analyzer.analyze()
analyzer.print_results()

# To get the component dictionary
component_dict = analyzer.get_component_dict()
pprint.pprint(component_dict)

# To add comments to the Verilog code and write it to a new file
code_lines = analyzer.read_verilog_code()
analyzer.hardware_component.update_comments_in_dict(code_lines)
analyzer.hardware_component.remove_duplicate_line_entries()
analyzer.hardware_component.update_size_in_comment()
comment_writer = VerilogCommentWriter(analyzer.hardware_component)
comment_writer.add_comments_to_code(code_lines, output_path)
