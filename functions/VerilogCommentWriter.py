class VerilogCommentWriter:
    def __init__(self, hardware_component):
        self.hardware_component = hardware_component

    def generate_port_description_block(self):
        component = self.hardware_component.get_component()
        port_lines = ["//",
                      "//",
                      "//#### Ports", 
                      "//| Port Name    | Direction | Width | Description                               |",
                      "//|--------------|-----------|-------|-------------------------------------------|"]

        for key, direction in [("inputs", "input"), ("outputs", "output"), ("inouts", "inout")]:
            for element in component.get(key, []):
                name = element.get("name", "")
                width = element.get("size", "")
                description = element.get("comment", "No description")
                port_lines.append(f"//| `{name}`{' ' * (12 - len(name))}| {direction}{' ' * (9 - len(direction))}| {width}{' ' * (5 - len(str(width)))}| {description}{' ' * (42 - len(description))}|")
        
        return "\n".join(port_lines) + "\n"

    def generate_parameter_description_block(self):
        component = self.hardware_component.get_component()
        param_lines = ["//",
                      "//",
                      "//#### Parameters",
                       "//| Parameter Name | Default Value | Description                               |",
                       "//|----------------|---------------|-------------------------------------------|"]

        for element in component.get("parameters", []):
            name = element.get("name", "")
            default_value = element.get("default_value", "")
            description = element.get("comment", "No description")
            param_lines.append(f"//| `{name}`{' ' * (16 - len(name))}| {default_value}{' ' * (13 - len(str(default_value)))}| {description}{' ' * (42 - len(description))}|")

        return "\n".join(param_lines) + "\n"

    def generate_internal_signal_description_block(self):
        component = self.hardware_component.get_component()
        signal_lines = ["//",
                      "//",
                      "//#### Internal Signals",
                        "//| Signal Name    | Width | Description                               |",
                        "//|----------------|-------|-------------------------------------------|"]

        for element in component.get("internal_signals", []):
            name = element.get("name", "")
            width = element.get("size", "")
            description = element.get("comment", "No description")
            signal_lines.append(f"//| `{name}`{' ' * (16 - len(name))}| {width}{' ' * (5 - len(str(width)))}| {description}{' ' * (42 - len(description))}|")

        return "\n".join(signal_lines) + "\n"

    def add_comments_to_code(self, code_lines, output_path):
        component = self.hardware_component.get_component()

        for key in ["parameters", "inputs", "outputs", "inouts", "internal_signals"]:
            elements = component.get(key, [])
            for element in elements:
                line_no = element.get("line_no")
                comment = element.get("comment")
                if line_no is not None and comment:
                    line_content = code_lines[line_no - 1]
                    if '//' not in line_content:
                        code_lines[line_no - 1] = line_content.rstrip() + f" // {comment}\n"

        # Generate description blocks and insert at the top
        port_description_block = self.generate_port_description_block()
        parameter_description_block = self.generate_parameter_description_block()
        internal_signal_description_block = self.generate_internal_signal_description_block()

        code_lines.insert(0, "//doc end\n")
        code_lines.insert(0, internal_signal_description_block)
        code_lines.insert(0, parameter_description_block)
        code_lines.insert(0, port_description_block)
        code_lines.insert(0, "//doc init\n")
        with open(output_path, 'w') as file:
            file.writelines(code_lines)