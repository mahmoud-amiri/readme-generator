import re

class StructureRecognizer:
    def __init__(self, hardware_component):
        self.hardware_component = hardware_component

    def recognize_ports_structure(self, code_lines, patterns):
        for pattern_info in patterns:
            pattern, input_type, description_format, add_method = pattern_info
            for line_no, line in enumerate(code_lines, start=1):
                match = pattern.search(line)
                if match:
                    if 'array' in input_type:
                        size = match.group(1)
                        name = match.group(2)
                    elif input_type in ['parameter', 'localparam']:
                        size = '1'
                        name = match.group(1)
                        default_value = match.group(2)
                    else:
                        size = '1'
                        name = match.group(1)
                    
                    description = description_format.format(size=size.strip() if isinstance(size, str) else size, name=name, default_value=default_value if input_type in ['parameter', 'localparam'] else "")
                    
                    # Pass default_value only for parameters
                    if input_type in ['parameter', 'localparam']:
                        add_method(line_no, name, input_type, size, description, default_value)
                    else:
                        add_method(line_no, name, input_type, size, description)

    def recognize_internal_signals(self, code_lines, patterns):
        for pattern_info in patterns:
            pattern, signal_type, description_format, add_method = pattern_info
            for line_no, line in enumerate(code_lines, start=1):
                match = pattern.search(line)
                if match:
                    if 'multidimensional array' in signal_type:
                        high1, low1 = int(match.group(1)), int(match.group(2))
                        name = match.group(3)
                        high2, low2 = int(match.group(4)), int(match.group(5))

                        # Correct the order if necessary
                        if high1 < low1:
                            high1, low1 = low1, high1
                        if high2 < low2:
                            high2, low2 = low2, high2

                        width = high1 - low1 + 1
                        depth = high2 - low2 + 1

                        description = description_format.format(width=width, depth=depth)
                        add_method(line_no, name, signal_type, (width, depth), description)
                    elif 'array' in signal_type:
                        size = match.group(1)
                        name = match.group(2)
                        description = description_format.format(size=size.strip(), name=name)
                        add_method(line_no, name, signal_type, size, description)
                    else:
                        size = '1'
                        name = match.group(1)
                        description = description_format.format(size=size.strip(), name=name)
                        add_method(line_no, name, signal_type, size, description)







    def recognize_all_structures(self, code_lines):
        ports_patterns = [
            (re.compile(r'\binput\s+(clk|clock|CLK|CLOCK)\s*,'), 'clock', 'input clock', self.hardware_component.add_input),
            (re.compile(r'\binput\s+(rst|reset|RST|RESET)\s*,'), 'reset', 'input reset', self.hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+(clk|clock|CLK|CLOCK)\s*,'), 'clock', 'input clock', self.hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+(rst|reset|RST|RESET)\s*,'), 'reset', 'input reset', self.hardware_component.add_input),

            (re.compile(r'\binput\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input array for <1>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input array for <2>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input for <3>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+reg\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input reg array for <4>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+logic\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input logic array for <5>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+bit\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input bit array for <6>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input wire array for <7>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+reg\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input reg array for <8>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+logic\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input logic array for <9>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+bit\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input bit array for <10>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input wire array for <11>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+reg\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input reg for <12>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+logic\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input logic for <13>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+bit\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input bit for <14>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input wire for <15>', self.hardware_component.add_input),

            (re.compile(r'\boutput\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output array for <16>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output array for <17>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output single bit for <18>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+reg\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output reg for <19>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+logic\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output logic for <20>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+bit\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output bit for <21>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+wire\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output wire for <22>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+reg\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output reg array for <23>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+logic\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output logic array for <24>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+bit\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output bit array for <24>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+wire\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output wire array for <26>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+reg\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output reg array for <27>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+logic\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output logic array for <28>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+bit\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output bit array for <29>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+wire\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output wire array for <30>', self.hardware_component.add_output),

            (re.compile(r'\binout\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'inout array', '{size}-bit inout array for <31>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'inout array', '({size} + 1)-bit inout array for <32>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+(\w+)\s*,'), 'inout single_bit', '{size}-bit inout single bit for <33>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+reg\s+(\w+)\s*,'), 'inout single_bit', '{size}-bit inout reg for <34>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+logic\s+(\w+)\s*,'), 'inout single_bit', '{size}-bit inout logic for <35>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+bit\s+(\w+)\s*,'), 'inout single_bit', '{size}-bit inout bit for <36>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+wire\s+(\w+)\s*,'), 'inout single_bit', '{size}-bit inout wire for <37>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+reg\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'inout array', '{size}-bit inout reg array for <38>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+logic\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'inout array', '{size}-bit inout logic array for <39>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+bit\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'inout array', '{size}-bit inout bit array for <40>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+wire\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'inout array', '{size}-bit inout wire array for <41>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+reg\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'inout array', '({size} + 1)-bit inout reg array for <42>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+logic\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'inout array', '({size} + 1)-bit inout logic array for <43>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+bit\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'inout array', '({size} + 1)-bit inout bit array for <44>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+wire\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'inout array', '({size} + 1)-bit inout wire array for <45>', self.hardware_component.add_inout),
            (re.compile(r'\bparameter\s+(\w+)\s*=\s*([^\s;]+)\s*[;,]?\s*\)?'), 'parameter', 'parameter {name} with default value {default_value}', self.hardware_component.add_parameter)
        
        ]
        self.recognize_ports_structure(code_lines, ports_patterns)

        internal_signal_patterns = [
            # Internal signal patterns
            (re.compile(r'\breg\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*[;,]'), 'reg array', '{size}-bit reg array', self.hardware_component.add_internal_signal),
            (re.compile(r'\breg\s+\[([^\]]+):0\]\s+(\w+)\s*[;,]'), 'reg array', '({size} + 1)-bit reg array', self.hardware_component.add_internal_signal),
            (re.compile(r'\breg\s+(\w+)\s*[;,]'), 'reg single_bit', '{size}-bit reg', self.hardware_component.add_internal_signal),
            
            (re.compile(r'\bwire\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*[;,]'), 'wire array', '{size}-bit wire array', self.hardware_component.add_internal_signal),
            (re.compile(r'\bwire\s+\[([^\]]+):0\]\s+(\w+)\s*[;,]'), 'wire array', '({size} + 1)-bit wire array', self.hardware_component.add_internal_signal),
            (re.compile(r'\bwire\s+(\w+)\s*[;,]'), 'wire single_bit', '{size}-bit wire', self.hardware_component.add_internal_signal),

            (re.compile(r'\blogic\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*[;,]'), 'logic array', '{size}-bit logic array', self.hardware_component.add_internal_signal),
            (re.compile(r'\blogic\s+\[([^\]]+):0\]\s+(\w+)\s*[;,]'), 'logic array', '({size} + 1)-bit logic array', self.hardware_component.add_internal_signal),
            (re.compile(r'\blogic\s+(\w+)\s*[;,]'), 'logic single_bit', '{size}-bit logic', self.hardware_component.add_internal_signal),

            (re.compile(r'\bbit\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*[;,]'), 'bit array', '{size}-bit bit array', self.hardware_component.add_internal_signal),
            (re.compile(r'\bbit\s+\[([^\]]+):0\]\s+(\w+)\s*[;,]'), 'bit array', '({size} + 1)-bit bit array', self.hardware_component.add_internal_signal),
            (re.compile(r'\bbit\s+(\w+)\s*[;,]'), 'bit single_bit', '{size}-bit bit', self.hardware_component.add_internal_signal),

            (re.compile(r'\bwire\s+reg\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*[;,]'), 'wire reg array', '{size}-bit wire reg array', self.hardware_component.add_internal_signal),
            (re.compile(r'\bwire\s+reg\s+\[([^\]]+):0\]\s+(\w+)\s*[;,]'), 'wire reg array', '({size} + 1)-bit wire reg array', self.hardware_component.add_internal_signal),
            (re.compile(r'\bwire\s+reg\s+(\w+)\s*[;,]'), 'wire reg single_bit', '{size}-bit wire reg', self.hardware_component.add_internal_signal),
           
            (re.compile(r'\breg\s+\[(\d+):(\d+)\]\s+(\w+)\s*\[(\d+):(\d+)\]\s*;'), 'multidimensional array', '{width}x{depth}-bit reg array', self.hardware_component.add_internal_signal),
            (re.compile(r'\bwire\s+\[(\d+):(\d+)\]\s+(\w+)\s*\[(\d+):(\d+)\]\s*;'), 'multidimensional array', '{width}x{depth}-bit wire array', self.hardware_component.add_internal_signal),
            (re.compile(r'\blogic\s+\[(\d+):(\d+)\]\s+(\w+)\s*\[(\d+):(\d+)\]\s*;'), 'multidimensional array', '{width}x{depth}-bit logic array', self.hardware_component.add_internal_signal),
            (re.compile(r'\bbit\s+\[(\d+):(\d+)\]\s+(\w+)\s*\[(\d+):(\d+)\]\s*;'), 'multidimensional array', '{width}x{depth}-bit bit array', self.hardware_component.add_internal_signal),
        ]

        self.recognize_internal_signals(code_lines, internal_signal_patterns)

        self.recognize_signed_registers(code_lines)

    def recognize_signed_registers(self, code_lines):
        patterns = [
            (re.compile(r'\breg\s+signed\s+\[([^\]]+):0\]\s+(\w+)\s*[;,]'), 'reg signed array', 'signed ({size} + 1)-bit reg array for {name}'),
            (re.compile(r'\bwire\s+signed\s+\[([^\]]+):0\]\s+(\w+)\s*[;,]'), 'wire signed array', 'signed ({size} + 1)-bit wire array for {name}'),
            (re.compile(r'\blogic\s+signed\s+\[([^\]]+):0\]\s+(\w+)\s*[;,]'), 'logic signed array', 'signed ({size} + 1)-bit logic array for {name}'),
            (re.compile(r'\bbit\s+signed\s+\[([^\]]+):0\]\s+(\w+)\s*[;,]'), 'bit signed array', 'signed ({size} + 1)-bit bit array for {name}')
        ]

        for pattern, signal_type, description_format in patterns:
            for line_no, line in enumerate(code_lines, start=1):
                match = pattern.search(line)
                if match:
                    size = match.group(1)
                    name = match.group(2)
                    description = description_format.format(size=size.strip(), name=name)
                    self.hardware_component.add_internal_signal(line_no, name, signal_type, size, description)
