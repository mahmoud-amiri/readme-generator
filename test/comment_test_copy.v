//#### Ports
//| Port Name    | Direction | Width | Description                               |
//|--------------|-----------|-------|-------------------------------------------|
//| `clk`         | input    | 1    | input clock                               |
//| `reset`       | input    | 1    | input reset                               |
//| `threshold`   | input    | WIDTH| WIDTH-bit input array for <1>             |
//| `data_in_ext` | input    | WIDTH| WIDTH-bit input array for <1>             |
//| `instruction` | input    | 31   | (31 + 1)-bit input array for <2>          |
//| `counter`     | input    | DEPTH| DEPTH-bit input reg array for <4>         |
//| `enable`      | input    | DEPTH| DEPTH-bit input logic array for <5>       |
//| `buffer`      | input    | WIDTH| WIDTH-bit input logic array for <5>       |
//| `data_in`     | input    | WIDTH| WIDTH-bit input wire array for <7>        |
//| `write_addr`  | input    | ADDR_WIDTH| ADDR_WIDTH-bit input wire array for <7>   |
//| `temp`        | input    | WIDTH| WIDTH-bit input wire array for <7>        |
//| `mode`        | input    | 3    | 3-bit input reg array for <8>             |
//| `control`     | input    | 7    | 7-bit input reg array for <8>             |
//| `mask`        | input    | 15   | 15-bit input logic array for <9>          |
//| `status`      | input    | 3    | 3-bit input logic array for <9>           |
//| `interrupt`   | input    | 7    | 7-bit input logic array for <9>           |
//| `config`      | input    | 7    | 7-bit input bit array for <10>            |
//| `flag`        | input    | 7    | 7-bit input bit array for <10>            |
//| `cmd`         | input    | 3    | 3-bit input bit array for <10>            |
//| `address`     | input    | 15   | (15+1)-bit input wire array for <11>      |
//| `shift`       | input    | 15   | (15+1)-bit input wire array for <11>      |
//| `stop`        | input    | 1    | 1-bit input bit for <14>                  |
//| `start`       | input    | 1    | 1-bit input wire for <15>                 |
//| `init`        | input    | 1    | 1-bit input wire for <15>                 |
//| `ready`       | input    | 1    | 1-bit input wire for <15>                 |
//| `done`        | input    | 1    | 1-bit input wire for <15>                 |
//| `threshold_out`| output   | WIDTH| WIDTH-bit output array for <16>           |
//| `data_out_ext`| output   | WIDTH| WIDTH-bit output array for <16>           |
//| `result`      | output   | 31   | (31 + 1)-bit output array for <17>        |
//| `stop_ack`    | output   | 1    | 1-bit output bit for <21>                 |
//| `complete`    | output   | 1    | 1-bit output wire for <22>                |
//| `init_done`   | output   | 1    | 1-bit output wire for <22>                |
//| `ready_signal`| output   | 1    | 1-bit output wire for <22>                |
//| `task_done`   | output   | 1    | 1-bit output wire for <22>                |
//| `counter_out` | output   | DEPTH| DEPTH-bit output reg array for <23>       |
//| `status_out`  | output   | DEPTH| DEPTH-bit output logic array for <24>     |
//| `buffer_out`  | output   | WIDTH| WIDTH-bit output logic array for <24>     |
//| `data_out`    | output   | WIDTH| WIDTH-bit output wire array for <26>      |
//| `read_addr`   | output   | ADDR_WIDTH| ADDR_WIDTH-bit output wire array for <26> |
//| `temp_out`    | output   | WIDTH| WIDTH-bit output wire array for <26>      |
//| `mode_out`    | output   | 3    | (3 + 1)-bit output reg array for <27>     |
//| `control_out` | output   | 7    | (7 + 1)-bit output reg array for <27>     |
//| `mask_out`    | output   | 15   | (15 + 1)-bit output logic array for <28>  |
//| `status_flag` | output   | 3    | (3 + 1)-bit output logic array for <28>   |
//| `interrupt_out`| output   | 7    | (7 + 1)-bit output logic array for <28>   |
//| `config_out`  | output   | 7    | (7 + 1)-bit output bit array for <29>     |
//| `error_flag`  | output   | 7    | (7 + 1)-bit output bit array for <29>     |
//| `cmd_out`     | output   | 3    | (3 + 1)-bit output bit array for <29>     |
//| `address_out` | output   | 15   | (15 + 1)-bit output wire array for <30>   |
//| `shift_out`   | output   | 15   | (15 + 1)-bit output wire array for <30>   |
//| `bidir_instruction`| inout    | 31   | (31 + 1)-bit inout array for <32>         |
//| `bidir_start` | inout    | 1    | 1-bit inout wire for <37>                 |
//| `bidir_init`  | inout    | 1    | 1-bit inout wire for <37>                 |
//| `bidir_status`| inout    | DEPTH| DEPTH-bit inout logic array for <39>      |
//| `bidir_data`  | inout    | WIDTH| WIDTH-bit inout wire array for <41>       |
//| `bidir_write_addr`| inout    | ADDR_WIDTH| ADDR_WIDTH-bit inout wire array for <41>  |
//| `bidir_mode`  | inout    | 3    | (3 + 1)-bit inout reg array for <42>      |
//| `bidir_mask`  | inout    | 15   | (15 + 1)-bit inout logic array for <43>   |
//| `bidir_config`| inout    | 7    | (7 + 1)-bit inout bit array for <44>      |
//| `bidir_address`| inout    | 15   | (15 + 1)-bit inout wire array for <45>    |
module ExampleModule #(
    parameter WIDTH = 8, // parameter WIDTH with default value 8,
    parameter DEPTH = 16, // parameter DEPTH with default value 16,
    parameter ADDR_WIDTH = 4 // parameter ADDR_WIDTH with default value 4
)(
    // Inputs
    input wire clk, // input clock
    input wire reset, // input reset
    input wire [WIDTH-1:0] data_in, // WIDTH-bit input wire array for <7>
    input logic [DEPTH-1:0] enable, // DEPTH-bit input logic array for <5>
    input bit [7:0] config, // 7-bit input bit array for <10>
    input reg [3:0] mode, // 3-bit input reg array for <8>
    input wire [15:0] address, // (15+1)-bit input wire array for <11>
    input [31:0] instruction, // (31 + 1)-bit input array for <2>
    input wire start, // 1-bit input wire for <15>
    input wire [ADDR_WIDTH-1:0] write_addr, // ADDR_WIDTH-bit input wire array for <7>
    input logic [15:0] mask, // 15-bit input logic array for <9>
    input wire init, // 1-bit input wire for <15>
    input bit stop, // 1-bit input bit for <14>
    input [WIDTH-1:0] threshold, // WIDTH-bit input array for <1>
    input logic [3:0] status, // 3-bit input logic array for <9>
    input wire ready, // 1-bit input wire for <15>
    input bit [7:0] flag, // 7-bit input bit array for <10>
    input reg [DEPTH-1:0] counter, // DEPTH-bit input reg array for <4>
    input logic [WIDTH-1:0] buffer, // WIDTH-bit input logic array for <5>
    input wire [WIDTH-1:0] temp, // WIDTH-bit input wire array for <7>
    input bit [3:0] cmd, // 3-bit input bit array for <10>
    input reg [7:0] control, // 7-bit input reg array for <8>
    input wire [15:0] shift, // (15+1)-bit input wire array for <11>
    input logic [7:0] interrupt, // 7-bit input logic array for <9>
    input wire done, // 1-bit input wire for <15>
    input [WIDTH-1:0] data_in_ext, // WIDTH-bit input array for <1>

    // Outputs
    output wire [WIDTH-1:0] data_out, // WIDTH-bit output wire array for <26>
    output logic [DEPTH-1:0] status_out, // DEPTH-bit output logic array for <24>
    output bit [7:0] config_out, // (7 + 1)-bit output bit array for <29>
    output reg [3:0] mode_out, // (3 + 1)-bit output reg array for <27>
    output wire [15:0] address_out, // (15 + 1)-bit output wire array for <30>
    output [31:0] result, // (31 + 1)-bit output array for <17>
    output wire complete, // 1-bit output wire for <22>
    output wire [ADDR_WIDTH-1:0] read_addr, // ADDR_WIDTH-bit output wire array for <26>
    output logic [15:0] mask_out, // (15 + 1)-bit output logic array for <28>
    output wire init_done, // 1-bit output wire for <22>
    output bit stop_ack, // 1-bit output bit for <21>
    output [WIDTH-1:0] threshold_out, // WIDTH-bit output array for <16>
    output logic [3:0] status_flag, // (3 + 1)-bit output logic array for <28>
    output wire ready_signal, // 1-bit output wire for <22>
    output bit [7:0] error_flag, // (7 + 1)-bit output bit array for <29>
    output reg [DEPTH-1:0] counter_out, // DEPTH-bit output reg array for <23>
    output logic [WIDTH-1:0] buffer_out, // WIDTH-bit output logic array for <24>
    output wire [WIDTH-1:0] temp_out, // WIDTH-bit output wire array for <26>
    output bit [3:0] cmd_out, // (3 + 1)-bit output bit array for <29>
    output reg [7:0] control_out, // (7 + 1)-bit output reg array for <27>
    output wire [15:0] shift_out, // (15 + 1)-bit output wire array for <30>
    output logic [7:0] interrupt_out, // (7 + 1)-bit output logic array for <28>
    output wire task_done, // 1-bit output wire for <22>
    output [WIDTH-1:0] data_out_ext, // WIDTH-bit output array for <16>

    // Inouts
    inout wire [WIDTH-1:0] bidir_data, // WIDTH-bit inout wire array for <41>
    inout logic [DEPTH-1:0] bidir_status, // DEPTH-bit inout logic array for <39>
    inout bit [7:0] bidir_config, // (7 + 1)-bit inout bit array for <44>
    inout reg [3:0] bidir_mode, // (3 + 1)-bit inout reg array for <42>
    inout wire [15:0] bidir_address, // (15 + 1)-bit inout wire array for <45>
    inout [31:0] bidir_instruction, // (31 + 1)-bit inout array for <32>
    inout wire bidir_start, // 1-bit inout wire for <37>
    inout wire [ADDR_WIDTH-1:0] bidir_write_addr, // ADDR_WIDTH-bit inout wire array for <41>
    inout logic [15:0] bidir_mask, // (15 + 1)-bit inout logic array for <43>
    inout wire bidir_init, // 1-bit inout wire for <37>
    inout bit bidir_stop
);

// Module implementation here

endmodule
