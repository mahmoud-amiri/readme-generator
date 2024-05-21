module state_machine (
    input wire clk,
    input wire reset,
    input wire start,
    input wire write_signal,
    input wire data_read_complete,
    input wire processing_complete,
    input wire write_complete,
    input wire error,
    output reg [2:0] state,
    output reg read_data,
    output reg process_data,
    output reg write_data,
    output reg handle_error
);

// State encoding
localparam IDLE    = 3'b000;
localparam READ    = 3'b001;
localparam PROCESS = 3'b010;
localparam WRITE   = 3'b011;
localparam ERROR   = 3'b100;

reg [2:0] next_state;

// State transition
always @(posedge clk or posedge reset) begin
    if (reset) begin
        state <= IDLE;
    end else begin
        state <= next_state;
    end
end

// Next state logic
always @(*) begin
    case (state)
        IDLE: begin
            if (start) begin
                next_state = READ;
            end else if (write_signal) begin
                next_state = WRITE;
            end else begin
                next_state = IDLE;
            end
        end
        READ: begin
            if (data_read_complete) begin
                next_state = PROCESS;
            end else if (error) begin
                next_state = ERROR;
            end else begin
                next_state = READ;
            end
        end
        PROCESS: begin
            if (processing_complete) begin
                next_state = WRITE;
            end else if (error) begin
                next_state = ERROR;
            end else begin
                next_state = PROCESS;
            end
        end
        WRITE: begin
            if (write_complete) begin
                next_state = IDLE;
            end else if (error) begin
                next_state = ERROR;
            end else begin
                next_state = WRITE;
            end
        end
        ERROR: begin
            if (reset) begin
                next_state = IDLE;
            end else begin
                next_state = ERROR;
            end
        end
        default: next_state = IDLE;
    endcase
end

// Output logic
always @(posedge clk or posedge reset) begin
    if (reset) begin
        read_data    <= 0;
        process_data <= 0;
        write_data   <= 0;
        handle_error <= 0;
    end else begin
        case (state)
            IDLE: begin
                read_data    <= 0;
                process_data <= 0;
                write_data   <= 0;
                handle_error <= 0;
            end
            READ: begin
                read_data    <= 1;
                process_data <= 0;
                write_data   <= 0;
                handle_error <= 0;
            end
            PROCESS: begin
                read_data    <= 0;
                process_data <= 1;
                write_data   <= 0;
                handle_error <= 0;
            end
            WRITE: begin
                read_data    <= 0;
                process_data <= 0;
                write_data   <= 1;
                handle_error <= 0;
            end
            ERROR: begin
                read_data    <= 0;
                process_data <= 0;
                write_data   <= 0;
                handle_error <= 1;
            end
        endcase
    end
end

endmodule