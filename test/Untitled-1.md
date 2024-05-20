#### Ports
| Port Name    | Direction | Width | Description                               |
|--------------|-----------|-------|-------------------------------------------|
| `clk`         | input    | 1    | input clock                               |
| `reset`       | input    | 1    | input reset                               |
| `threshold`   | input    | WIDTH| WIDTH-bit input array for <1>             |
| `data_in_ext` | input    | WIDTH| WIDTH-bit input array for <1>             |
| `instruction` | input    | 31   | (31 + 1)-bit input array for <2>          |
| `counter`     | input    | DEPTH| DEPTH-bit input reg array for <4>         |
| `enable`      | input    | DEPTH| DEPTH-bit input logic array for <5>       |
| `buffer`      | input    | WIDTH| WIDTH-bit input logic array for <5>       |
| `data_in`     | input    | WIDTH| WIDTH-bit input wire array for <7>        |
| `write_addr`  | input    | ADDR_WIDTH| ADDR_WIDTH-bit input wire array for <7>   |
| `temp`        | input    | WIDTH| WIDTH-bit input wire array for <7>        |
| `mode`        | input    | 3    | 3-bit input reg array for <8>             |
| `control`     | input    | 7    | 7-bit input reg array for <8>             |
| `mask`        | input    | 15   | 15-bit input logic array for <9>          |
| `status`      | input    | 3    | 3-bit input logic array for <9>           |
| `interrupt`   | input    | 7    | 7-bit input logic array for <9>           |
| `config`      | input    | 7    | 7-bit input bit array for <10>            |
| `flag`        | input    | 7    | 7-bit input bit array for <10>            |
| `cmd`         | input    | 3    | 3-bit input bit array for <10>            |
| `address`     | input    | 15   | (15+1)-bit input wire array for <11>      |
| `shift`       | input    | 15   | (15+1)-bit input wire array for <11>      |
| `stop`        | input    | 1    | 1-bit input bit for <14>                  |
| `start`       | input    | 1    | 1-bit input wire for <15>                 |
| `init`        | input    | 1    | 1-bit input wire for <15>                 |
| `ready`       | input    | 1    | 1-bit input wire for <15>                 |
| `done`        | input    | 1    | 1-bit input wire for <15>                 |
| `threshold_out`| output   | WIDTH| WIDTH-bit output array for <16>           |
| `data_out_ext`| output   | WIDTH| WIDTH-bit output array for <16>           |
| `result`      | output   | 31   | (31 + 1)-bit output array for <17>        |
| `stop_ack`    | output   | 1    | 1-bit output bit for <21>                 |
| `complete`    | output   | 1    | 1-bit output wire for <22>                |
| `init_done`   | output   | 1    | 1-bit output wire for <22>                |
| `ready_signal`| output   | 1    | 1-bit output wire for <22>                |
| `task_done`   | output   | 1    | 1-bit output wire for <22>                |
| `counter_out` | output   | DEPTH| DEPTH-bit output reg array for <23>       |
| `status_out`  | output   | DEPTH| DEPTH-bit output logic array for <24>     |
| `buffer_out`  | output   | WIDTH| WIDTH-bit output logic array for <24>     |
| `data_out`    | output   | WIDTH| WIDTH-bit output wire array for <26>      |
| `read_addr`   | output   | ADDR_WIDTH| ADDR_WIDTH-bit output wire array for <26> |
| `temp_out`    | output   | WIDTH| WIDTH-bit output wire array for <26>      |
| `mode_out`    | output   | 3    | (3 + 1)-bit output reg array for <27>     |
| `control_out` | output   | 7    | (7 + 1)-bit output reg array for <27>     |
| `mask_out`    | output   | 15   | (15 + 1)-bit output logic array for <28>  |
| `status_flag` | output   | 3    | (3 + 1)-bit output logic array for <28>   |
| `interrupt_out`| output   | 7    | (7 + 1)-bit output logic array for <28>   |
| `config_out`  | output   | 7    | (7 + 1)-bit output bit array for <29>     |
| `error_flag`  | output   | 7    | (7 + 1)-bit output bit array for <29>     |
| `cmd_out`     | output   | 3    | (3 + 1)-bit output bit array for <29>     |
| `address_out` | output   | 15   | (15 + 1)-bit output wire array for <30>   |
| `shift_out`   | output   | 15   | (15 + 1)-bit output wire array for <30>   |
| `bidir_instruction`| inout    | 31   | (31 + 1)-bit inout array for <32>         |
| `bidir_start` | inout    | 1    | 1-bit inout wire for <37>                 |
| `bidir_init`  | inout    | 1    | 1-bit inout wire for <37>                 |
| `bidir_status`| inout    | DEPTH| DEPTH-bit inout logic array for <39>      |
| `bidir_data`  | inout    | WIDTH| WIDTH-bit inout wire array for <41>       |
| `bidir_write_addr`| inout    | ADDR_WIDTH| ADDR_WIDTH-bit inout wire array for <41>  |
| `bidir_mode`  | inout    | 3    | (3 + 1)-bit inout reg array for <42>      |
| `bidir_mask`  | inout    | 15   | (15 + 1)-bit inout logic array for <43>   |
| `bidir_config`| inout    | 7    | (7 + 1)-bit inout bit array for <44>      |
| `bidir_address`| inout    | 15   | (15 + 1)-bit inout wire array for <45>    |