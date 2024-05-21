import re

def extract_state_encodings(verilog_code):
    state_encoding_pattern = re.compile(r'localparam\s+(\w+)\s*=\s*3\'b(\d+);')
    state_encodings = state_encoding_pattern.findall(verilog_code)
    states = {name: {'code': code, 'transitions': {}, 'actions': []} for name, code in state_encodings}
    return states

def extract_state_transitions(verilog_code, states):
    transition_pattern = re.compile(r'case\s*\(\s*state\s*\)\s*(.+?)endcase', re.DOTALL)
    state_block_pattern = re.compile(r'(\w+):\s*begin\s*(.+?)(?=\w+:|$)', re.DOTALL)
    if_transition_pattern = re.compile(r'if\s*\((.+?)\)\s*begin')
    next_state_pattern = re.compile(r'next_state\s*=\s*(\w+);')

    transition_blocks = transition_pattern.findall(verilog_code)
    if not transition_blocks:
        return states

    for block in transition_blocks:
        state_transitions = state_block_pattern.findall(block)
        for state, code in state_transitions:
            transitions = {}
            current_condition = 'default'
            lines = code.split('\n')
            for line in lines:
                line = line.strip()
                if 'if' in line:
                    condition_match = if_transition_pattern.search(line)
                    if condition_match:
                        current_condition = condition_match.group(1)
                next_state_match = next_state_pattern.search(line)
                if next_state_match:
                    next_state = next_state_match.group(1)
                    transitions[current_condition] = next_state
                    current_condition = 'default'  # Reset for next transition
            states[state]['transitions'] = transitions

    return states

def extract_actions(verilog_code, states):
    output_logic_pattern = re.compile(
        r'always @(?:posedge clk or posedge reset)\s*begin\s*if\s*\(reset\)\s*begin\s*(.+?)end\s*else\s*begin\s*(.+?)end',
        re.DOTALL
    )
    state_block_pattern = re.compile(r'(\w+):\s*begin\s*(.+?)end', re.DOTALL)
    action_pattern = re.compile(r'(\w+)\s*<=\s*(\d);')

    output_logic_match = output_logic_pattern.search(verilog_code)
    if not output_logic_match:
        return states

    state_actions = state_block_pattern.findall(output_logic_match.group(2))
    for state, code in state_actions:
        lines = code.split('\n')
        for line in lines:
            line = line.strip()
            action_match = action_pattern.search(line)
            if action_match:
                signal, value = action_match.groups()
                if value == '1':
                    states[state]['actions'].append(signal)
    return states

def generate_documentation(states):
    documentation = "# State Machine Documentation\n\n## State Machine (if applicable)\n\n"
    documentation += "| State Name | Description           | Transitions To | Conditions for Transition       | Actions Performed                |\n"
    documentation += "|------------|-----------------------|----------------|---------------------------------|----------------------------------|\n"
    
    for state, info in states.items():
        description = f"Description for {state}"
        transitions_to = ", ".join(set(info['transitions'].values()))
        conditions = ", ".join([f"{cond} -> {next_state}" for cond, next_state in info['transitions'].items()])
        actions = ", ".join(info['actions'])
        documentation += f"| {state} | {description} | {transitions_to} | {conditions} | {actions} |\n"
    
    return documentation

def main(file_path):
    with open(file_path, 'r') as file:
        verilog_code = file.read()
    
    states = extract_state_encodings(verilog_code)
    states = extract_state_transitions(verilog_code, states)
    states = extract_actions(verilog_code, states)
    documentation = generate_documentation(states)
    
    return documentation

if __name__ == "__main__":
    file_path = 'state_machine.v'  # Replace with the path to your Verilog file
    documentation = main(file_path)
    print(documentation)
