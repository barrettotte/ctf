#!/bin/bash

# iverilog encoder_tb.v -o encoder.vvp
# vvp encoder.vvp
# gtkwave encoder.vcd

iverilog encoder.sv -o encoder.vvp
vvp encoder.vvp
