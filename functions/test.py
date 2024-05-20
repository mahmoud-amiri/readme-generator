from structure_recognizer import StructureRecognizer
from hardware_component import HardwareComponent
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

    def update_comments_in_dict(self, code_lines):
        component = self.hardware_component.get_component()
        
        for key in ["inputs", "outputs", "inouts", "internal_signals"]:
            elements = component.get(key, [])
            for element in elements:
                line_no = element.get("line_no")
                if line_no is not None and line_no <= len(code_lines):
                    line_content = code_lines[line_no - 1]
                    comment_match = re.search(r'//\s*(.*)', line_content)
                    if comment_match:
                        existing_comment = comment_match.group(1).strip()
                        element["comment"] = existing_comment

    def remove_duplicate_line_entries(self):
        component = self.hardware_component.get_component()

        for key in ["inputs", "outputs", "inouts", "internal_signals"]:
            elements = component.get(key, [])
            seen_lines = set()
            unique_elements = []
            for element in elements:
                line_no = element.get("line_no")
                if line_no not in seen_lines:
                    unique_elements.append(element)
                    seen_lines.add(line_no)
            component[key] = unique_elements

    def generate_port_description_block(self):
        component = self.hardware_component.get_component()
        port_lines = ["//#### Ports", 
                      "//| Port Name    | Direction | Width | Description                               |",
                      "//|--------------|-----------|-------|-------------------------------------------|"]

        for key, direction in [("inputs", "input"), ("outputs", "output"), ("inouts", "inout")]:
            for element in component.get(key, []):
                name = element.get("name", "")
                width = element.get("size", "")
                description = element.get("comment", "No description")
                port_lines.append(f"//| `{name}`{' ' * (12 - len(name))}| {direction}{' ' * (9 - len(direction))}| {width}{' ' * (5 - len(str(width)))}| {description}{' ' * (42 - len(description))}|")
        
        return "\n".join(port_lines) + "\n"

    def add_comments_to_code(self, output_path):
        code_lines = self.read_verilog_code()
        self.update_comments_in_dict(code_lines)
        self.remove_duplicate_line_entries()

        # Generate port description block and insert at the top
        port_description_block = self.generate_port_description_block()
        code_lines.insert(0, port_description_block)

        component = self.hardware_component.get_component()
        for key in ["inputs", "outputs", "inouts", "internal_signals"]:
            elements = component.get(key, [])
            for element in elements:
                line_no = element.get("line_no")
                comment = element.get("comment")
                if line_no is not None and comment:
                    line_content = code_lines[line_no - 1]
                    if '//' not in line_content:
                        code_lines[line_no - 1] = line_content.rstrip() + f" // {comment}\n"

        with open(output_path, 'w') as file:
            file.writelines(code_lines)

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
analyzer.add_comments_to_code(output_path)
