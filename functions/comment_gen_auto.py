import pprint
import re
class HardwareComponent:
    def __init__(self, name="", description=""):
        self.component = {
            "name": name,
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

    def add_input(self, line_no, name, type, size, comment):
        input_dict = {
            "line_no": line_no,
            "name": name,
            "type": type,
            "size": size,
            "comment": comment
        }
        self.component["inputs"].append(input_dict)
    
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
        self.component["outputs"].append(output_dict)

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
        self.component["inouts"].append(inout_dict)

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

# Example usage:
hardware_component = HardwareComponent(name="ExampleComponent", description="This is an example hardware component.")

# Adding inputs
hardware_component.add_input(1, "input1", "digital", "32-bit", "Comment for input1")
hardware_component.add_input(2, "input2", "analog", "16-bit", "Comment for input2")

# Adding outputs
hardware_component.add_output(1, "output1", "digital", "32-bit", "Comment for output1")

# Adding inouts
hardware_component.add_inout(1, "inout1", "analog", "16-bit", "Comment for inout1")

# Adding internal signals
hardware_component.add_internal_signal(1, "signal1", "digital", "32-bit", "Comment for signal1")

# Adding submodules
hardware_component.add_submodule(1, 10, "input_set1", "output_set1", "inout_set1", "param_set1", "submodule1", "Comment for submodule1")

# Adding statemachines
hardware_component.add_statemachine(1, 20, "statemachine1", "Comment for statemachine1", "states1", "transitions1")

# Removing inputs
hardware_component.remove_input(1)

# Removing outputs
hardware_component.remove_output(1)

# Removing inouts
hardware_component.remove_inout(1)

# Removing internal signals
hardware_component.remove_internal_signal(1)

# Removing submodules
hardware_component.remove_submodule(1)

# Removing statemachines
hardware_component.remove_statemachine(1)

print(hardware_component.get_component())

################################################################
import re

def parse_verilog_module(verilog_code):
    # Define regex patterns to capture module name, parameters, and ports
    module_pattern = r"(module\s+\w+\s*#\([^)]*\)\s*\([^)]*\);)"
    
    match = re.search(module_pattern, verilog_code, re.DOTALL)
    
    if match:
        module_definition = match.group(1).strip()
        remaining_code = verilog_code.replace(module_definition, "").strip()
        
        return {
            "module_definition": module_definition,
            "remaining_code": remaining_code
        }
    else:
        return None

# Example Verilog code
verilog_code = """
module my_module #(
    parameter WIDTH = 8,
    parameter HEIGHT = 16
) (
    input clk,
    input rst,
    output [WIDTH-1:0] data_out
);

// Some other code
wire a;
assign a = clk & rst;
"""

result = parse_verilog_module(verilog_code)
if result:
    print(f"Module Definition:\n{result['module_definition']}")
    print(f"\nRemaining Code:\n{result['remaining_code']}")
else:
    print("No module definition found.")
###############################################################################

import re

def extract_module_parameters(code_text):
    # Regex pattern to match module definition with parameters
    pattern = re.compile(r'module\s+(\w+)\s*#\((.*?)\)\s*', re.DOTALL)
    
    match = pattern.search(code_text)
    if not match:
        return [], code_text, None
    
    module_name = match.group(1)
    params_text = match.group(2).strip()
    
    if not params_text:
        parameters = []
    else:
        # Split the parameters by commas and strip spaces
        parameters = [param.strip() for param in params_text.split(',')]
    
    # Remove the matched part from the original code text
    remaining_text = pattern.sub('', code_text, count=1).strip()
    
    return parameters, remaining_text, module_name

# Example usage
code_text = """
module complex_module #(
    parameter WIDTH = 8, 
    parameter DEPTH = 16
    )
    // Other module code
endmodule
"""

parameters, remaining_text, module_name = extract_module_parameters(code_text)
print("Parameters:", parameters)
print("Remaining Text:", remaining_text)
print("Module Name:", module_name)

##############################################################################
#import re
#import os
#
## Updated Regex Patterns for Verilog and VHDL to handle parameters/generics and parameterized dimensions
#regex_patterns = {
#    'verilog': {
#        'parameter': re.compile(r'\bparameter\s+(\w+)\s*=\s*([\w\'\-\+\*/\s]+)\s*[,;]?'),
#        'input': re.compile(r'\binput\s+(wire\s+)?(\[.+?\]\s*)?(\w+)\s*[,;]?'),
#        'output': re.compile(r'\boutput\s+(reg\s+)?(\[.+?\]\s*)?(\w+)\s*[,;]?'),
#        'inout': re.compile(r'\binout\s+(wire\s+)?(\[.+?\]\s*)?(\w+)\s*[,;]?')
#    },
#    'vhdl': {
#        'generic': re.compile(r'(\w+)\s*:\s*(integer|real|boolean|std_logic|std_logic_vector|positive|natural)\s*:=\s*([\w\'\-\+\*/\s]+)\s*;?'),
#        'input': re.compile(r'(\w+)\s*:\s*in\s*((std_logic_vector\(.+?\s+downto\s+\d+\))|(std_logic))\s*;?'),
#        'output': re.compile(r'(\w+)\s*:\s*out\s*((std_logic_vector\(.+?\s+downto\s+\d+\))|(std_logic))\s*;?'),
#        'inout': re.compile(r'(\w+)\s*:\s*inout\s*((std_logic_vector\(.+?\s+downto\s+\d+\))|(std_logic))\s*;?')
#    }
#}
#
#def generate_comment_verilog(match):
#    direction = match.group(0).split()[0]
#    width_expr = match.group(2)
#    signal = match.group(3)
#    clock_signals = ['clk', 'clock']
#    reset_signals = ['reset', 'rst']
#
#    if any(clock in signal.lower() for clock in clock_signals):
#        description = "clock signal"
#    elif any(reset in signal.lower() for reset in reset_signals):
#        description = "reset signal"
#    else:
#        width = "parameterized width" if width_expr else "1-bit"
#        description = f"{width} {direction} signal for {signal}"
#    return f"{match.group(0).strip()} // {description}"
#
#def generate_comment_vhdl(match):
#    direction = "in" if "in" in match.group(0) else "out" if "out" in match.group(0) else "inout"
#    signal = match.group(1)
#    type_spec = match.group(2)
#    clock_signals = ['clk', 'clock']
#    reset_signals = ['reset', 'rst']
#
#    if any(clock in signal.lower() for clock in clock_signals):
#        description = "clock signal"
#    elif any(reset in signal.lower() for reset in reset_signals):
#        description = "reset signal"
#    else:
#        if "std_logic_vector" in type_spec:
#            width = "parameterized width"
#        else:
#            width = "1-bit"
#        description = f"{width} {direction} signal for {signal}"
#    return f"{match.group(0).strip()} -- {description}"
#
#def generate_comment_parameter(match, language):
#    parameter_name = match.group(1)
#    parameter_value = match.group(3) if language == 'vhdl' else match.group(2)
#    description = f"Parameter {parameter_name} with default value {parameter_value}"
#    comment_symbol = '--' if language == 'vhdl' else '//'
#    return f"{match.group(0).strip()} {comment_symbol} {description}"
#
#def determine_language(file_path):
#    _, file_extension = os.path.splitext(file_path)
#    if file_extension in ['.v', '.sv']:
#        return 'verilog'
#    elif file_extension in ['.vhdl', '.vhd']:
#        return 'vhdl'
#    else:
#        raise ValueError("Unsupported file extension. Please provide a Verilog (.v, .sv) or VHDL (.vhdl, .vhd) file.")
#
#def add_comments_to_hdl(file_path):
#    language = determine_language(file_path)
#
#    try:
#        with open(file_path, 'r') as file:
#            code = file.read()
#    except FileNotFoundError:
#        return "File not found. Please check the file path and try again."
#    except Exception as e:
#        return f"An error occurred: {e}"
#
#    lines = code.splitlines()
#    commented_code = []
#
#    for line in lines:
#        if re.search(r'//|--', line):  # If there's already a comment, keep the line as is
#            commented_code.append(line)
#            continue
#
#        processed = False
#        for direction in ['parameter', 'generic', 'input', 'output', 'inout']:
#            if direction in regex_patterns[language]:
#                pattern = regex_patterns[language][direction]
#                if direction == 'parameter' or direction == 'generic':
#                    new_line = pattern.sub(lambda m: generate_comment_parameter(m, language), line)
#                else:
#                    new_line = pattern.sub(generate_comment_verilog if language == 'verilog' else generate_comment_vhdl, line)
#                if new_line != line:
#                    line = new_line
#                    processed = True
#                    break
#        commented_code.append(line)
#
#    new_content = '\n'.join(commented_code)
#    with open(file_path, 'w') as file:
#        file.write(new_content)
#
#    return f"Comments added and file '{file_path}' has been updated."
#
#
#
## Usage example
#file_path = "../test/comment_test.v"  # Adjust the file path and extension as needed
#print(add_comments_to_hdl(file_path))
#
## Usage example
#file_path = "../test/comment_test.vhd"  # Adjust the file path and extension as needed
#print(add_comments_to_hdl(file_path))

#################################################################
