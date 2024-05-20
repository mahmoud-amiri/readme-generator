#import re
#
#def generate_port_table_from_file(file_path):
#    # Determine the file type based on the file extension
#    if file_path.endswith('.v'):
#        file_type = 'verilog'
#    elif file_path.endswith('.vhdl') or file_path.endswith('.vhd'):
#        file_type = 'vhdl'
#    else:
#        raise ValueError("Unsupported file type. Please provide a Verilog (.v) or VHDL (.vhdl/.vhd) file.")
#
#    # Read the file
#    with open(file_path, 'r') as file:
#        code = file.read()
#
#    if file_type == 'verilog':
#        # Regular expression to match Verilog port definitions and their comments
#        port_regex = r"^\s*(input|output|inout)\s+(?:\[(\d+):(\d+)\]\s+)?(\w+)\s*;\s*//\s*(.*)$"
#    else:  # VHDL
#        # Regular expression to match VHDL port definitions and their comments
#        port_regex = r"^\s*(signal)?\s*(\w+)\s*:\s*(in|out|inout)\s+(std_logic|std_logic_vector\((\d+) downto (\d+)\))\s*;\s*--\s*(.*)$"
#
#    # Extract ports and their descriptions
#    ports = re.findall(port_regex, code, re.MULTILINE)
#
#    # Generate table header
#    table = []
#    table.append("//#### Ports")
#    table.append("//| Port Name    | Direction | Width | Description                               |")
#    table.append("//|--------------|-----------|-------|-------------------------------------------|")
#
#    if file_type == 'verilog':
#        for port in ports:
#            direction = port[0]
#            msb = port[1]
#            lsb = port[2]
#            name = port[3]
#            description = port[4]
#
#            if msb and lsb:
#                width = abs(int(msb) - int(lsb)) + 1
#            else:
#                width = 1
#
#            table.append(f"//| `{name}`      | {direction}     | {width}   | {description:<40} |")
#    else:  # VHDL
#        for port in ports:
#            name = port[1]
#            direction = port[2]
#            data_type = port[3]
#            msb = port[4]
#            lsb = port[5]
#            description = port[6]
#
#            if msb and lsb:
#                width = abs(int(msb) - int(lsb)) + 1
#            else:
#                width = 1
#
#            table.append(f"//| `{name}`      | {direction}     | {width}   | {description:<40} |")
#
#    # Return the generated table
#    return "\n".join(table)
#
## Example usage
#file_path = 'path_to_your_file.v'  # Change this to your file path
#table = generate_port_table_from_file(file_path)
#print(table)
#
#
#################################################
#
#
#import re
#
#def generate_parameter_table_from_file(file_path):
#    # Determine the file type based on the file extension
#    if file_path.endswith('.v'):
#        file_type = 'verilog'
#    elif file_path.endswith('.vhdl') or file_path.endswith('.vhd'):
#        file_type = 'vhdl'
#    else:
#        raise ValueError("Unsupported file type. Please provide a Verilog (.v) or VHDL (.vhdl/.vhd) file.")
#
#    # Read the file
#    with open(file_path, 'r') as file:
#        code = file.read()
#
#    if file_type == 'verilog':
#        # Regular expression to match Verilog parameter definitions and their comments
#        parameter_regex = r"^\s*parameter\s+(\w+)\s*=\s*(\d+)\s*;\s*//\s*(.*)$"
#    else:  # VHDL
#        # Regular expression to match VHDL generic parameter definitions and their comments
#        parameter_regex = r"^\s*generic\s*\(\s*(\w+)\s*:\s*integer\s*:=\s*(\d+)\s*;\s*--\s*(.*)$"
#
#    # Extract parameters and their descriptions
#    parameters = re.findall(parameter_regex, code, re.MULTILINE)
#
#    # Generate table header
#    table = []
#    table.append("//#### Parameters")
#    table.append("//| Parameter Name | Default Value | Description                               |")
#    table.append("//|----------------|---------------|-------------------------------------------|")
#
#    for parameter in parameters:
#        name = parameter[0]
#        default_value = parameter[1]
#        description = parameter[2]
#
#        table.append(f"//| `{name}`       | {default_value}            | {description:<40} |")
#
#    # Return the generated table
#    return "\n".join(table)
#
## Example usage
#file_path = 'path_to_your_file.v'  # Change this to your file path
#table = generate_parameter_table_from_file(file_path)
#print(table)
#
#
########################################################################
#
#import re
#
#def generate_signal_table_from_file(file_path):
#    # Determine the file type based on the file extension
#    if file_path.endswith('.v'):
#        file_type = 'verilog'
#    elif file_path.endswith('.vhdl') or file_path.endswith('.vhd'):
#        file_type = 'vhdl'
#    else:
#        raise ValueError("Unsupported file type. Please provide a Verilog (.v) or VHDL (.vhdl/.vhd) file.")
#
#    # Read the file
#    with open(file_path, 'r') as file:
#        code = file.read()
#
#    if file_type == 'verilog':
#        # Regular expression to match Verilog signal definitions and their comments
#        signal_regex = r"^\s*(wire|reg)\s+(?:\[(\d+):(\d+)\]\s+)?(\w+)\s*;\s*//\s*(.*)$"
#    else:  # VHDL
#        # Regular expression to match VHDL signal definitions and their comments
#        signal_regex = r"^\s*signal\s+(\w+)\s*:\s*(std_logic|std_logic_vector\((\d+) downto (\d+)\))\s*;\s*--\s*(.*)$"
#
#    # Extract signals and their descriptions
#    signals = re.findall(signal_regex, code, re.MULTILINE)
#
#    # Generate table header
#    table = []
#    table.append("//#### Internal Signals")
#    table.append("//| Signal Name    | Width | Description                               |")
#    table.append("//|----------------|-------|-------------------------------------------|")
#
#    if file_type == 'verilog':
#        for signal in signals:
#            signal_type = signal[0]
#            msb = signal[1]
#            lsb = signal[2]
#            name = signal[3]
#            description = signal[4]
#
#            if msb and lsb:
#                width = abs(int(msb) - int(lsb)) + 1
#            else:
#                width = 1
#
#            table.append(f"//| `{name}`      | {width}   | {description:<40} |")
#    else:  # VHDL
#        for signal in signals:
#            name = signal[0]
#            data_type = signal[1]
#            msb = signal[2]
#            lsb = signal[3]
#            description = signal[4]
#
#            if msb and lsb:
#                width = abs(int(msb) - int(lsb)) + 1
#            else:
#                width = 1
#
#            table.append(f"//| `{name}`      | {width}   | {description:<40} |")
#
#    # Return the generated table
#    return "\n".join(table)
#
## Example usage
#file_path = 'path_to_your_file.v'  # Change this to your file path
#table = generate_signal_table_from_file(file_path)
#print(table)
#
####################################################
#
#import re
#
#def generate_submodule_table_from_file(file_path):
#    # Determine the file type based on the file extension
#    if file_path.endswith('.v'):
#        file_type = 'verilog'
#    elif file_path.endswith('.vhdl') or file_path.endswith('.vhd'):
#        file_type = 'vhdl'
#    else:
#        raise ValueError("Unsupported file type. Please provide a Verilog (.v) or VHDL (.vhdl/.vhd) file.")
#
#    # Read the file
#    with open(file_path, 'r') as file:
#        code = file.read()
#
#    if file_type == 'verilog':
#        # Regular expression to match Verilog submodule instances and their comments
#        submodule_regex = r"^\s*(\w+)\s+#?\s*\(([^)]*)\)\s*(\w+)\s*;\s*//\s*(.*)$"
#    else:  # VHDL
#        # Regular expression to match VHDL component instances and their comments
#        submodule_regex = r"^\s*(\w+)\s*:\s*entity\s+(\w+\.\w+)\s*(\w+)?\s*(--\s*(.*))?$"
#
#    # Extract submodules and their descriptions
#    submodules = re.findall(submodule_regex, code, re.MULTILINE)
#
#    # Generate table header
#    table = []
#    table.append("//#### Submodules")
#    table.append("//| Submodule Name | Instance Name | Description                               |")
#    table.append("//|----------------|---------------|-------------------------------------------|")
#
#    if file_type == 'verilog':
#        for submodule in submodules:
#            submodule_name = submodule[0]
#            instance_name = submodule[2]
#            description = submodule[3]
#            table.append(f"//| `{submodule_name}`   | `{instance_name}`   | {description:<40} |")
#    else:  # VHDL
#        for submodule in submodules:
#            submodule_name = submodule[1]
#            instance_name = submodule[0]
#            description = submodule[4] if submodule[4] else ""
#            table.append(f"//| `{submodule_name}`   | `{instance_name}`   | {description:<40} |")
#
#    # Return the generated table
#    return "\n".join(table)
#
## Example usage
#file_path = 'path_to_your_file.v'  # Change this to your file path
#table = generate_submodule_table_from_file(file_path)
#print(table)
#