import pprint
import re

class HardwareComponent:
    def __init__(self, name="", description=""):
        self.component = {
            "name": name,
            "parameters": [],
            "inputs": [],
            "outputs": [],
            "inouts": [],
            "internal_signals": [],
            "submodules": [],
            "statemachines": [],
            "description": description
        }
    
    def print_component(self):
        pprint.pprint(self.component)

    def add_parameter(self, line_no, name, type, size, comment, default_value):
        parameter_dict = {
            "line_no": line_no,
            "name": name,
            "type": type,
            "size": size,
            "comment": comment,
            "default_value": default_value
        }
        if self._check_parameter_dict(parameter_dict):
            self.component["parameters"].append(parameter_dict)
        else:
            print(f"Invalid parameter: {parameter_dict}")

    def _check_parameter_dict(self, parameter_dict):
        # Add any specific checks for parameters if needed
        return True
    
    def remove_parameter(self, line_no):
        parameter_to_remove = next((param for param in self.component["parameters"] if param["line_no"] == line_no), None)
        if parameter_to_remove:
            self.component["parameters"].remove(parameter_to_remove)
        else:
            print(f"Parameter with line number '{line_no}' does not exist.")


    def add_input(self, line_no, name, type, size, comment):
        input_dict = {
            "line_no": line_no,
            "name": name,
            "type": type,
            "size": size,
            "comment": comment
        }
        if self._check_input_dict(input_dict):
            self.component["inputs"].append(input_dict)
        else:
            print(f"Invalid input: size '{size}' is not allowed.")

    def _check_input_dict(self, input_dict):
        pattern = re.compile(r'.*-\s*1')
        if pattern.match(str(input_dict["size"])):
            return False
        
        if input_dict["size"] == 1 and input_dict["name"] == ("rst" or "RST" or "reset" or "RESET") and input_dict["type"] != "reset":
            return False
        
        if input_dict["size"] == 1 and input_dict["name"] == ("clk" or "CLK" or "clock" or "CLOCK") and input_dict["type"] != "clock":
            return False
        
        return True
    
    def remove_input(self, line_no):
        input_to_remove = next((input for input in self.component["inputs"] if input["line_no"] == line_no), None)
        if input_to_remove:
            self.component["inputs"].remove(input_to_remove)
        else:
            print(f"Input with line number '{line_no}' does not exist.")

    def add_output(self, line_no, name, type, size, comment):
        output_dict = {
            "line_no": line_no,
            "name": name,
            "type": type,
            "size": size,
            "comment": comment
        }
        if self._check_output_dict(output_dict):
            self.component["outputs"].append(output_dict)
        else:
            print(f"Invalid output: size '{size}' is not allowed.")

    def _check_output_dict(self, output_dict):
        pattern = re.compile(r'.*-\s*1')
        if pattern.match(str(output_dict["size"])):
            return False
        return True
    
    def remove_output(self, line_no):
        output_to_remove = next((output for output in self.component["outputs"] if output["line_no"] == line_no), None)
        if output_to_remove:
            self.component["outputs"].remove(output_to_remove)
        else:
            print(f"Output with line number '{line_no}' does not exist.")

    def add_inout(self, line_no, name, type, size, comment):
        inout_dict = {
            "line_no": line_no,
            "name": name,
            "type": type,
            "size": size,
            "comment": comment
        }
        if self._check_inout_dict(inout_dict):
            self.component["inouts"].append(inout_dict)
        else:
            print(f"Invalid inouts: size '{size}' is not allowed.")

    def _check_inout_dict(self, inout_dict):
        pattern = re.compile(r'.*-\s*1')
        if pattern.match(str(inout_dict["size"])):
            return False
        return True
    
    def remove_inout(self, line_no):
        inout_to_remove = next((inout for inout in self.component["inouts"] if inout["line_no"] == line_no), None)
        if inout_to_remove:
            self.component["inouts"].remove(inout_to_remove)
        else:
            print(f"Inout with line number '{line_no}' does not exist.")

    def add_internal_signal(self, line_no, name, type, size, comment):
        signal_dict = {
            "line_no": line_no,
            "name": name,
            "type": type,
            "size": size,
            "comment": comment
        }
        self.component["internal_signals"].append(signal_dict)

    def remove_internal_signal(self, line_no):
        signal_to_remove = next((signal for signal in self.component["internal_signals"] if signal["line_no"] == line_no), None)
        if signal_to_remove:
            self.component["internal_signals"].remove(signal_to_remove)
        else:
            print(f"Internal signal with line number '{line_no}' does not exist.")

    def add_submodule(self, line_no_start, line_no_end, inputs, outputs, inouts, parameters, name, comment):
        submodule_dict = {
            "line_no_start": line_no_start,
            "line_no_end": line_no_end,
            "inputs": inputs,
            "outputs": outputs,
            "inouts": inouts,
            "parameters": parameters,
            "name": name,
            "comment": comment
        }
        self.component["submodules"].append(submodule_dict)

    def remove_submodule(self, line_no_start):
        submodule_to_remove = next((submodule for submodule in self.component["submodules"] if submodule["line_no_start"] == line_no_start), None)
        if submodule_to_remove:
            self.component["submodules"].remove(submodule_to_remove)
        else:
            print(f"Submodule with starting line number '{line_no_start}' does not exist.")

    def add_statemachine(self, line_no_start, line_no_end, name, comment, states, transitions):
        statemachine_dict = {
            "line_no_start": line_no_start,
            "line_no_end": line_no_end,
            "name": name,
            "comment": comment,
            "states": states,
            "transitions": transitions
        }
        self.component["statemachines"].append(statemachine_dict)

    def remove_statemachine(self, line_no_start):
        statemachine_to_remove = next((statemachine for statemachine in self.component["statemachines"] if statemachine["line_no_start"] == line_no_start), None)
        if statemachine_to_remove:
            self.component["statemachines"].remove(statemachine_to_remove)
        else:
            print(f"Statemachine with starting line number '{line_no_start}' does not exist.")

    def get_component(self):
        return self.component
    
    def update_comments_in_dict(self, code_lines):
        component = self.get_component()
        
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
        component = self.get_component()

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

    def update_size_in_comment(self):
        pattern = re.compile(r'\((\d+)\s*\+\s*1\)-bit')
        
        for key in ["inputs", "outputs", "inouts", "internal_signals"]:
            elements = self.component.get(key, [])
            for element in elements:
                comment = element.get("comment", "")
                match = pattern.search(comment)
                if match:
                    base_number = int(match.group(1))
                    new_size = base_number + 1
                    new_comment = pattern.sub(f'{new_size}-bit', comment)
                    element["comment"] = new_comment
                    element["size"] = new_size
