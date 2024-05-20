class VerilogCommentWriter:
    def __init__(self, hardware_component):
        self.hardware_component = hardware_component

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


        # Generate port description block and insert at the top
        port_description_block = self.generate_port_description_block()
        code_lines.insert(0, port_description_block)

        with open(output_path, 'w') as file:
            file.writelines(code_lines)