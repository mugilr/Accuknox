#!/usr/bin/python

from bcc import BPF

device = "lo"
b = BPF(src_file="tcp_block.c")
fn = b.load_func("filter", BPF.XDP)
b.attach_xdp(device, fn, 0)

try:
  b.trace_print()
except KeyboardInterrupt:
  pass

b.remove_xdp(device, 0)
