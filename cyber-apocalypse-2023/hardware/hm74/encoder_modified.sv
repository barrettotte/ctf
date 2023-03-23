module encoder(
    input [3:0] data_in,
    output [6:0] ham_out
    );
 
    wire p0, p1, p2;
 
    assign p0 = data_in[3] ^ data_in[2] ^ data_in[0];
    assign p1 = data_in[3] ^ data_in[1] ^ data_in[0];
    assign p2 = data_in[2] ^ data_in[1] ^ data_in[0];
    
    assign ham_out = {p0, p1, data_in[3], p2, data_in[2], data_in[1], data_in[0]};
endmodule

module main;
    reg[3:0] data_in = 5;
    wire[6:0] ham_out;

    encoder en(data_in, ham_out);

    initial begin
        #10;

        data_in = 0;
        $display("%b = %b", data_in, ham_out);
        #10;
        
        data_in = 1;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 2;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 3;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 4;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 5;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 6;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 7;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 8;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 9;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 10;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 11;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 12;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 13;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 14;
        $display("%b = %b", data_in, ham_out);
        #10;

        data_in = 15;
        $display("%b = %b", data_in, ham_out);
        #10;

    end
endmodule
