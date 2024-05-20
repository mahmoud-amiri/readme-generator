import re

class StructureRecognizer:
    def __init__(self, hardware_component):
        self.hardware_component = hardware_component

    def recognize_structure(self, code_lines, patterns):
        for pattern_info in patterns:
            pattern, input_type, description_format, add_method = pattern_info
            for line_no, line in enumerate(code_lines, start=1):
                match = pattern.search(line)
                if match:
                    size = match.group(1) if len(match.groups()) > 1 else '1'
                    name = match.group(len(match.groups()))
                    description = description_format.format(size=size.strip() if isinstance(size, str) else size)
                    add_method(line_no, name, input_type, size, description)

    def recognize_all_structures(self, code_lines):
        patterns = [
            (re.compile(r'\binput\s+(clk|clock|CLK|CLOCK)\s*,'), 'clock', 'input clock', self.hardware_component.add_input),
            (re.compile(r'\binput\s+(rst|reset|RST|RESET)\s*,'), 'reset', 'input reset', self.hardware_component.add_input),
            (re.compile(r'\binput\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input array for <1>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input array for <2>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input for <3>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+reg\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input reg array for <4>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+logic\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input logic array for <5>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+bit\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input bit array for <6>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input wire array for <7>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+reg\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '{size}-bit input reg array for <8>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+logic\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '{size}-bit input logic array for <9>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+bit\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '{size}-bit input bit array for <10>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size}+1)-bit input wire array for <11>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+reg\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input reg for <12>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+logic\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input logic for <13>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+bit\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input bit for <14>', self.hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input wire for <15>', self.hardware_component.add_input),



            (re.compile(r'\boutput\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output array for <16>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output array for <17>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output single bit', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+reg\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output reg  for <20>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+logic\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output logic  for <21>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+bit\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output bit  for <22>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+wire\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output wire  for <23>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+reg\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output reg array for <18>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+logic\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output logic array for <24>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+bit\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output bit array for <25>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+wire\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output wire array for <26>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+reg\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output reg array for <19>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+logic\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output logic array for <27>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+bit\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output bit array for <28>', self.hardware_component.add_output),
            (re.compile(r'\boutput\s+wire\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output wire array for <29>', self.hardware_component.add_output),

            (re.compile(r'\binout\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'inout array', '{size}-bit inout array for <30>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'inout array', '({size} + 1)-bit inout array for <31>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+(\w+)\s*,'), 'inout single_bit', '{size}-bit inout single bit', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+reg\s+(\w+)\s*,'), 'inout single_bit', '{size}-bit inout reg  for <32>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+logic\s+(\w+)\s*,'), 'inout single_bit', '{size}-bit inout logic  for <33>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+bit\s+(\w+)\s*,'), 'inout single_bit', '{size}-bit inout bit  for <34>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+wire\s+(\w+)\s*,'), 'inout single_bit', '{size}-bit inout wire  for <35>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+reg\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'inout array', '{size}-bit inout reg array for <36>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+logic\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'inout array', '{size}-bit inout logic array for <37>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+bit\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'inout array', '{size}-bit inout bit array for <38>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+wire\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'inout array', '{size}-bit inout wire array for <39>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+reg\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'inout array', '({size} + 1)-bit inout reg array for <40>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+logic\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'inout array', '({size} + 1)-bit inout logic array for <41>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+bit\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'inout array', '({size} + 1)-bit inout bit array for <42>', self.hardware_component.add_inout),
            (re.compile(r'\binout\s+wire\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'inout array', '({size} + 1)-bit inout wire array for <43>', self.hardware_component.add_inout)
        ]
        self.recognize_structure(code_lines, patterns)




